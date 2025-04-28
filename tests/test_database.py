import unittest
from services.database import MongoDB
from config import Config


class TestDatabase(unittest.TestCase):
    def test_database_instance(self):
        db1 = MongoDB(Config.MONGO_URI, Config.DB_NAME)
        db2 = MongoDB(Config.MONGO_URI, Config.DB_NAME)
        self.assertIs(db1, db2)
        db1.close()

    def test_different_parameters(self):
        db1 = MongoDB("mongodb://localhost:27017/", "test_db1")
        db2 = MongoDB("mongodb://localhost:27017/", "test_db2")
        self.assertIsNot(db1, db2)
        db1.close()
        db2.close()