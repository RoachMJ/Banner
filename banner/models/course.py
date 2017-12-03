from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    ForeignKey, Table)
from sqlalchemy.orm import relationship

from .meta import Base


class Course(Base):
    __tablename__ = 'Courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(15))