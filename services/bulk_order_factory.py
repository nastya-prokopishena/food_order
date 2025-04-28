from interfaces.order_factory import OrderFactory
from models.order import Order


class BulkOrderFactory(OrderFactory):
    def __init__(self, notifier=None, order_repository=None, discount: float = 0.1):
        if not 0 <= discount < 1:
            raise ValueError("Discount must be between 0 and 1")
        self.notifier = notifier
        self.order_repository = order_repository
        self.discount = discount

    def create_order(self, client, dishes):
        if not client:
            raise ValueError("Клієнт не може бути None")
        if not dishes or len(dishes) < 5:
            raise ValueError("Масове замовлення має містити щонайменше 5 страв")

        discounted_dishes = []
        for dish in dishes:
            discounted_dish = type(dish)(dish.name, dish.price * (1 - self.discount))
            discounted_dishes.append(discounted_dish)

        return Order(
            client=client,
            dishes=discounted_dishes,
            notifier=self.notifier,
            order_repository=self.order_repository
        )