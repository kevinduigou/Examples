from sqlalchemy import Column, INTEGER, String

from models.base import Base


class Book(Base):

    __tablename__ = 'book'

    id = Column(INTEGER(), primary_key=True)
    name = Column(String(11))
    author = Column(String(11))