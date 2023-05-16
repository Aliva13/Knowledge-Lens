class APis:
    # create_api = '/create'
    view_all_items_api = '/view_all_items'
    create_api = '/items/create'
    update_api = '/items/{items_id}'
    delete_api = '/delete/{items_id}'
    send_api = '/send_email'
    get_api = '/billing-price'


class DBConstants:
    # user_db_name = 'Aliva'
    # user_collection_name = 'users'
    # grocery_details_collection_name = 'grocery'
    DB_URI = 'mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23'
    DB_DATABASE = 'interns_b2_23'
    DB_COllECTION = 'Aliva_GROCERY'
