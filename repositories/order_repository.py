from typing import List
from datetime import datetime
from bson import ObjectId


class OrderRepository:
    def __init__(self, db):
        self.collection = db['orders']

    def save_order(self, order) -> str:
        order_data = {
            'client_name': order.client.name,
            'dishes': [{'name': dish.name, 'price': dish.price} for dish in order.dishes],
            'total_price': order.get_total_price(),
            'created_at': datetime.utcnow(),
            'status': 'pending'
        }
        result = self.collection.insert_one(order_data)
        return str(result.inserted_id)

    def get_orders(self, limit: int = 10) -> List[dict]:
        orders = self.collection.find().sort('created_at', -1).limit(limit)
        return list(orders)

    def update_order_status(self, order_id: str, status: str) -> bool:
        if not ObjectId.is_valid(order_id):
            return False
        result = self.collection.update_one(
            {'_id': ObjectId(order_id)},
            {'$set': {'status': status}}
        )
        return result.modified_count > 0