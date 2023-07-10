from sqlalchemy import Column,Integer, String
from scripts.utils.sql_utility import Base


class Book(Base):
    __tablename__ = "AlivaLibraray"

    book_id = Column(Integer, primary_key=True)
    book_title = Column(String)
    book_author = Column(String)
    book_year= Column(Integer)

