from pydantic import BaseModel


class Book(BaseModel):
    book_id:int
    book_title: str
    book_author: str
    book_year: int
    class Config:
        orm_mode=True