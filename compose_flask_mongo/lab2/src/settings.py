import os


MONGO_DB_USERNAME=os.getenv('MONGO_DB_USERNAME')
MONGO_DB_PASSWOR=os.getenv('MONGO_DB_PASSWOR')
MONGO_DB_NAME=os.getenv('MONGO_CONTAINER_NAME')
MONGO_DB_INSTANCE_URL=f"mongodb://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWOR}@localhost:27017"

ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)