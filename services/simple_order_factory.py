from interfaces.order_factory import OrderFactory
from models.order import Order


class SimpleOrderFactory(OrderFactory):
    def __init__(self, notifier, order_repository=None):
        self.notifier = notifier
        self.order_repository = order_repository

    def create_order(self, client, dishes):
        if not client:
            raise ValueError("Клієнт не може бути None")
        if not dishes:
            raise ValueError("Список страв не може бути порожнім")

        order = Order(
            client=client,
            dishes=dishes,
            notifier=self.notifier,
            order_repository=self.order_repository
        )

        if self.notifier:
            self.notifier.notify(order)

        return order
