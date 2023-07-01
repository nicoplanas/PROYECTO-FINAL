class Sale:
    def __init__(self, buyer, date, purchased_products, amount_product, payment_method, shipping_service, total_breakdown):
        self.buyer = buyer
        self.date = date
        self.purchased_products = purchased_products
        self.amount_product = amount_product
        self.payment_method = payment_method
        self.shipping_service = shipping_service
        self.total_breakdown = total_breakdown

    def show_attr(self):
        return f"Cliente: {self.buyer}, Fecha: {self.date}, Producto: {self.purchased_products}, Cantidad: {self.amount_product}, Método de pago: {self.payment_method}, Método de envío: {self.shipping_service}, Desglose del total de compra: {self.total_breakdown}"
    
    def convert_dicc(self):
        return {"buyer": self.buyer, "date": self.date, "purchased_products": self.purchased_products, "amount_product": self.amount_product, "payment_method": self.payment_method, "shipping_service": self.shipping_service, "total_breakdown": self.total_breakdown}