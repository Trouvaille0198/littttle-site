from typing import List
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
# from utils import logger
from schemas.course import *
from utils import CourseHelper


router = APIRouter()


@router.post('/login', tags=['login'])
def login(login_info: LoginInfo):
    global xk
    xk = CourseHelper(login_info.stu_id, login_info.password, login_info.term_id)
    return {'login_state': xk.login_state}


@router.get('/course_rank',  response_model=List[CourseRank], tags=['Get SHU course rank'])
def get_course_rank():
    return xk.switch2dict(xk.get_course_rank())


@router.get('/course_info', response_model=List[CourseInfo], tags=['Get SHU course information'])
def get_course_info():
    return xk.switch2dict(xk.get_course_info())


@router.get('/course_table',  response_model=List[CourseTable], tags=['Get SHU course table'])
def get_course_table():
    return xk.switch2dict(xk.get_course_table())


@router.get('/stu_info',  response_model=StuInfo, tags=['Get SHU self info'])
def get_stu_info():
    return xk.switch2dict(xk.get_stu_info())[0]
