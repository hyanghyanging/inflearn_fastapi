from typing import List

from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from fastapi import Depends

from database.connection import get_db
from database.orm import ToDo, User


class ToDoRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_todos(self) -> List[ToDo]:
        return list(self.session.scalars(select(ToDo)))   # 전체 todo를 조회해서 return

    def get_todo_by_todo_id(self, todo_id: int) -> ToDo | None:
        return self.session.scalar(select(ToDo).where(ToDo.id == todo_id))    # todo가 존재하는 경우 todo, 존재하지 않는 경우 None 리턴

    def create_todo(self, todo: ToDo) -> ToDo:
        self.session.add(instance=todo)
        self.session.commit()   # 실제 데이터베이스에 저장 : todo_id는 모르는 상태
        self.session.refresh(instance=todo)   # 다시 데이터베이스를 읽어옴  -> todo_id 결정
        return todo

    def update_todo(self, todo: ToDo) -> ToDo:
        self.session.add(instance=todo)
        self.session.commit()    # db save
        self.session.refresh(instance=todo)
        return todo                               # create_todo와 update_todo의 코드는 동일하지만 레포지토리 패턴 특성상 명시적으로 분리하는 것이 좋음.

    def delete_todo(self, todo_id:int) -> None:
        self.session.execute(delete(ToDo).where(ToDo.id == todo_id))
        self.session.commit()

class UserRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_user_by_username(self, username: str) -> User | None:
        return  self.session.scalar(
            select(User).where(User.username == username)
        )

    def save_user(self, user: User) -> User:
        self.session.add(instance=user)
        self.session.commit()  # db save
        self.session.refresh(instance=user)
        return user

