class Order:
    def __init__(self, order_id, customer_id, order_date, status="Pending"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status
