from fastapi import APIRouter
from scripts.constant.app_constant import APis
from scripts.core.schema.model import Item
from scripts.core.handlers.billing_handler import Item_handler
from scripts.core.handlers.email_handler import send_email, Email
from scripts.exceptions.exceptions_code import Billing_ServicesException
from scripts.logging.logger import logger
from json2html import *

item_router = APIRouter(tags=['abc'])


@item_router.get(APis.view_all_items_item)
def view_all_items():
    try:
        logger.info("Services:view_All_items")
        item_object = Item_handler()
        return item_object.read_data()
    except Exception as e:
        logger.error(Billing_ServicesException.EX007.format(error=str(e)))
        return {'status': 'failed'}


@item_router.post(APis.create_item)
def create_item(item: Item):
    try:
        logger.info("Services:create_item")
        item_object = Item_handler()
        return item_object.create_data(item)
    except Exception as e:
        logger.error(Billing_ServicesException.EX008.format(error=str(e)))


@item_router.put(APis.update_item)
def update_item(item_id: int, item: Item):
    try:
        logger.info("Services:update_item")
        item_object = Item_handler()
        return item_object.update_data(item_id, item)
    except  Exception as e:
        logger.error(Billing_ServicesException.EX009.format(error=str(e)))
        return {'status': 'failed'}


@item_router.delete(APis.delete_item)
def delete_item(item_id: int):
    try:
        logger.info("Services:delete_item")
        item_object = Item_handler()
        return item_object.delete_data(item_id)
    except Exception as e:
        logger.error(Billing_ServicesException.EX010.format(error=str(e)))
        return {'status': 'failed'}


@item_router.post(APis.send_item)
def send_item(email: Email):
    """Function to send item"""
    try:
        item_object = Item_handler()
        all_billing_list_json = item_object.read_data()
        table = json2html.convert(json=all_billing_list_json)
        logger.info("services:send_item")
        item_handler = Item_handler()
        result = item_handler.pipeline_aggregation
        message = f"The Table is below: {table}"
        message1 = f"{message} \n total amount is {result}"
        send_email(message1, email)
        logger.info("send_item: Email Sent")
        return {"message": "email sent"}
    except Exception as e:
        logger.error(Billing_ServicesException.EX011.format(error=str(e)))
        return {"message": "failed"}


@item_router.get(APis.get_item)
def get_grocery():
    try:
        logger.info("Services:get_grocery")
        itemhandler = Item_handler()
        return itemhandler.pipeline_aggregation
    except Exception as e:
        logger.error(Billing_ServicesException.EX012.format(error=str(e)))
        return {'status': 'failed'}
