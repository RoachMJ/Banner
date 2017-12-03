from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    ForeignKey, Table)
from sqlalchemy.orm import relationship

from .meta import Base

#one to many relationship
'''
class Course(Base):
    __tablename__ = 'course'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(Text)


class Professor(Base):
    __tablename__ = 'professor'
    professor_id = Column(Integer, primary_key=True)
    professor_name = Column(Text)


class Section(Base):
    __tablename__ = 'section'
    section_id = Column(Integer, primary_key=True)
    section_name = Column(String(4))
    professor_id = Column(Integer, ForeignKey('professors.professor_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
'''

#many to one relationhip









#     TODO Need to implement these tables throughout the code so we can finish this project,
#     TODO will need 3 jinja files view files 3 create files
'''
#many to many

Section = Table('association', Base.metadata,
                Column('Professors_id', Integer, ForeignKey('Professors.id')), Column('Courses_id', Integer, ForeignKey('Courses.id')))


class Professor(Base):
    __tablename__ = 'Professors'
    id = Column(Integer, primary_key=True)
    course = relationship("Course", secondary=Section)
    name = Column(String(15))


class Course(Base):
    __tablename__ = 'Courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(15))

'''
