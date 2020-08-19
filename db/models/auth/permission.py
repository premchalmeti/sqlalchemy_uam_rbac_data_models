
from sqlalchemy import Column, String, Text

from db.models.utils import AutoPKBaseModel

__author__ = 'premkumar30'


class Permission(AutoPKBaseModel):
    name = Column(String(1000))
    description = Column(Text)
