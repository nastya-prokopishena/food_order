from pymongo import MongoClient
from pymongo.database import Database


class MongoDB:
    _instances = {}

    def __new__(cls, uri: str, db_name: str):
        key = (uri, db_name)
        if key not in cls._instances:
            instance = super().__new__(cls)
            instance.client = MongoClient(uri)
            instance.db = instance.client[db_name]
            cls._instances[key] = instance
        return cls._instances[key]

    def get_db(self) -> Database:
        return self.db

    def close(self):
        for key, instance in list(self._instances.items()):
            instance.client.close()
            del self._instances[key]