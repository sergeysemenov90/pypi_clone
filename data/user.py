import datetime
from sqlalchemy import Column, Integer, String, DateTime
from data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hash_password = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.now, index=True)
    last_login = Column(DateTime, default=datetime.datetime.now)
    profile_image_url = Column(String)
