from fastapi import APIRouter
from routers.api_v1 import todos, steam, course

api_router = APIRouter()
# router注册
api_router.include_router(todos.router, prefix='/todos', tags=['todo api'])
api_router.include_router(steam.router, prefix='/steam', tags=['steam api'])
api_router.include_router(course.router, prefix='/course', tags=['SHU course api'])
