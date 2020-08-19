from sqlalchemy import (
    Column, String, Integer, ForeignKey, Text, DateTime, Boolean
)

from db.models.utils import AutoPKBaseModel

__author__ = 'premkumar30'


class Group(AutoPKBaseModel):
    name = Column(String(200))
    description = Column(Text)


class GroupMember(AutoPKBaseModel):
    group_id = Column(Integer, ForeignKey('group.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    removed = Column(Boolean, default=False)


class GroupPermission(AutoPKBaseModel):
    group_id = Column(Integer, ForeignKey('group.id'))
    permission_id = Column(Integer, ForeignKey('permission.id'))

    active = Column(Boolean, default=True)
