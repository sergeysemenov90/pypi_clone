from typing import Optional

from data.user import User


def user_count() -> int:
    return 3_272_115


def create_account(name: str, email: str, password: str) -> User:
    return User(name, email, password)


def login_user(email: str, password: str) -> Optional[User]:
    if password == 'abc':
        return User('test_user', email, 'abc')
    return None
