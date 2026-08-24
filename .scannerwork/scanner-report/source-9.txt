from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "UP",
        "service": "student-management-api",
    }
def test_login_success():
    response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "admin123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials():
    response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"

def test_protected_route():
    login_response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "admin123",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.get(
        "/protected",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200
    assert response.json()["message"] == (
        "You have access to the protected API"
    )
def test_protected_route_without_token():
    response = client.get("/protected")

    assert response.status_code == 401
def test_student_details_pagination():
    login_response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "admin123",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/students/details",
        params={
            "course": "B.Tech",
            "limit": 5,
            "offset": 0,
            "sort_by": "id",
            "sort_order": "asc",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 5001
    assert data["limit"] == 5
    assert data["offset"] == 0
    assert len(data["students"]) == 5

    for student in data["students"]:
        assert student["course_name"] == "B.Tech"

def test_student_details_cursor_pagination():
    login_response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "admin123",
        },
    )

    token = login_response.json()["access_token"]

    first_response = client.get(
        "/students/details",
        params={
            "course": "B.Tech",
            "limit": 5,
            "offset": 0,
            "sort_by": "id",
            "sort_order": "asc",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert first_response.status_code == 200

    first_data = first_response.json()
    cursor = first_data["next_cursor"]

    assert cursor is not None

    second_response = client.get(
        "/students/details",
        params={
            "course": "B.Tech",
            "limit": 5,
            "offset": 0,
            "last_id": cursor,
            "sort_by": "id",
            "sort_order": "asc",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert second_response.status_code == 200

    second_data = second_response.json()

    assert len(second_data["students"]) == 5

    assert (
        second_data["students"][0]["id"]
        > first_data["students"][-1]["id"]
    )
