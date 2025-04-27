import unittest
from models.client import Client
from models.dish import Dish
from services.simple_order_factory import SimpleOrderFactory
from services.kitchen_notifier import KitchenNotifier

class TestClient(unittest.TestCase):
    def test_client_name_update(self):
        client = Client("Анастасія")
        self.assertEqual(client.name, "Анастасія")

    def test_make_order(self):
        client = Client(name="Анастасія")
        dish = Dish(name="Піца Маргарита", price=210.0)
        notifier = KitchenNotifier()
        factory = SimpleOrderFactory(notifier=notifier)
        order = client.make_order([dish], factory)
        self.assertIsNotNone(order)
        self.assertEqual(order.client.name, "Анастасія")
        self.assertIn(dish, order.dishes)

    def test_client_empty_name(self):
        with self.assertRaises(ValueError):
            Client("")

    def test_make_order_empty_dishes(self):
        client = Client("Анастасія")
        factory = SimpleOrderFactory(notifier=None)
        with self.assertRaises(ValueError):
            client.make_order([], factory)
