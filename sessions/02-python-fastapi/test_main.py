import json

from fastapi.testclient import TestClient

import main


def reset_students(tmp_path):
    data_file = tmp_path / "students.json"
    main.DATA_FILE = data_file
    main.students = {
        "1": {
            "id": 1,
            "name": "Ayesha Khan",
            "age": 20,
            "major": "Computer Science",
        }
    }
    data_file.write_text(json.dumps(main.students), encoding="utf-8")


def test_root():
    client = TestClient(main.app)

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Home": "Our home endpoint"}


def test_get_existing_student(tmp_path):
    reset_students(tmp_path)
    client = TestClient(main.app)

    response = client.get("/studentdata/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Ayesha Khan"


def test_get_missing_student_returns_404(tmp_path):
    reset_students(tmp_path)
    client = TestClient(main.app)

    response = client.get("/studentdata/99")

    assert response.status_code == 404
    assert response.json()["detail"] == "No student with such id"


def test_create_and_delete_student(tmp_path):
    reset_students(tmp_path)
    client = TestClient(main.app)

    create_response = client.post(
        "/studentdata",
        json={"name": "Muhammad Ali", "age": 21, "major": "AI"},
    )

    assert create_response.status_code == 200
    assert create_response.json() == {
        "id": 2,
        "name": "Muhammad Ali",
        "age": 21,
        "major": "AI",
    }
    assert "2" in main.students

    delete_response = client.delete("/studentdata/2")

    assert delete_response.status_code == 200
    assert delete_response.json() == {"detail": "student with id 2 has been deleted"}
    assert "2" not in main.students

