import unittest
from mock.mock import MagicMock
from interfaces.notifier import Notifier
from services.kitchen_notifier import KitchenNotifier
from models.order import Order
from models.dish import Dish
from models.client import Client


class TestNotifier(unittest.TestCase):

    def test_notify(self):
        notifier = KitchenNotifier()
        notifier.notify = MagicMock()
        client = Client(name="Анастасія")
        dish = Dish(name="Піца Маргарита", price=210.0)
        order = Order(dishes=[dish], client=client, notifier=notifier)
        notifier.notify(order)
        notifier.notify.assert_called_once_with(order)
        self.assertIsNone(notifier.notify.return_value)

    def test_notify_invalid_order(self):
        notifier = KitchenNotifier()
        with self.assertRaises(ValueError):
            notifier.notify(None)