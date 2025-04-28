from interfaces.notifier import Notifier
from models.order import Order


class KitchenObserver(Notifier):
    def __init__(self):
        self.observers = []

    def attach(self, observer: Notifier):
        self.observers.append(observer)

    def notify(self, order: Order):
        if order is None:
            raise ValueError("Order cannot be None")

        for observer in self.observers:
            observer.notify(order)