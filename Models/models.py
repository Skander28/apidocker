from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Database.database import Base


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    rating = Column(Integer)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship("Author")


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
