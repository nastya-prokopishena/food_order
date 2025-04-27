from typing import List
from .dish import Dish
from interfaces.order_factory import OrderFactory


class Client:
    def __init__(self, name: str):
        pass
    def make_order(self, dishes: List[Dish], factory: OrderFactory):
        pass