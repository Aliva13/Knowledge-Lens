from fastapi import FastAPI
from pymongo import MongoClient
from scripts.constant.app_configuration import DBConf
from scripts.logging.logger import logger
from scripts.exceptions.exceptions_code import *

app = FastAPI()

client = MongoClient(DBConf.DB_URI)
db = client[DBConf.DB_DATABASE]
grocery = db[DBConf.DB_COLLECTION]

def pipeline_aggregation(pipeline: list):
    try:
        logger.info("MongoDB:pipeline_aggregation")
    except Exception as e:
        logger.error(Mongo_DBExceptions.EX013.format(error=str(e)))
    return grocery.aggregate(pipeline)

