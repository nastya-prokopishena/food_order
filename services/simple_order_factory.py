from interfaces.order_factory import OrderFactory
from interfaces.notifier import Notifier
from models.order import Order

class SimpleOrderFactory(OrderFactory):
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def create_order(self, client, dishes):
        if not client:
            raise ValueError("Клієнт не може бути None")
        if not dishes:
            raise ValueError("Список страв не може бути порожнім")

        order = Order(client=client, dishes=dishes, notifier=self.notifier)

        if self.notifier:
            self.notifier.notify(order)

        return order
