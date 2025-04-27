class Dish:
    def __init__(self, name: str, price: float):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f"{self.name}: ₴{self.price:.2f}"