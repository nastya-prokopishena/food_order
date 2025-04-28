
class Client:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name

    def make_order(self, dishes, factory):
        if not dishes:
            raise ValueError("Dish list cannot be empty.")

        order = factory.create_order(self, dishes)
        return order
