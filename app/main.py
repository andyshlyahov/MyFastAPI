from fastapi import FastAPI, HTTPException
from utils import json_to_dict_list
import os
from typing import Optional

# script_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(script_dir)
# path_to_json = os.path.join(parent_dir, "students.json")

path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'students.json')

app = FastAPI()

@app.get("/")
def home_page():
    return {"Message": "Hello, Andy!"}


# @app.get("/students")
# def get_all_students():
#     return json_to_dict_list(path_to_json)

# @app.get("/students/{course}")
# def get_all_students_course(course: int):
#     students = json_to_dict_list(path_to_json)
#     return_list = []
#     for student in students:
#         if student["course"] == course:
#             return_list.append(student)
#     return return_list

@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    return_list = []
    for student in students:
        if student["course"] == course:
            return_list.append(student)
    return return_list

@app.get("/students/{course}")
def get_all_students_course(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        flag = (student["course"] == course)
        if major:
            flag &= (student["major"].lower() == major.lower())
        if enrollment_year:
            flag &= (student["enrollment_year"] == enrollment_year)
        if flag:
            filtered_students.append(student)
    return filtered_students

@app.get("/student/{student_id}")
def get_student_from_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail=f"Student with id={student_id} not found")

@app.get("/student")
def get_student_param_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail=f"Student with id={student_id} not found")
