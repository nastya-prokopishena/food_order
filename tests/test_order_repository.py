import unittest
from models.dish import Dish
from models.client import Client
from models.order import Order
from repositories.order_repository import OrderRepository
from mock import MagicMock
from bson import ObjectId


class TestOrderRepository(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_collection = MagicMock()
        self.mock_db.__getitem__.return_value = self.mock_collection
        self.repo = OrderRepository(self.mock_db)

    def test_save_order(self):
        client = Client("Анастасія")
        dish = Dish("Піца Маргарита", 210.0)
        order = Order(client=client, dishes=[dish], notifier=None)

        self.mock_collection.insert_one.return_value.inserted_id = ObjectId()
        order_id = self.repo.save_order(order)

        self.assertIsInstance(order_id, str)
        self.mock_collection.insert_one.assert_called_once()

    def test_get_orders(self):
        mock_cursor = [
            {"_id": ObjectId(), "client_name": "Test", "dishes": []}
        ]
        self.mock_collection.find.return_value.sort.return_value.limit.return_value = mock_cursor
        orders = self.repo.get_orders()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["client_name"], "Test")