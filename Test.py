from socketserver import UDPServer
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Data" : "Home"}

@app.get("/about")
def about():
    return {"Info" : "About..."}

students = {
    12345:{"first": "ABC", "last" : "DEF", "grade" : 12},
    67890:{"first": "GHI", "last" : "JKL", "grade" : 11}
}
@app.get("/get-student/{student_id}")
def get_students(student_id : int):
    return students[student_id]

@app.get("/get-student/{student_id}/{first_name}")
def get_students(student_id : int, first_name : str):
    if first_name == students[student_id]["first"]:
        return students[student_id]
    else:
        return {"Error" : "Access denied"}

@app.get("/get-by-name/{name}")
def get_student(name : str):
    for id in students:
        if students[id]["first"] == name:
            return id
    return {"Error" : "Student Not Found"}

from pydantic import BaseModel

class Student(BaseModel):
    first:str
    last:str
    grade:int

@app.post("/create-student/{id}")
def create_student(id : int, st : Student):
    if id in students:
        return {"Error" : "ID already assigned"}
    else:
        students[id] = {"first": st.first, "last" : st.last, "grade" : st.grade}
        return {"Success": "Student created"}

@app.put("/update-student/{id}")
def update_student(id: int, st: Student):
    if id not in students:
        return {"Error": "Student does not exist, cannot modify!"}
    if st.first != None:
        students[id]["first"] = st.first
    if st.last != None:
        students[id]["last"] = st.last
    if st.grade != None:
        students[id]["grade"] = st.grade
    return students[id]

@app.delete("/delete-student/{id}")
def delete_student(id: int):
    if id not in students:
        return {"Error": "Student does not exist"}
    else:
        del students[id]
        return {"Success": "Student Erased"}