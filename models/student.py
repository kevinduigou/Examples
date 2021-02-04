from sqlalchemy import Column, String, JSON, TIMESTAMP, text, INTEGER

from models.base import Base


class Student(Base):

    __tablename__ = 'student'

    id = Column(INTEGER(), primary_key=True)
    enroll = Column(INTEGER())
    personal_info = Column(JSON)
    name= Column(String(255))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    def __repr__(self):
        return f"{self.name} (created on ,{self.created_on})"