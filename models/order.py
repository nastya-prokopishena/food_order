from typing import List
from .dish import Dish
from .client import Client
from interfaces.notifier import Notifier


class Order:
    def __init__(self, client, dishes, notifier):
        pass

    def place_order(self) -> None:
        pass

    def get_total_price(self) -> float:
        pass