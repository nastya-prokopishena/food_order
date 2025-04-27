from interfaces.notifier import Notifier
from models.order import Order


class KitchenNotifier(Notifier):
    def notify(self, order: Order):
        if order is None:
            raise ValueError("Order cannot be None")

        print(
            f"Сповіщення кухні: замовлення для {order.client.name} на {', '.join(dish.name for dish in order.dishes)}")
        return None
