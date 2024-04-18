from pydantic.v1 import BaseModel
from typing import List

class ToDoSchema(BaseModel):
    id : int
    contents : str
    is_done : bool

    class Config:       # pydantic에서 sqlalchemy를 바로 읽어오게 하는 옵션
        orm_mode = True


class ToDoListSchema(BaseModel):
    todos: List[ToDoSchema]

class UserSchema(BaseModel):
    id: int
    username: str

    class Config:       # pydantic에서 sqlalchemy를 바로 읽어오게 하는 옵션
        orm_mode = True

class JWTResponse(BaseModel):
    access_token: str
# test