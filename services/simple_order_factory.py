from interfaces.order_factory import OrderFactory
from interfaces.notifier import Notifier


class SimpleOrderFactory(OrderFactory):
    def __init__(self, notifier: Notifier):
        pass

    def create_order(self, client, dishes):
        pass
