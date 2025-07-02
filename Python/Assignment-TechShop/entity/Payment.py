class Payment:
    def __init__(self, payment_id, order_id, amount, status="Pending"):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.status = status
