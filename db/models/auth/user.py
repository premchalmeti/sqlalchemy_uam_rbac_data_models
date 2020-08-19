from sqlalchemy import (
    Column, String, Integer, ForeignKey, Text, DateTime, Boolean
)

from db.models.utils import AutoPKBaseModel

__author__ = 'premkumar30'


class UserEmail(AutoPKBaseModel):
    user_id = Column(Integer, ForeignKey('user.id'))

    primary_email = Column(String(255), nullable=False, unique=True)
    secondary_email = Column(String(255), unique=True)


class User(AutoPKBaseModel):
    first_name =  Column(String(150))
    last_name =  Column(String(150))

    username = Column(String(255), unique=True)
    avatar = Column(Text)
    bio = Column(Text)
    role = Column(Integer, ForeignKey('role.id'))
    geography_id = Column(Integer, ForeignKey('geography.id'))

    password = Column(Text)
    last_login = Column(DateTime)

    locked = Column(Boolean, default=False)


class UserPermission(AutoPKBaseModel):
    role_id = Column(Integer, ForeignKey('role.id'))
    permission_id = Column(Integer, ForeignKey('permission.id'))

    active = Column(Boolean, default=True)
