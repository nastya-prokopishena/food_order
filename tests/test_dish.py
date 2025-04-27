import unittest
from models.dish import Dish


class TestDish(unittest.TestCase):
    def test_dish_creation(self):
        dish = Dish("Піца Маргарита", 210.0)
        self.assertEqual(dish.name, "Піца Маргарита")
        self.assertEqual(dish.price, 210.0)

    def test_dish_get_info(self):
        dish = Dish("Салат Цезар з куркою", 220.0)
        self.assertEqual(dish.get_info(), "Салат Цезар з куркою: ₴220.00")

    def test_dish_negative_price(self):
        with self.assertRaises(ValueError):
            Dish("Піца Маргарита", -10.0)

    def test_dish_empty_name(self):
        with self.assertRaises(ValueError):
            Dish("", 210.0)