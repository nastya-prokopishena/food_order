import unittest
from models.dish import Dish
from models.client import Client
from services.kitchen_notifier import KitchenNotifier
from models.order import Order


class TestOrder(unittest.TestCase):

    def test_create_order(self):
        client = Client(name="Валерія")
        dish = Dish(name="Піца 4 сири", price=290.0)
        order = Order(dishes=[dish], client=client, notifier=None)
        self.assertEqual(len(order.dishes), 1)
        self.assertEqual(order.client.name, "Валерія")

    def test_order_total_price(self):
        client = Client(name="Анастасія")
        dish1 = Dish(name="Піца Маргарита", price=210.0)
        dish2 = Dish(name="Шоколаний фондан", price=280.0)
        order = Order(dishes=[dish1, dish2], client=client, notifier=None)
        self.assertEqual(order.get_total_price(), 490.0)
