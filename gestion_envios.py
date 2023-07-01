class Shipping:
    def __init__(self, purchase_order, client_name, client_phone, date, shipping_address, shipping_service, motorizado, service_cost):
        self.purchase_order = purchase_order
        self.client_name = client_name
        self.client_phone = client_phone
        self.date = date
        self.shipping_address = shipping_address
        self.shipping_service = shipping_service
        self.motorizado = motorizado
        self.service_cost = service_cost

    def convert_dicc(self):
        return {"purchase_order": self.purchase_order, "client_name": self.client_name, "client_phone": self.client_phone, "date": self.date, "shipping_address": self.shipping_address, "shipping_service": self.shipping_service, "motorizado": self.motorizado, "service_cost": self.service_cost}