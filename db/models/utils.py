import datetime as dt

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declared_attr, declarative_base

from db.config import SQLA_URL

engine = create_engine(SQLA_URL, echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base(bind=engine)


def to_snake_case(s):
    return ''.join(['_'+c.lower() if c == c.upper() and i!=0 else c.lower() for (i, c) in enumerate(s)])


class BaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(self):
        return to_snake_case(self.__name__)

    created_datetime = Column(DateTime, default=dt.datetime.utcnow())
    updated_datetime = Column(
        DateTime, default=dt.datetime.utcnow(),
        onupdate=dt.datetime.utcnow()
    )

    created_datetime._creation_order = 998
    updated_datetime._creation_order = 999

    def __str__(self):
        return f'<{self.__class__.__name__} ({self.id})>'
    
    __repr__ = __str__


class AutoPKBaseModel(BaseModel):
    __abstract__ = True

    id = Column(Integer(), primary_key=True)
