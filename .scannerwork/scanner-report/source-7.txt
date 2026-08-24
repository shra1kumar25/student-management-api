import os

import jwt
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel

from app.auth import verify_access_token
from app.database import Base, engine
from app.models import Student
from app.routes import router as student_router

load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="REST API for managing students",
    version="1.0.0",
)


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/")
def root():
    return {
        "message": "Student Management API is running"
    }


@app.post("/login")
def login(request: LoginRequest):
    # Simple credentials for learning/testing
    if request.username != "admin" or request.password != "admin123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    payload = {
        "sub": request.username,
        "role": "admin",
    }

    access_token = jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@app.get("/protected")
def protected_route(
    current_user: dict = Depends(verify_access_token),
):
    return {
        "message": "You have access to the protected API",
        "token_data": current_user,
    }

app.include_router(student_router)


@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "service": "student-management-api"
    }