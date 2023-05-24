from configparser import  ConfigParser
import sys
from scripts.logging.logger import logger


try:
    config = ConfigParser(interpolation=None)
    config.read("configuration/application.conf")
    SERVICE_HOST = config.get("SERVICE","HOST")
    SERVICE_PORT = config.get("SERVICE", "PORT")
except Exception as e:
    logger.info(f"Error while loading the config: {e}")
    logger.info("Failed to Load Configuration. Exiting!!!")
    sys.stdout.flush()
    sys.exit()

class DBConf:
    DB_URI = config.get("MONGO_DB", "DB_URI")
    if not DB_URI:
        logger.info("Error, environment variable DB_URI not set")
        sys.exit(1)

    DB_DATABASE = config.get("MONGO_DB", "DB_DATABASE")
    if not DB_DATABASE:
        logger.info("Error, environment variable DB_DATABASE not set")
        sys.exit(1)

    DB_COLLECTION = config.get("MONGO_DB", "DB_COLLECTION")
    if not DB_COLLECTION:
        logger.info("Error, environment variable DB_COLLECTION not set")
        sys.exit(1)