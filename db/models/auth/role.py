
from sqlalchemy import (
    Column, String, Boolean, Text
)

from db.models.utils import AutoPKBaseModel

__author__ = 'premkumar30'


class Role(AutoPKBaseModel):
    name = Column(String(100))
    description = Column(Text)

    active = Column(Boolean, default=True)
