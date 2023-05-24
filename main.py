"""importing uvicorn """
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from scripts.core.services.billing_service import item_router
from scripts.logging.logger import logger
from scripts.constant.app_configuration import *
app = FastAPI()
load_dotenv()
app.include_router(item_router)

if __name__ == "__main__":
    logger.info("main: main file started")
    uvicorn.run(host=SERVICE_HOST,app="main:app", port=int(SERVICE_PORT), reload=True)
