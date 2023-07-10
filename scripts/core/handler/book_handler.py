from scripts.logging.logs import logger
from scripts.schemas.sql_schemas import Book
from scripts.db.sql import sql_book_object
from sqlalchemy.orm import Session


class Book_handler:
    def fetch(self, db: Session):
        try:
            all_books = sql_book_object.fetch(db)
            if all_books == []:
                logger.warning({"Warning": "No books present in the database"})
                return {"Warning": "No books present in the database"}
            return all_books
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def add_book(self, book_id: int, book: Book, db: Session):
        try:
            if list(sql_book_object.find_by_id(book_id, db)) != []:
                logger.warning({"Warning:": "book already exist"})
                return {"Warning:": "book already exist"}
            return sql_book_object.add_book(book, db)
        except Exception as e:
            logger.error({"error": str(e.args)})
            return {"error": str(e.args)}

    def update_book(self, book_id: int, book: Book, db: Session):
        try:
            if sql_book_object.find_by_id(book_id, db) == []:
                logger.warning({"Warning": "book does not exist"})
                return {"Warning": "book does not exist"}
            return sql_book_object.update_book(book_id, book, db)
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def delete_book(self, book_id: int, db: Session):
        try:
            if sql_book_object.find_by_id(book_id, db) == []:
                logger.warning({"Warning": "book does not exist"})
                return {"Warning": "book does not exist"}
            return sql_book_object.delete_book(book_id, db)
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}


sql_book_handler = Book_handler()
