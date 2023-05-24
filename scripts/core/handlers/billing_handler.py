from scripts.core.DB.MongoDB import  \
    pipeline_aggregation
from scripts.utility.mongo_utility import MongoCollectionBaseClass, MongoConnect
from scripts.constant.app_configuration import DBConf
from scripts.logging.logger import logger
from scripts.exceptions.exceptions_code import *
from scripts.constant.app_constant import Aggregation
from scripts.core.schema.model import Item

class Item_handler:

    def __init__(self):
        self.user_mongo_obj = MongoCollectionBaseClass(database=DBConf.DB_DATABASE,
                                                       mongo_client=MongoConnect(DBConf.DB_URI).client,
                                                       collection=DBConf.DB_COLLECTION)

    def read_data(self):
        try:
            logger.info("Handler:read_data")
            if result := self.user_mongo_obj.find({}):
                logger.info("read_data:Record Found")
                return list(result)
        except Exception as e:
            logger.error(Billing_HandlerException.EX001.format(error=str(e)))
            return {"message":"failed"}

    def create_data(self, item: Item):
        try:
            logger.info("Handler:create_data")
            if result := self.user_mongo_obj.insert_one(data=item.dict()):
                logger.info("create_data:record created successfully")
                return {"message": "success"}
        except Exception  as e:
            logger.error(Billing_HandlerException.EX002.format(error=str(e)))
            return {"message":"failed"}


    def update_data(self, item_id: int, item: Item):
        try:
            logger.info("Handler:update_data")
            if result :=self.user_mongo_obj.update_one({'id':item_id},item.dict()):
                logger.info("update_data:record updated successfully")
                return {"message":"success"}
        except Exception as e:
            logger.error(Billing_HandlerException.EX003.format(error=str(e)))
            return {"message":"failed"}

    def delete_data(self, item_id: int):
        try:
            logger.info("Handler:delete_data")
            if result := self.user_mongo_obj.delete_one({'id': item_id}):
                logger.info("delete_data:record deleted successfully")
                return {"message": "success"}
        except Exception as e:
            logger.error(Billing_HandlerException.EX004.format(error=str(e)))
            return {"message": "failed"}

    def pipeline_aggregation(self):
        global data
        try:
            logger.info("Handler:pipeline_aggregation")
            data = pipeline_aggregation(Aggregation.Agr)
            logger.info("pipeline_aggregation:",data)
        except Exception as e:
            logger.error(Billing_HandlerException.EX005.format(error=str(e)))
        return list(data)[0]['total']
