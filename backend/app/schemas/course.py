from typing import List, Optional
from pydantic import BaseModel


class LoginInfo(BaseModel):
    stu_id: str
    password: str
    term_id: str = '秋'


class CourseRank(BaseModel):
    course_id: str
    course_name: str
    teacher_id: str
    teacher_name: str
    capacity: str
    number: str
    rank: str


class StuInfo(BaseModel):
    stu_id: str
    name: str
    sexual: str
    grade: str
    academy: str
    campus: str
    credit: str


class CourseInfo(BaseModel):
    id: str
    course_id: str
    course_name: str
    credit: str
    teacher_id: str
    teacher_name: str
    course_time: str
    course_location: str
    question_time: str
    question_location: str
    campus: str


class CourseTable(BaseModel):
    id: str
    time: str
    Mon: str
    Tues: str
    Wed: str
    Thur: str
    Fri: str
    Sat: str
    Sun: str
