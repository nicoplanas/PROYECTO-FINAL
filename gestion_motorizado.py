class Motorizado:
    def __init__(self, name, phone_number, id, license_plate):
        self.name = name
        self.phone_number = phone_number
        self.id = id
        self.license_plate = license_plate

    def show_attr(self):
        return f"Nombre: {self.name}, Número de teléfono: {self.phone_number}, Cédula: {self.id}, Placa: {self.license_plate}"
    
    def convert_dicc(self):
        return {"name": self.name, "phone_number": self.phone_number, "id": self.id, "license_plate": self.license_plate}
    
    def show_name(self):
        return f"{self.name}"