from sqlalchemy import INTEGER, String, Column

from models.base import Base


class School(Base):

    __tablename__ = 'school'

    id = Column(INTEGER(), primary_key=True)
    name = Column(String(11))