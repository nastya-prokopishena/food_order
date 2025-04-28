import unittest
from services.bulk_order_factory import BulkOrderFactory
from services.kitchen_notifier import KitchenNotifier
from mock.mock import MagicMock
from models.client import Client
from models.dish import Dish

class TestBulkOrderFactory(unittest.TestCase):
    def setUp(self):
        self.mock_notifier = MagicMock()
        self.mock_repo = MagicMock()
        self.client = Client("Володимир")
        self.dishes = [Dish(f"Dish {i}", 100) for i in range(1, 6)]

    def test_bulk_factory_creates_discounted_order(self):
        factory = BulkOrderFactory(notifier=self.mock_notifier, discount=0.1)
        order = factory.create_order(self.client, self.dishes)
        self.assertEqual(len(order.dishes), 5)
        self.assertAlmostEqual(order.dishes[0].price, 90.0)

    def test_bulk_factory_minimum_dishes(self):
        factory = BulkOrderFactory(notifier=self.mock_notifier)
        with self.assertRaises(ValueError):
            factory.create_order(self.client, self.dishes[:4])

    def test_bulk_factory_invalid_discount(self):
        with self.assertRaises(ValueError):
            BulkOrderFactory(notifier=self.mock_notifier, discount=1.5)
