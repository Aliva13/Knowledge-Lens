class APis:
    # create_api = '/create'
    view_all_items_item = '/view_all_items'
    create_item = '/items/create'
    update_item = '/items/{items_id}'
    delete_item = '/delete/{items_id}'
    send_item = '/send_email'
    get_item = '/billing-price'

class Aggregation:
    Agr= [
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
    ]
