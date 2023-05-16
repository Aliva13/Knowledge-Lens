from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from scripts.constant.app_constant import DBConstants

app = FastAPI()

# Creating instance of mongo client
client = MongoClient(DBConstants.DB_URI)
db = client[DBConstants.DB_DATABASE]
# # Creating document
grocery = db[DBConstants.DB_COllECTION]


class Item(BaseModel):
    id: int
    name: str
    quantity: int
    cost: int


def read_item():
    data = []
    print(grocery.find())
    for items in grocery.find():
        del items['_id']
        data.append(items)

    return {
        "db": data
    }


def create_item(item: Item):
    grocery.insert_one(item.dict())
    return {
        "message": "Item added successfully"
    }


def update_item(item_id: int, item: Item):
    try:
        grocery.update_one({"id": item_id}, {"$set": item.dict()})
        return {"message": "Item updated successfully"}
    except Exception as es:
        print("Exception while updating the record", es)
        return {"message": "failed to update"}


def delete_item(item_id: int):
    grocery.delete_one({"id": item_id})
    return {"message": "deleted successfully"}


def pipeline_aggregation(pipeline: list):
    return grocery.aggregate(pipeline)
