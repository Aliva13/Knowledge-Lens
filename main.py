from fastapi import FastAPI
from scripts.services.book_services import book_router
from scripts.logging.logs import logger

app = FastAPI()
book_data = {}

try:
    app.include_router(book_router)
except :
    logger.error({"Error:":"Unexpected scenario happened with the router"})    


