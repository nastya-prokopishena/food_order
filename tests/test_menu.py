import unittest
from models.dish import Dish
from models.menu import Menu


class TestMenu(unittest.TestCase):

    def test_add_dish_to_menu(self):
        menu = Menu()
        dish = Dish("Паста Карбонара", 250.0)
        menu.add_dish(dish)
        self.assertEqual(len(menu.dishes), 1)
        self.assertIn(dish, menu.dishes)

    def test_get_dishes(self):
        menu = Menu()
        dish1 = Dish("Піца Пепероні", 310.0)
        dish2 = Dish("Шоколадний фондан", 280.0)
        menu.add_dish(dish1)
        menu.add_dish(dish2)
        dishes = menu.get_dishes()
        self.assertEqual(len(dishes), 2)
        self.assertIn(dish1, dishes)
        self.assertIn(dish2, dishes)