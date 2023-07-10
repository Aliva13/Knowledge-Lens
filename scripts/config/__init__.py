from configparser import ConfigParser

config = ConfigParser()
config.read("config/application.conf")


class Service:
    port = config["SERVICE"]["port"]
    host = config["SERVICE"]["host"]
    uri = config["POSTGREE_SQL"]["uri"]
    database_name = config["POSTGREE_SQL"]["database_name"]
    collection_name = config["POSTGREE_SQL"]["collection_name"]
    root_logger_level =config["LOGGER_LEVEL"][" root_logger_level"] 
    file_handler_logger_level=config["LOGGER_LEVEL"]["file_handler_logger_level=config"]
    console_handler_logger_level=config["LOGGER_LEVEL"]["console_handler_logger_level"]

service_object=Service()