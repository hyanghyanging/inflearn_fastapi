from datetime import datetime, timedelta

import bcrypt
from jose import jwt

class UserService:
    encoding: str = "UTF-8"
    secret_key: str = "935809a934f7398906418f656c35cf3dfa7487d5827728d76c886d4f8c10edfb"
    jwt_algorithm: str = "HS256"

    def hash_password(self, plain_password: str) -> str:
        hashed_password: bytes = bcrypt.hashpw(
            plain_password.encode(self.encoding),
            salt = bcrypt.gensalt(),
        )
        return hashed_password.decode(self.encoding)

    def verify_password(
            self, plain_password: str, hashed_password: str
    )-> bool:
        # try/except
        return bcrypt.checkpw(
            plain_password.encode(self.encoding),
            hashed_password.encode(self.encoding)
        )

    def create_jwt(self, username: str) -> str:
        return jwt.encode(
            {
                "sub":username,
                "exp":datetime.now() + timedelta(days=1),
             },
            self.secret_key,
            algorithm=self.jwt_algorithm,
        )