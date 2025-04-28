
class Order:
    def __init__(self, client, dishes, notifier, order_repository=None):
        if not client:
            raise ValueError("Клієнт не може бути порожнім")
        if not dishes:
            raise ValueError("Список страв не може бути порожнім")
        self.client = client
        self.dishes = dishes
        self.notifier = notifier
        self.order_repository = order_repository
        self.order_id = None

    def place_order(self) -> None:
        if self.notifier:
            self.notifier.notify(self)

        if self.order_repository:
            self.order_id = self.order_repository.save_order(self)

    def get_total_price(self) -> float:
        return sum(dish.price for dish in self.dishes)
