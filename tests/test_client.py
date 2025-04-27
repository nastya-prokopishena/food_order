import unittest
from models.client import Client
from models.dish import Dish
from services.simple_order_factory import SimpleOrderFactory

class TestClient(unittest.TestCase):
    def test_client_name_update(self):
        client = Client("Анастасія")
        self.assertEqual(client.name, "Анастасія")

    def test_make_order(self):
        client = Client(name="Анастасія")
        dish = Dish(name="Піца Маргарита", price=210.0)
        factory = SimpleOrderFactory(notifier=None)
        order = client.make_order([dish], factory)
        self.assertIsNotNone(order)
        self.assertEqual(order.client.name, "Анастасія")
        self.assertIn(dish, order.dishes)