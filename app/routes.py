from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.auth import verify_access_token
from app.database import get_db
from app.models import Student
from app.schemas import (
    StudentCreate,
    StudentResponse,
    StudentDetailsResponse,
    StudentDetailsPaginatedResponse,
)


router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


# ---------------------------------------------------------
# GET ALL STUDENTS
# GET /students/
# GET /students/?course=B.Tech
# ---------------------------------------------------------
@router.get(
    "/",
    response_model=List[StudentResponse],
    status_code=status.HTTP_200_OK,
)
def get_all_students(
    course: str | None = Query(default=None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(verify_access_token),
):
    try:
        query = db.query(Student)

        if course:
            query = query.filter(Student.course == course)

        students = query.all()

        return students

    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to retrieve students",
        ) from None


# ---------------------------------------------------------
# GET STUDENT DETAILS FROM POSTGRESQL VIEW
# GET /students/details
#
# Supports:
# ?course=B.Tech
# ?limit=5
# ?offset=0
# ---------------------------------------------------------
@router.get(
    "/details",
    response_model=StudentDetailsPaginatedResponse,
    status_code=status.HTTP_200_OK,
)
def get_student_details(
    course: str | None = Query(default=None),
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    last_id: int | None = Query(default=None, ge=0),
    sort_by: str = Query(default="id"),
    sort_order: str = Query(default="asc"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(verify_access_token),
):
    try:
        allowed_sort_columns = {
            "id": "id",
            "student_name": "student_name",
            "email": "email",
            "course_name": "course_name",
            "year": "year",
        }

        if sort_by not in allowed_sort_columns:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    "Invalid sort_by. Allowed values: "
                    "id, student_name, email, course_name, year"
                ),
            )

        if sort_order not in {"asc", "desc"}:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid sort_order. Allowed values: asc, desc",
            )

        count_query = """
            SELECT COUNT(*)
            FROM student_details_view
        """

        data_query = """
            SELECT *
            FROM student_details_view
        """

        params = {}

        # Course filter
        if course:
            count_query += " WHERE course_name = :course"
            data_query += " WHERE course_name = :course"
            params["course"] = course

        # Cursor filter
        if last_id is not None:
            if course:
                data_query += " AND id > :last_id"
            else:
                data_query += " WHERE id > :last_id"

            params["last_id"] = last_id

        # Total count
        count_result = db.execute(
            text(count_query),
            params,
        )

        total = count_result.scalar_one()

        # Sorting + pagination
        sort_column = allowed_sort_columns[sort_by]
        order = sort_order.upper()

        data_query += (
            f" ORDER BY {sort_column} {order}"
            " LIMIT :limit OFFSET :offset"
        )

        params["limit"] = limit
        params["offset"] = offset

        # Fetch students
        result = db.execute(
            text(data_query),
            params,
        )

        students = result.mappings().all()

        # Cursor for next page
        next_cursor = students[-1]["id"] if students else None

        return {
            "total": total,
            "limit": limit,
            "offset": offset,
            "next_cursor": next_cursor,
            "students": students,
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to retrieve student details",
        ) from None 
