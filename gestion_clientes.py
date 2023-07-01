class Client:
    def __init__(self, name_lastname, type, id, email, shipping_address, phone_number):
        self.name_lastname = name_lastname
        self.type = type
        self.id = id
        self.email = email
        self.shipping_address = shipping_address
        self.phone_number = phone_number

    def show_attr(self):
        return f"Nombre y Apellido: {self.name_lastname}, Tipo de cliente: {self.type}, Cédula: {self.id}, Correo electrónico: {self.email}, Dirección de envío: {self.shipping_address}, Teléfono: {self.phone_number}"
    
    def convert_dicc(self):
        return {"name_lastname": self.name_lastname, "type": self.type, "id": self.id, "email": self.email, "shipping_address": self.shipping_address, "phone_number": self.phone_number}
    