import unittest

from mock.mock import MagicMock

from models.dish import Dish
from models.client import Client
from services.kitchen_notifier import KitchenNotifier
from models.order import Order
from mock import Mock


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.notifier = Mock(spec=KitchenNotifier)

    def test_place_order(self):
        notifier = Mock(spec=KitchenNotifier)
        client = Client(name="Валерія")
        dish = Dish(name="Піца 4 сири", price=290.0)
        order = Order(dishes=[dish], client=client, notifier=notifier)
        order.place_order()
        notifier.notify.assert_called_once_with(order)

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

    def test_create_order_empty_dishes(self):
        client = Client("Валерія")
        with self.assertRaises(ValueError):
            Order(dishes=[], client=client, notifier=None)

    def test_create_order_no_client(self):
        dish = Dish("Піца 4 сири", 290.0)
        with self.assertRaises(ValueError):
            Order(dishes=[dish], client=None, notifier=None)

    def test_place_order_with_repository(self):
        client = Client(name="Валерія")
        dish = Dish(name="Піца 4 сири", price=290.0)
        order = Order(
            dishes=[dish],
            client=client,
            notifier=self.notifier,
            order_repository=self.mock_repo
        )
        order.place_order()
        self.notifier.notify.assert_called_once_with(order)
        self.mock_repo.save_order.assert_called_once_with(order)

    def test_order_without_repository(self):
        client = Client(name="Валерія")
        dish = Dish(name="Піца 4 сири", price=290.0)
        order = Order(dishes=[dish], client=client, notifier=None)
        order.place_order()