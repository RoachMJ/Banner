from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    ForeignKey, Table)
from sqlalchemy.orm import relationship

from .meta import Base


class Section(Base):
    __tablename__ = 'Sections'
    id = Column(Integer, primary_key=True)
    number = Column(String(4))
    professor_id = Column(Integer, ForeignKey('Professors.id'))
    professor_name = relationship("Professor")
    course_id = Column(Integer, ForeignKey('Courses.id'))
    course_name = relationship("Course")
