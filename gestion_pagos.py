class Payment:
    def __init__(self, client, amount, currency, payment_method, payment_date):
        self.client = client
        self.amount = amount
        self.currency = currency
        self.payment_method = payment_method
        self.payment_date = payment_date

    def convert_dicc(self):
        return {"client": self.client, "amount": self.amount, "currency": self.currency, "payment_method": self.payment_method, "payment_date": self.payment_date}