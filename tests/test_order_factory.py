import unittest
from mock.mock import MagicMock
from services.simple_order_factory import SimpleOrderFactory
from models.client import Client
from models.dish import Dish


class TestOrderFactory(unittest.TestCase):

    def test_create_order(self):
        factory = SimpleOrderFactory(notifier=None)
        client = Client(name="Анастасія")
        dish = Dish(name="Піца Маргарита", price=210.0)
        order = factory.create_order(client, [dish])
        self.assertEqual(order.client.name, "Анастасія")
        self.assertIn(dish, order.dishes)

    def test_create_order_empty_dishes(self):
        factory = SimpleOrderFactory(notifier=None)
        client = Client("Анастасія")
        with self.assertRaises(ValueError):
            factory.create_order(client, [])

    def test_create_order_no_client(self):
        factory = SimpleOrderFactory(notifier=None)
        dish = Dish("Піца Маргарита", 210.0)
        with self.assertRaises(ValueError):
            factory.create_order(None, [dish])

    def test_create_order_with_repository(self):
        mock_repo = MagicMock()
        factory = SimpleOrderFactory(notifier=None, order_repository=mock_repo)
        client = Client(name="Анастасія")
        dish = Dish(name="Піца Маргарита", price=210.0)
        order = factory.create_order(client, [dish])

        self.assertEqual(order.client.name, "Анастасія")
        self.assertIn(dish, order.dishes)
        self.assertEqual(order.order_repository, mock_repo)



