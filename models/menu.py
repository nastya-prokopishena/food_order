from typing import List
from .dish import Dish


class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish: Dish) -> None:
        if not isinstance(dish, Dish):
            raise TypeError("Expected a Dish instance")
        self.dishes.append(dish)

    def get_dishes(self) -> List[Dish]:
        return self.dishes
