import unittest
from services.kitchen_observer import KitchenObserver
from services.kitchen_notifier import KitchenNotifier
from models.order import Order
from models.client import Client
from models.dish import Dish
from mock import MagicMock, patch


class TestObserverPattern(unittest.TestCase):
    def setUp(self):
        self.observer = KitchenObserver()
        self.mock_notifier1 = MagicMock()
        self.mock_notifier2 = MagicMock()
        self.observer.attach(self.mock_notifier1)
        self.observer.attach(self.mock_notifier2)

        self.client = Client("Test Client")
        self.dish = Dish("Test Dish", 100)
        self.order = Order(client=self.client, dishes=[self.dish], notifier=None)

    def test_observer_notifies_all_attached(self):
        self.observer.notify(self.order)
        self.mock_notifier1.notify.assert_called_once_with(self.order)
        self.mock_notifier2.notify.assert_called_once_with(self.order)

    def test_kitchen_notifier_output(self):
        notifier = KitchenNotifier()
        with patch('builtins.print') as mock_print:
            notifier.notify(self.order)
            mock_print.assert_called_once_with(
                "Сповіщення кухні: замовлення для Test Client на Test Dish"
            )

    def test_observer_with_invalid_order(self):
        with self.assertRaises(ValueError):
            self.observer.notify(None)