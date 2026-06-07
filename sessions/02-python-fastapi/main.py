import json
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI()
DATA_FILE = Path(__file__).with_name("students.json")

with DATA_FILE.open("r", encoding="utf-8") as file:
    students = json.load(file)


class StudentModel(BaseModel):
    name: str
    age: int
    major: str


@app.get("/")
def root():
    return {"Home": "Our home endpoint"}


@app.get("/studentdata/{id}")
def search_student(id: str):
    if id in students:
        return students[id]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="No student with such id"
    )


@app.post("/studentdata")
def add_student(body: StudentModel):
    next_id = max([int(student_id) for student_id in students] or [0]) + 1
    key = str(next_id)
    students[key] = {
        "id": next_id,
        **body.model_dump(),
    }
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    return students[key]


@app.delete("/studentdata/{id}")
def deletestudent(id: int):
    try:
        students.pop(str(id))
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return {"detail": f"student with id {id} has been deleted"}
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="given id not found",
        )
