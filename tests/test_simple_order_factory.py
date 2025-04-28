import unittest
from services.simple_order_factory import SimpleOrderFactory
from services.kitchen_notifier import KitchenNotifier
from mock.mock import MagicMock
from models.client import Client
from models.dish import Dish


class TestSimpleOrderFactory(unittest.TestCase):
    def test_factory_init(self):
        notifier = KitchenNotifier()
        factory = SimpleOrderFactory(notifier=notifier)
        self.assertEqual(factory.notifier, notifier)

    def setUp(self):
        self.mock_notifier = MagicMock()
        self.mock_repo = MagicMock()
        self.client = Client("Володимир")
        self.dishes = [Dish(f"Dish {i}", 100) for i in range(1, 6)]

    def test_simple_factory_creates_order(self):
        factory = SimpleOrderFactory(notifier=self.mock_notifier, order_repository=self.mock_repo)
        order = factory.create_order(self.client, self.dishes[:1])
        self.assertEqual(order.client.name, "Володимир")
        self.assertEqual(len(order.dishes), 1)

    def test_simple_factory_empty_dishes(self):
        factory = SimpleOrderFactory(notifier=self.mock_notifier)
        with self.assertRaises(ValueError):
            factory.create_order(self.client, [])
