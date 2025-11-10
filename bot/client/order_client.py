from .base_client import BaseClient

class OrderClient(BaseClient):
    """Cliente para os endpoints de OrderController"""

    def create_order(self, order: dict):
        """POST /orders"""
        return self.post("/orders", json=order)

    def get_all_orders(self):
        """GET /orders"""
        return self.get("/orders")

    def get_order_by_id(self, order_id: int):
        """GET /orders/{id}"""
        return self.get(f"/orders/{order_id}")

    def update_order(self, order: dict):
        """PUT /orders"""
        return self.put("/orders", json=order)

    def delete_order(self, order_id: int):
        """DELETE /orders/{id}"""
        return self.delete(f"/orders/{order_id}")
