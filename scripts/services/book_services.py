from fastapi import APIRouter
from scripts.api import EndPoints
from scripts.logging.logs import logger
from scripts.core.handler.book_handler import sql_book_object
from sqlalchemy.orm import Session
from scripts.utils.sql_utility import Base
from scripts.schemas.sql_schemas import Book
from fastapi import Depends
from scripts.utils.sql_utility import SessionLocal, engine

try:
    book_router = APIRouter()
    logger.info({"Message": "succesfully established the api router"})
except Exception as e:
    logger.error({"Error": str(e)})

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@book_router.get(EndPoints.getting_books)
def fetch(db: Session = Depends(get_db)):
    try:
        get_books = sql_book_object.fetch(db)
        return get_books
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@book_router.post(EndPoints.adding_book)
def adding_book(book_id: int,book: Book, db: Session = Depends(get_db)):
    try:
        return sql_book_object.add_book(book.book_id, book, db)

    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@book_router.put(EndPoints.updating_book)
def updating_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    try:
        updated_values = book.dict(exclude_unset=True)
        up_book = sql_book_object.update_book(book_id, updated_values, db)
        return up_book
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@book_router.delete(EndPoints.deleting_book)
def deleting_book(book_id: int, db: Session = Depends(get_db)):
    try:

        del_book = sql_book_object.delete_book(book_id, db)
        return del_book
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}
