class Product:

    def __init__(self, name, description, price, category, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.quantity = quantity
    
    def show_attr(self):
        return f"Nombre: {self.name}, Descripción: {self.description}, Precio: {self.price}, Categoría: {self.category}, quantity: {self.quantity}"
    
    def convert_dicc(self):
        return {"name": self.name, "description": self.description, "price": self.price, "category": self.category, "quantity": self.quantity}