from typing import List

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    student_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )
    email: EmailStr
    course: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )
    year: int = Field(
        ...,
        ge=1,
        le=10,
    )

class StudentResponse(BaseModel):
    id: int
    student_name: str
    email: EmailStr
    course: str
    year: int

    model_config = ConfigDict(from_attributes=True)


class StudentDetailsResponse(BaseModel):
    id: int
    student_name: str
    email: EmailStr
    course_name: str
    year: int

    model_config = ConfigDict(from_attributes=True)


class StudentDetailsPaginatedResponse(BaseModel):
    total: int
    limit: int
    offset: int
    next_cursor: int | None
    students: List[StudentDetailsResponse]
