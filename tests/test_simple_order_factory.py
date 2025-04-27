import unittest
from services.simple_order_factory import SimpleOrderFactory
from services.kitchen_notifier import KitchenNotifier


class TestOrderFactory(unittest.TestCase):
    def test_factory_init(self):
        notifier = KitchenNotifier()
        factory = SimpleOrderFactory(notifier=notifier)
        self.assertEqual(factory.notifier, notifier)
