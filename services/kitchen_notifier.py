from interfaces.notifier import Notifier


class KitchenNotifier(Notifier):
    def notify(self, order):
        if order is None:
            raise ValueError("Order cannot be None")

        print(
            f"Сповіщення кухні: замовлення для {order.client.name} на {', '.join(dish.name for dish in order.dishes)}")
        return None
