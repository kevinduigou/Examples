from sqlalchemy.orm import sessionmaker

from models import Student

from sqlalchemy import create_engine

DATABASE_URI="sqlite:///myDb.db"
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

session = Session()

student = session.query(Student).filter_by(name="DUIGOU").first()
print(student)
#student = Student(name="DUIGOU")
#s.add(student)
#session.commit()
session.close()

