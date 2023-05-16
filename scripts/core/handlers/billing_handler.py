from scripts.constant.app_constant import DBConstants
from scripts.core.DB.MongoDB import read_item, update_item, delete_item, Item, \
    pipeline_aggregation
from scripts.utility.mongo_utility import MongoCollectionBaseClass, MongoConnect


class Item_handler:

    def __init__(self):
        self.user_mongo_obj = MongoCollectionBaseClass(database=DBConstants.DB_DATABASE,
                                                       mongo_client=MongoConnect(DBConstants.DB_URI).client,
                                                       collection=DBConstants.DB_COllECTION)

    def read_data(self):
        data = read_item()
        print(data)
        return data

    def create_data(self, item: Item):

        # ADD LOGIC to validate data
        # Re-order
        res = self.user_mongo_obj.insert_one(data=item.dict())
        # res= 'success'
        if res:
            return {"status": "success", "message": "Record Inserted"}
        else:
            return {"status": "failed", "message": "Error inserting", "error": ""}
        # return create_item(item)

    def update_data(self, item_id: int, item: Item):
        return update_item(item_id, item)

    def delete_data(self, item_id: int):
        return delete_item(item_id)

    def pipeline_aggregation(self):
        data = pipeline_aggregation([
            {
                '$addFields': {
                    'total_amount': {
                        '$multiply': [
                            '$quantity', '$cost'
                        ]
                    }
                }
            }, {
                '$group': {
                    '_id': None,
                    'total': {
                        '$sum': '$total_amount'
                    }
                }
            }, {
                '$project': {
                    '_id': 0
                }
            }
        ])
        print(data)
        return list(data)[0]['total']
