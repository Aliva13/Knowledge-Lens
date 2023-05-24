class Billing_HandlerException:
    EX001 = "Exception in read_data:{error}"
    EX002 = "Exception in create_data:{error}"
    EX003 = "Exception in update_data:{error}"
    EX004 = "Exception in delete_data:{error}"
    EX005 = "Exception in pipeline_aggregation:{error}"

class Email_HandlerException:
    EX006 = "Exception in send_email:{error}"

class Billing_ServicesException:
    EX007 = "Exception in view_All_items:{error}"
    EX008 = "Exception in create_item:{error}"
    EX009 = "Exception in update_item:{error}"
    EX010 = "Exception in delete_item:{error}"
    EX011 = "Exception in send_item:{error}"
    EX012 = "Exception in get_grocery:{error}"

class Mongo_DBExceptions:
    EX013 = "Exception in pipeline_aggregation:{error}"