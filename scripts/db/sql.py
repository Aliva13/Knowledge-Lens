from sqlalchemy.orm import Session
from scripts.schemas.sql_model import Book
from scripts.logging.logs import logger

class sql_book_handler:

    def find_by_id(self,book_id: int,db: Session):
        try:
            data= db.query(Book).filter(Book.book_id == book_id).first()
            if data:
                return [data]
            else:
                return []
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}  
        


    def fetch(self, db: Session):
        return db.query(Book).all()

    def get_home_page(self, db: Session):
        return "Welcome to My Library"




    def delete_book(self,book_id: int,db: Session):
        book = db.query(Book).get(book_id)
        if book:
            db.delete(book)
            db.commit()
            return True
        return False

    def update_book(self, book_id: int, updated_values: dict,db: Session):
        book = db.query(Book).get(book_id)
        if book:
            for key, value in updated_values.items():
                setattr(book, key, value)
            db.commit()
            return True
        return False


    def add_book(self,book_id,book,db: Session):
        db_book = Book(book_id=book.book_id,book_title=book.book_title,book_author=book.book_author,book_year=book.book_year)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

sql_book_object=sql_book_handler()