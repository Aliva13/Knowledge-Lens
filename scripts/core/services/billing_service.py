from fastapi import APIRouter
from scripts.constant.app_constant import APis
from scripts.core.DB.MongoDB import Item
from scripts.core.handlers.billing_handler import Item_handler
from scripts.core.handlers.email_handler import send_email, Email

item_router = APIRouter(tags=['abc'])


@item_router.get(APis.view_all_items_api)
def view_all_items():
    try:
        item_object = Item_handler()
        return item_object.read_data()
    except Exception as e:
        print(e)
        return {'status': 'failed'}


@item_router.post(APis.create_api)
def create_item(item: Item):

    item_object = Item_handler()

    return item_object.create_data(item)


@item_router.put(APis.update_api)
def update_item(item_id: int, item: Item):
    item_object = Item_handler()
    return item_object.update_data(item_id, item)


@item_router.delete(APis.delete_api)
def delete_item(item_id: int):
    item_object = Item_handler()
    return item_object.delete_data(item_id)


@item_router.post(APis.send_api)
def send_item(email: Email):
    itemhandler = Item_handler()
    result = itemhandler.pipeline_aggregation()
    message = f"total amount is {result}"
    send_email(message, email)
    return {"message": "email sent"}


@item_router.get(APis.get_api)
def get_grocery():
    itemhandler = Item_handler()
    return itemhandler.pipeline_aggregation()
