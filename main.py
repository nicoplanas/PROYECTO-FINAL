import requests
import json

def obtener_info_apis():
    response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json').text
    info_apis = json.loads(response)
    return info_apis

from gestion_productos import *
from gestion_ventas import *
from gestion_clientes import *
from gestion_pagos import *
from gestion_envios import *
from gestion_motorizado import *

productos = []

for product in obtener_info_apis():
    productos.append(product)

ventas = [{"buyer": "Willy Wonka", "date": "04/05/2023", "purchased_products": "Meat", "amount_product": 30, "payment_method": "Zelle", "shipping_service": "Zoom", "total_breakdown": 435},
          {"buyer": "Jose Linares", "date": "12/09/2023", "purchased_products": "Cereal", "amount_product": 2, "payment_method": "PM", "shipping_service": "MRW", "total_breakdown": 12},
          {"buyer": "Jimmy Neutron", "date": "07/07/2023", "purchased_products": "Crabs", "amount_product": 15, "payment_method": "Cash", "shipping_service": "Delivery", "total_breakdown": 50}]

clientes = [{"name_lastname": "Jose Linares", "type": "Natural", "id": "28411077", "email": "joseli@gmail.com", "shipping_address": "EL Hatillo", "phone_number": "04123348590"},
            {"name_lastname": "Jimmy Neutron", "type": "Natural", "id": "28410065", "email": "planasnico@gmail.com", "shipping_address": "Altamira", "phone_number": "04123348577"},
            {"name_lastname": "Willy Wonka", "type": "Jurídico", "id": "22414565", "email": "willydi@gmail.com", "shipping_address": "Chacao", "phone_number": "04243348590"}]

pagos = [{"client": "Jose Linares", "amount": 2, "currency": "USD (Dólares Americanos)", "payment_method": "Zelle", "payment_date": "02/04/2023"},
         {"client": "Willy Wonka", "amount": 30, "currency": "BS (Bolívares)", "payment_method": "Cash", "payment_date": "27/1/2023"},
         {"client": "Jimmy Neutron", "amount": 15, "currency": "USD (Dólares Americanos)", "payment_method": "Zelle", "payment_date": "04/07/2023"}]

envios = [{"purchase_order": "1", "client_name": "Jimmy Neutron", "client_phone": "04123348577", "date": "04/07/2023", "shipping_address": "Altamira", "shipping_service": "Delivery", "motorizado": "Mateo", "service_cost": 12},
          {"purchase_order": "2", "client_name": "Willy Wonka", "client_phone": "04243348590", "date": "27/01/2023", "shipping_address": "Chacao", "shipping_service": "MRW", "motorizado": "Ninguno", "service_cost": 10},
          {"purchase_order": "3", "client_name": "Jimmy Neutron", "client_phone": "04123347395", "date": "04/07/2023", "shipping_address": "Altamira", "shipping_service": "Delivery", "motorizado": "Edwin", "service_cost": 10}]

motorizados = []

#GESTIÓN DE PRODUCTOS

def add_product(obtener_info_apis):
    '''Toma cinco parametros
       Crea una clase
       Convierte la clase en un diccionario
       Agrega la clase a un API
       Imprime la clase creada.
    '''

    global producto

    print("""Para agregar un producto nuevo coloque la siguiente información:
            """)
        
    name = input("Nombre: ")

    description = input("Descripción: ")

    price = input("Precio: ")
    while not price.isnumeric() or int(price) < 1:
        price = input("Error! Ingrese un precio válido: ")
    price = int(price)

    category = input("Ingrese una categoría: ").capitalize()
    while not category.isalpha() or " " in category:
        category = input("Error! Ingrese una categoría válida: ").capitalize()

    quantity = input("Inventario disponible: ")
    while not quantity.isnumeric() or int(quantity) < 0:
        quantity = input("Error! Ingrese un número inventario válido: ")
    quantity = int(quantity)

    producto = Product(name, description, price, category, quantity).convert_dicc()

    productos.append(producto)

    completed = input("""El producto ha sido registrado exitosamente:
    
1. Mostrar producto agregado.
2. Salir.

>> """)

    if completed == "1":
        print(f"""
Nombre del producto: {producto["name"]}
Descripción: {producto["description"]}
Precio: ${producto["price"]}
Categoría: {producto["category"]}
Inventario: {producto["quantity"]}""")
    else:
        exit()

def search_product(obtener_info_apis):
    '''Recibe un input
       Busca el input como un valor en una lista de diccionarios
       Inprime los productos cuyo valor coincide con el input.
    '''

    filter = input("""Para buscar el producto seleccione alguno de lo siguientes filtros de búsqueda:

1. Categoría.
2. Precio.
3. Nombre.
4. Disponibilidad en inventario.

>> """)

    while not filter.isnumeric() or int(filter) not in range (1,5):
        filter = input("""Error! Seleccione una opción válida:

1. Categoría.
2. Precio.
3. Nombre.
4. Disponibilidad en inventario.

>> """)
    
    if filter == "1":
        found = 0
        category = input("Ingrese una categoría: ").capitalize()
        while not category.isalpha() or " " in category:
            category = input("Error! Ingrese una categoría válida: ").capitalize()

        for product in productos:
            if product["category"] == category:
                found += 1
                print(f"""
Nombre: {product["name"]}
Descripción: {product["description"]}
Precio: ${product["price"]}
Categoría: {product["category"]}
Disponibilidad: {product["quantity"]}""")
        if found == 0:
            print("No se ha encontrado ningún producto con esta categoría.")
    
    elif filter == "2":
        found = 0
        price = input("Ingrese un precio: ")
        while not price.isnumeric() or int(price) < 1:
            price = input("Error! Ingrese un precio válido: ")
        price = int(price)

        for product in productos:
            if product["price"] == price:
                found += 1
                print(f"""
Nombre: {product["name"]}
Descripción: {product["description"]}
Precio: ${product["price"]}
Categoría: {product["category"]}
Disponibilidad: {product["quantity"]}""")
        if found == 0:
            print("No se ha encontrado ningún producto con este precio.")

    elif filter == "3":
        found = 0
        name = input("Ingrese un nombre: ")

        for product in productos:
            if product["name"] == name:
                found += 1
                print(f"""
Nombre: {product["name"]}
Descripción: {product["description"]}
Precio: ${product["price"]}
Categoría: {product["category"]}
Disponibilidad: {product["quantity"]}""")
        if found == 0:
            print("No se ha encontrado ningún producto con este nombre.")

    elif filter == "4":
        found = 0
        quantity = input("Inventario disponible: ")
        while not quantity.isnumeric() or int(quantity) < 0:
            quantity = input("Error! Ingrese un número inventario válido: ")
        quantity = int(quantity)

        for product in productos:
            if product["quantity"] == quantity:
                found += 1
                print(f"""
Nombre: {product["name"]}
Descripción: {product["description"]}
Precio: ${product["price"]}
Categoría: {product["category"]}
Disponibilidad: {product["quantity"]}""")
        if found == 0:
            print("No se ha encontrado ningún producto con esta disponibilidad.")

def modify_product(obtener_info_apis):
    '''Recibe un input para un atributo preexistente
       Actualiza el valor
       Inprime el objeto con el atributo modificado.
    '''

    print("""PRODUCTOS:
    """)

    for x, producto in enumerate(productos):
        print(f"{x+1}. {producto['name']}, {producto['category']}")

    modify = input(f"""
Seleccione el producto que desea modificar:

>> """)

    while not modify.isnumeric() or int(modify) not in range(1, len(productos)+1):
            modify = input("""Error! Ingrese una respuesta válida:
            
>> """)

    modify = int(modify)-1

    modified_product = productos[modify]

    option = input("""Seleccione lo que desea modificar:

1. Nombre.
2. Descripción.
3. Precio.
4. Categoría.
5. Inventario disponible.

>> """)

    while not option.isnumeric() or int(option) not in range(1, 6):
            option = input("Error! Ingrese una respuesta válida: ")

    if option == "1":
        name = input("Ingrese un nombre nuevo: ")
        modified_product["name"] = name

    elif option == "2":
        description = input("Ingrese una descipción nueva: ")
        modified_product["description"] = description

    elif option == "3":
        price = input("Ingrese un precio nuevo: ")
        while not price.isnumeric() or int(price) < 1:
            price = input("Error! Ingrese un precio válido: ")
        price = int(price)
        modified_product["price"] = price

    elif option == "4":
        category = input("Ingrese una categoría nueva: ")
        while not category.isalpha() or " " in category:
            category = input("Error! Ingrese una categoría válida: ")
        modified_product["category"] = category.capitalize()

    elif option == "5":
        quantity = input("Inventario disponible: ")
        while not quantity.isnumeric() or int(quantity) < 0:
            quantity = input("Error! Ingrese un número inventario válido: ")
        quantity = int(quantity)
        modified_product["quantity"] = quantity

    completed = input("""El producto ha sido modificado exitosamente:
    
1. Mostrar producto modificado.
2. Salir.

>> """)

    if completed == "1":
        print(f"""
Nombre: {modified_product["name"]}
Descripción: {modified_product["description"]}
Precio: ${modified_product["price"]}
Categoría: {modified_product["category"]}
Disponibilidad: {modified_product["quantity"]}""")
    else:
        exit()

def delete_product(obtener_info_apis):
    '''Recibe dos atributos
       Busca en una lista de diccionarios
       Elimina el objeto si ambos atributos coinciden.
    '''
        
    print("""Para eliminar un producto de la tienda coloque la siguiente información:
    """)

    found = 0

    name = input("Nombre: ")

    price = input("Precio: ")
    while not price.isnumeric() or int(price) < 1:
        price = input("Error! Ingrese un precio válido: ")
    price = int(price)

    category = input("Categoría: ").capitalize()
    while not category.isalpha() or " " in category:
        category = input("Error! Ingrese una categoría válida: ").capitalize()

    for product in productos:
        if product["category"] == category and product["price"] == price and product["name"] == name:
            found += 1
            productos.remove(product)
            print("El producto se ha eliminado con exito.")
    if found == 0:
        print("El producto no existe y por tanto no se puede eliminar.")
        exit()

#GESTIÓN DE VENTAS

def register_sale():
    '''Recibe siete atributos
       Crea una clase
       Convierte la clase en un diccionario
       Inprime la venta creada
       Genera una factura y la imprime.
    '''

    global total_breakdown

    purchased_products = [{"name": "Makoto", "description": "Bad", "price": 45, "category": "Comida", "inventory": 23, "amount_product": 5},
                          {"name": "Jabón", "description": "Good", "price": 22, "category": "Limpieza", "inventory": 5, "amount_product": 7}]
    
    list_products = []

    prices = []
    amounts = []

    print("""Para registrar una venta es necesario que coloque la siguiente información:
    """)

    buyer = input("Cédula del cliente: ")
    while len(buyer) != 8 or not buyer.isnumeric():
        buyer = input("Error! Ingrese una cédula válida: ")

    found = 0

    for client in clientes:
        if buyer == client["id"]:
            found += 1
            buyer = client["name_lastname"]
            if client["type"] == "Jurídico":
                payment = input("""Pago por contado:

1. Si.
2. No.

>> """)         
                while not payment.isnumeric() or int(payment) not in range(1,3):
                    payment = input("""Error! Ingrese una opción válida:

1. Si.
2. No.

>> """)         
                if payment == "1":
                    discount = 0.95
                    porcentage = "%5"
                elif payment == "2":
                    discount = 1
                    porcentage = "Ninguno"
            elif client["type"] == "Natural":
                discount = 1
                porcentage = "Ninguno"
    if found == 0:
        print("No existe nigún cliente con esa información.")
        exit()

    print("""Ingrese la fecha de la venta:
    """)
        
    dd = input("Día: ")
    while not dd.isnumeric() or int(dd) < 1 or int(dd) > 31:
        dd = input("Error! Coloque un día válido: ")
    if len(dd) < 2:
        dd = f"0{dd}"

    mm = input("Mes: ")
    while not mm.isnumeric() or int(mm) < 1 or int(mm) > 12:
        mm = input("Error! Coloque un mes válido: ")
    if len(mm) < 2:
        mm = f"0{mm}"

    yy = input("Año: ")
    while not yy.isnumeric() or int(yy) < 2023 or len(yy) > 4:
        yy = input("Error! Coloque un año válido: ")

    date = f"{dd}/{mm}/{yy}"

    currency = input("""Seleccione el tipo de moneda del pago: 
        
1. USD (Dólares Americanos).
2. BS (Bolívares).

>> """)
                     
    while int(currency) not in range(1,3):
        currency = input("""Error! Seleccione un tipo de moneda válido: 
        
1. USD (Dólares Americanos).
2. BS (Bolívares).

>> """)
                     
    if currency == "1":
        currency = "USD (Dólares Americanos)"
        igtf = 0.03
    elif currency == "2":
        currency = "BS (Bolívares)"
        igtf = 0

    print("""
PRODUCTOS:
""")

    for x, producto in enumerate(productos):
        list_products.append(f"{x+1}. {producto['name']}, ${producto['price']}, {producto['category']} - Disponibilidad: {producto['quantity']}")

    print("""Seleccione el producto comprado:
    """)

    for producto in list_products:
        print(producto)

    purchased = input("""
>> """)

    while not purchased.isnumeric() or int(purchased) not in range(1, len(productos)+1):
            print("""Error! Ingrese una respuesta válida:
            """)

            for producto in list_products:
                print(producto)

            purchased = input("""
>> """)
                           
    amount_product = input("""Ingrese la cantidad comprada de este producto:
                           
>> """)
                           
    while not amount_product.isnumeric() or int(amount_product) < 1:
        amount_product = input("Error! Ingrese una cantidad válida: ")

    found = 0

    for producto in productos:
        producto["quantity"] -= int(amount_product)
        if producto["quantity"] >= 0:
            found += 1
            producto["amount_product"] = int(amount_product)
    if found == 0:
        print("Error! la cantidad comprada excede la disponibilidad del producto.")
        exit()

    purchased = int(purchased) - 1
    purchased_products.append(productos[purchased])

    payment_method = input("""Seleccione el tipo de pago realizado:
        
1. PdV
2. PM
3. Zelle
4. Cash

>> """)
    
    while not payment_method.isnumeric() or int(payment_method) not in range(1,5):
        payment_method = input("""Error! Seleccione un tipo de pago válido:
        
1. PdV
2. PM
3. Zelle
4. Cash

>> """)
                           
    if payment_method == "1":
        payment_method = "PdV"
    elif payment_method == "2":
        payment_method = "PM"
    elif payment_method == "3":
        payment_method = "Zelle"
    elif payment_method == "4":
        payment_method = "Cash"

    shipping_service = input("""Escoja el servicio de envío:
        
1. MRW.
2. Zoom.
3. Delivery.

>> """)

    while not shipping_service.isnumeric() or int(shipping_service) not in range(1,4):
        shipping_service = input("""Error! Escoja una opción válida:

1. MRW.
2. Zoom.
3. Delivery.

>> """)

    if shipping_service == "1":
        shipping_service = "MRW"
    elif shipping_service == "2":
        shipping_service = "Zoom"
    elif shipping_service == "3":
        shipping_service = "Delivery"

    for product in purchased_products:
        prices.append(product["price"])
        amounts.append(product["amount_product"])

    subtotal = []

    for x, y in zip(prices, amounts):
        subtotal.append(x * y)
    
    subtotal = sum(subtotal)

    iva = round(subtotal * 0.16)

    igtf = round(subtotal * igtf)

    total = round((subtotal + iva + igtf) * discount)

    total_breakdown = {"subtotal": subtotal, "discount": discount, "iva": iva, "igtf": igtf, "total": total}

    sale = Sale(buyer, date, purchased_products, amount_product, payment_method, shipping_service, total_breakdown["total"]).convert_dicc()

    ventas.append(sale)

    completed = input("""
La venta se ha registrado con exito:

1. Mostrar la venta
2. Generar factura.
3. Salir.

>> """)
                      
    if completed == "1":
        print(f"""
Cliente: {buyer}
Fecha de venta: {date}
Moneda de pago: {currency}
Producto comprado: {product["name"]}
Cantidad: {sale["amount_product"]}
Costo total: ${total}
Método de pago: {payment_method}
Servicio de delivery: {shipping_service}""")

    elif completed == "2":
        print(f"""
Subtotal: ${subtotal}
Descuento disponible: {porcentage}
IVA (16%): ${iva}
IGTF (3%): ${igtf}
Total: ${total}""")
    else:
        exit()

def search_sale():
    '''Recibe un input
       Busca el input como un valor en una lista de diccionarios
       Inprime los productos cuyo valor coincide con el input.
    '''

    filter = input("""Para buscar la venta seleccione alguno de lo siguientes filtros de búsqueda:

1. Cliente.
2. Fecha de la venta.
3. Monto total de la venta.

>> """)

    while not filter.isnumeric() or int(filter) not in range (1,4):
        filter = input("""Error! Seleccione una opción válida:

1. Cliente.
2. Fecha de la venta.
3. Monto total de la venta.

>> """)
    
    if filter == "1":
        found = 0
        name = input("Nombre del cliente: ")
        while not name.isalpha():
            name = input("Error! Coloca un nombre válido: ")
        lastname = input("Apellido del cliente: ")
        while not lastname.isalpha():
            lastname = input("Error! Coloca un apellido válido: ")

        name_lastname = f"{name.capitalize()} {lastname.capitalize()}"

        buyer = name_lastname

        for venta in ventas:
            if buyer == venta["buyer"]:
                found += 1
                print(f"""
Cliente: {venta["buyer"]}
Fecha de venta: {venta["date"]}
Producto comprado: {product["name"]}
Cantidad: {venta["amount_product"]}
Monto total: ${venta["total_breakdown"]}
Método de pago: {venta["payment_method"]}
Servicio de delivery: {venta["shipping_service"]}""")
        if found == 0:
            print("No se encontro nigún pago.")
            exit()

    elif filter == "2":
        found = 0
        print("""Fecha de la venta:
    """)
        
        dd = input("Día: ")
        while not dd.isnumeric() or int(dd) < 1 or int(dd) > 31:
            dd = input("Error! Coloque un día válido: ")
        if len(dd) < 2:
            dd = f"0{dd}"

        mm = input("Mes: ")
        while not mm.isnumeric() or int(mm) < 1 or int(mm) > 12:
            mm = input("Error! Coloque un mes válido: ")
        if len(mm) < 2:
            mm = f"0{mm}"

        yy = input("Año: ")
        while not yy.isnumeric() or int(yy) < 2023 or len(yy) > 4:
            yy = input("Error! Coloque un año válido: ")
            
        date = f"{dd}/{mm}/{yy}"

        for venta in ventas:
            if date == venta["date"]:
                found += 1
                print(f"""
Cliente: {venta["buyer"]}
Fecha de venta: {venta["date"]}
Producto comprado: {product["name"]}
Cantidad: {venta["amount_product"]}
Monto total: ${venta["total_breakdown"]}
Método de pago: {venta["payment_method"]}
Servicio de delivery: {venta["shipping_service"]}""")
        if found == 0:
            print("No se encontro nigún pago.")
            exit()

    elif filter == "3":
        found = 0
        total_breakdown = input("Monto total de la venta: ")
        while not total_breakdown.isnumeric() or int(total_breakdown) < 1:
            total_breakdown = input("Monto total de la venta: ")

        total_breakdown = int(total_breakdown)

        for venta in ventas:
            if total_breakdown == venta["total_breakdown"]:
                found += 1
                print(f"""
Cliente: {venta["buyer"]}
Fecha de venta: {venta["date"]}
Producto comprado: {product["name"]}
Cantidad: {venta["amount_product"]}
Monto total: ${venta["total_breakdown"]}
Método de pago: {venta["payment_method"]}
Servicio de delivery: {venta["shipping_service"]}""")
        if found == 0:
            print("No se encontro nigún pago.")
            exit()

#GESTIÓN DE CLIENTES

def register_client():
    '''Recibe 6 atributos
       Crea una clase
       Convierte la clase en un diccionario
       Agrega la clase a una lista
       Imprime la clase creada.
    '''

    global cliente

    print("""Para agregar un cliente nuevo coloque la siguiente información:
        """)
    
    registered = 0

    name = input("Nombre del cliente: ")
    while not name.isalpha():
        name = input("Error! Coloca un nombre válido: ")
    lastname = input("Apellido del cliente: ")
    while not lastname.isalpha():
        lastname = input("Error! Coloca un apellido válido: ")

    name_lastname = f"{name.capitalize()} {lastname.capitalize()}"

    type = input("""Tipo de cliente:

1. Natural.
2. Jurídico.
        
>> """)
    
    while not type.isnumeric() or int(type) not in range (1,3):
        type = input("""Error! Seleccione un tipo de cliente válido:

1. Natural.
2. Jurídico.
        
>> """)

    if type == "1":
            type = "Natural"
    elif type == "2":
            type = "Jurídico"

    id = input("Cédula: ")
    while len(id) != 8 or not id.isnumeric():
        id = input("Error! Ingrese una cédula válida: ")

    email = input("Correo electrónico: ")
    while not "@" in email or not ".com" in email:
            email = input("Error! Ingrese un correo electrónico válido: ")

    shipping_address = input("Dirección de envío: ")

    phone_number = input("Número telefónico: ")
    while not phone_number.isnumeric() or len(phone_number) != 11:
        phone_number = input("Error! Ingrese un número telefónico válido: ")

    cliente = Client(name_lastname, type, id, email, shipping_address, phone_number)

    for client in clientes:
        if id == client["id"] or email == client["email"] or phone_number == client["phone_number"]:
            registered += 1
            print("Lo sentimos, pero ya existe un cliente registrado con esa información")
            break
    if registered == 0:
        clientes.append(cliente.convert_dicc())
        completed = input("""
El cliente se ha registrado con exito:

1. Mostrar cliente.
2. Salir.

>> """)

        if completed == "1":
            print(f"""
Nombre y apellido: {name_lastname}
Tipo: {type}
Cédula: {id}
Correo electrónico: {email}
Dirección de envío: {shipping_address}
Teléfono: {phone_number}""")
        else:
            exit()

def modify_client():
    '''Recibe un input para un atributo preexistente
       Actualiza el valor
       Inprime el objeto con el atributo modificado.
    '''

    list_clients = []

    print("""CLIENTES:
    """)

    for x, client in enumerate(clientes):
        list_clients.append(f"{x+1}. {client['name_lastname']} - ID: {client['id']}")

    print("""Seleccione al cliente que desea modificar:
    """)

    for client in list_clients:
        print(client)

    modify = input("""
>> """)

    while not modify.isnumeric() or int(modify) not in range(1, len(clientes)+1):
            print("""Error! Ingrese una respuesta válida:
            """)

            for client in list_clients:
                print(client)

            modify = input("""
>> """)

    modify = int(modify)-1

    modified_client = clientes[modify]

    option = input("""Seleccione lo que desea modificar:

1. Nombre y apellido.
2. Tipo.
3. Cédula.
4. Correo electrónico.
5. Dirección de envío.
6. Telefóno.

>> """)
                   
    while not option.isnumeric() or int(option) not in range(1, 7):
        option = input("""Error! Ingrese una respuesta válida:

1. Nombre y apellido.
2. Tipo.
3. Cédula.
4. Correo electrónico.
5. Dirección de envío.
6. Telefóno.

>> """)

    if option == "1":
        name = input("Nombre del cliente: ")
        while not name.isalpha():
            name = input("Error! Coloca un nombre válido: ")
        lastname = input("Apellido del cliente: ")
        while not lastname.isalpha():
            lastname = input("Error! Coloca un apellido válido: ")

        name_lastname = f"{name.capitalize()} {lastname.capitalize()}"

        modified_client["name_lastname"] = name_lastname

    elif option == "2":
        type = input("""Escoja el tipo de cliente al que desea cambiar:

1. Natural.
2. Jurídico.
        
>> """)
    
        while not type.isnumeric() or int(type) not in range (1,3):
            type = input("""Error! Seleccione un tipo de cliente válido:

1. Natural.
2. Jurídico.
        
>> """)

        if type == "1":
            type = "Natural"
        elif type == "2":
            type = "Jurídico"

        modified_client["type"] = type
    
    elif option == "3":
        id = input("Cédula: ")
        while len(id) != 8 or not id.isnumeric():
            id = input("Error! Ingrese una cédula válida: ")
        
        modified_client["id"] = id

    elif option == "4":
        email = input("Correo electrónico: ")
        while not "@" in email or not ".com" in email:
            email = input("Error! Ingrese un correo electrónico válido: ")

        modified_client["email"] = email

    elif option == "5":
        shipping_address = input("Modifique la dirección de envío: ")
    
        modified_client["shipping_address"] = shipping_address
        
    elif option == "6":
        phone_number = input("Modifique el número telefónico: ")
        while not phone_number.isnumeric() or len(phone_number) != 11:
            phone_number = input("Error! Ingrese un número telefónico válido: ")
        
        modified_client["phone_number"] = phone_number

    completed = input("""
El cliente se ha modificado con exito:

1. Mostrar cliente modificado.
2. Salir.

>> """)

    if completed == "1":
        print(f"""
Nombre y apellido: {modified_client["name_lastname"]}
Tipo: {modified_client["type"]}
Cédula: {modified_client["id"]}
Correo electrónico: {modified_client["email"]}
Dirección de envío: {modified_client["shipping_address"]}
Teléfono: {modified_client["phone_number"]}""")
    else:
        exit()

def delete_client():
    '''Recibe dos atributos
       Busca en una lista de diccionarios
       Elimina el objeto si ambos atributos coinciden.
    '''

    print("""Para eliminar a un cliente de la tienda coloque la siguiente información:
        """)
    
    found = 0

    id = input("Cédula: ")
    while len(id) != 8 or not id.isnumeric():
        id = input("Error! Ingrese una cédula válida: ")
    
    email = input("Correo electrónico: ")
    while not "@" in email or not "." in email:
            email = input("Error! Ingrese un correo electrónico válido: ")

    for cliente in clientes:
        if id == cliente["id"] and email == cliente["email"]:
            found += 1
            clientes.remove(cliente)
            print(f"El cliente ha sido eliminado con exito.")
    if found == 0:
            print("No existe ningún cliente con esta información y por tanto no se puede eliminar.")
            exit()

def search_client():
    '''Recibe un input
       Busca el input como un valor en una lista de diccionarios
       Inprime los productos cuyo valor coincide con el input.
    '''

    option = input("""Para buscar al cliente seleccione el filtro de búsqueda:

1. Cédula.
2. Correo electrónico.

>> """)
    
    while not option.isnumeric() or int(option) not in range (1,3):
        option = input("""Error! Seleccione una opción válida:

1. Cédula.
2. Correo electrónico.

>> """)

    if option == "1":
        found = 0
        id = input("""Coloque la cédula del cliente:

>> """)
        while len(id) != 8 or not id.isnumeric():
            id = input("Error! Ingrese una cédula válida: ")

        for cliente in clientes:
            if id == cliente["id"]:
                found += 1
                print(f"""
Nombre: {cliente['name_lastname']}
Tipo: {cliente['type']}
Email: {cliente['email']}
Telefono: {cliente['phone_number']}""")
        if found == 0:
            print("No se encontro nigún cliente.")
            exit()


    if option == "2":
        found = 0
        email = input("""Coloque el correo electrónico del cliente:

>> """)

        while not "@" in email or not "." in email:
            email = input("Error! Ingrese un correo electrónico válido: ")

        for cliente in clientes:
            if email == cliente["email"]:
                found += 1
                print(f"""
Nombre: {cliente['name_lastname']}
Tipo: {cliente['type']}
Email: {cliente['email']}
Telefono: {cliente['phone_number']}""")
        if found == 0:
            print("No se encontro nigún cliente.")
            exit()

#GESTIÓN DE PAGOS

def register_payment():
    '''Recibe 5 atributos
       Crea una clase
       Convierte la clase en un diccionario
       Agrega la clase a una lista
       Imprime la clase creada.
    '''

    print("""Para registrar un pago coloque la siguiente información:
        """)

    client = input("La cédula del comprador: ")
    while len(client) != 8 or not client.isnumeric():
        client = input("Error! Ingrese una cédula válida: ")

    found = 0

    for comprador in clientes:
        if comprador.get("id") == client:
            found += 1
            client = comprador["name_lastname"]
            continue
    if found == 0:
        print("Este pago no puede ser registrado ya que el cliente no existe en el sistema.")
        exit()

    
    amount = input("Ingrese la cantidad del producto comprado: ")
    while not amount.isnumeric() or int(amount) < 1:
        amount = input("Ingrese una cantidad válida: ")

    currency = input("""Seleccione el tipo de moneda del pago: 
        
1. USD (Dólares Americanos).
2. BS (Bolívares).

>> """)
                     
    while int(currency) not in range(1,3):
        currency = input("""Error! Seleccione un tipo de moneda válido: 
        
1. USD (Dólares Americanos).
2. BS (Bolívares).

>> """)
                     
    if currency == "1":
        currency = "USD (Dólares Americanos)"
    elif currency == "2":
        currency = "BS (Bolívares)"

    payment_method = input("""Seleccione el tipo de pago realizado:
        
1. PdV
2. PM
3. Zelle
4. Cash

>> """)
    
    while not payment_method.isnumeric() or int(payment_method) not in range(1,5):
        payment_method = input("""Error! Seleccione un tipo de pago válido:
        
1. PdV
2. PM
3. Zelle
4. Cash

>> """)
                           
    if payment_method == "1":
        payment_method = "PdV"
    elif payment_method == "2":
        payment_method = "PM"
    elif payment_method == "3":
        payment_method = "Zelle"
    elif payment_method == "4":
        payment_method = "Cash"

    print("""Ingrese la fecha del pago:
    """)

    dd = input("Día: ")
    while not dd.isnumeric() or int(dd) < 1 or int(dd) > 31:
        dd = input("Error! Coloque un día válido: ")
    if len(dd) < 2:
        dd = f"0{dd}"

    mm = input("Mes: ")
    while not mm.isnumeric() or int(mm) < 1 or int(mm) > 12:
        mm = input("Error! Coloque un mes válido: ")
    if len(mm) < 2:
        mm = f"0{mm}"

    yy = input("Año: ")
    while not yy.isnumeric() or int(yy) < 2023 or len(yy) > 4:
        yy = input("Error! Coloque un año válido: ")

    payment_date = f"{dd}/{mm}/{yy}"

    pago = Payment(client, amount, currency, payment_method, payment_date).convert_dicc

    pagos.append(pago)

    completed = input("""El pago ha sido registrado con exito:
    
1. Mostrar pago.
2. Salir.

>> """)
    if completed == "1":
        print(f"""
Nombre del cliente: {client}
Monto total: {amount}
Moneda del pago: {currency}
Tipo de pago: {payment_method}
Fecha del pago: {payment_date}""")
    else:
        exit()

def search_payment():
    '''Recibe un input
       Busca el input como un valor en una lista de diccionarios
       Inprime los productos cuyo valor coincide con el input.
    '''

    filter = input("""Para buscar un pago, seleccione alguno de los siguientes filtros de búsqueda:

1. Cliente.
2. Fecha.
3. Tipo de pago
4. Moneda de pago.

>> """)
          
    while not filter.isnumeric() or int(filter) not in range (1,8):
        filter = input("""Error! Seleccione un filtro de búsqueda válido:

1. Cliente.
2. Fecha.
3. Tipo de pago
4. Moneda de pago.

>> """)
                       
    if filter == "1":
        found = 0

        name = input("Nombre del cliente: ")
        while not name.isalpha():
            name = input("Error! Coloca un nombre válido: ")
        lastname = input("Apellido del cliente: ")
        while not lastname.isalpha():
            lastname = input("Error! Coloca un apellido válido: ")

        client = f"{name.capitalize()} {lastname.capitalize()}"

        for pago in pagos:
            if client == pago["client"]:
                found += 1
                print(f"""
Cliente: {pago["client"]}
Monto total: {pago["amount"]}
Moneda del pago: {pago["currency"]}
Tipo de pago: {pago["payment_method"]}
Fecha del pago: {pago["payment_date"]}""")
        if found == 0:
            print("No se encontro nigún pago.")
            exit()

                      
    elif filter == "2":
        found = 0
        print("""Fecha del pago:
    """)
        
        dd = input("Día: ")
        while not dd.isnumeric() or int(dd) < 1 or int(dd) > 31:
            dd = input("Error! Coloque un día válido: ")
        if len(dd) < 2:
            dd = f"0{dd}"

        mm = input("Mes: ")
        while not mm.isnumeric() or int(mm) < 1 or int(mm) > 12:
            mm = input("Error! Coloque un mes válido: ")
        if len(mm) < 2:
            mm = f"0{mm}"

        yy = input("Año: ")
        while not yy.isnumeric() or int(yy) < 2023 or len(yy) > 4:
            yy = input("Error! Coloque un año válido: ")
            
        payment_date = f"{dd}/{mm}/{yy}"

        for pago in pagos:
            if payment_date == pago["payment_date"]:
                found += 1
                print(f"""
Cliente: {pago["client"]}
Monto total: {pago["amount"]}
Moneda del pago: {pago["currency"]}
Tipo de pago: {pago["payment_method"]}
Fecha del pago: {pago["payment_date"]}""")
        if found == 0:
            print("No se encontro nigún pago.")
            exit()
            

    elif filter == "3":
        found = 0
        payment_method = input("""Método de pago:
        
1. PdV
2. PM
3. Zelle
4. Cash

>> """)
    
        while not payment_method.isnumeric() or int(payment_method) not in range(1,5):
            payment_method = input("""Error! Seleccione un tipo de pago válido:
        
1. PdV
2. PM
3. Zelle
4. Cash

>> """)
                           
        if payment_method == "1":
            payment_method = "PdV"
        elif payment_method == "2":
            payment_method = "PM"
        elif payment_method == "3":
            payment_method = "Zelle"
        elif payment_method == "4":
            payment_method = "Cash"

        for pago in pagos:
            if payment_method == pago["payment_method"]:
                found += 1
                print(f"""
Cliente: {pago["client"]}
Monto total: {pago["amount"]}
Moneda del pago: {pago["currency"]}
Tipo de pago: {pago["payment_method"]}
Fecha del pago: {pago["payment_date"]}""")
        if found == 0:
            print("No se encontro nigún pago.")
            exit()


    elif filter == "4":
        found = 0
        currency = input("""Tipo de moneda: 
        
1. USD (Dólares Americanos).
2. BS (Bolívares).

>> """)
                     
        while int(currency) not in range(1,3):
            currency = input("""Error! Seleccione un tipo de moneda válido: 
        
1. USD (Dólares Americanos).
2. BS (Bolívares).

>> """)
                     
        if currency == "1":
            currency = "USD (Dólares Americanos)"
        elif currency == "2":
            currency = "BS (Bolívares)"

        for pago in pagos:
            if currency == pago["currency"]:
                found += 1
                print(f"""
Cliente: {pago["client"]}
Monto total: {pago["amount"]}
Moneda del pago: {pago["currency"]}
Tipo de pago: {pago["payment_method"]}
Fecha del pago: {pago["payment_date"]}""")
        if found == 0:
            print("No se encontro nigún pago.")
            exit()

#GESTIÓN DE ENVÍOS

def register_delivery():
    '''Recibe 8 atributos
       Crea una clase
       Convierte la clase en un diccionario
       Agrega la clase a una lista
       Inprime la clase creada.
    '''

    global purchase_order

    print("""Para registrar un envío coloque la siguiente información:
    """)

    address = input("Dirección de envío: ")
    
    print ("""
Fecha de compra:
    """)

    dd = input("Día: ")
    while not dd.isnumeric() or int(dd) < 1 or int(dd) > 31:
        dd = input("Error! Coloque un día válido: ")
    if len(dd) < 2:
        dd = f"0{dd}"

    mm = input("Mes: ")
    while not mm.isnumeric() or int(mm) < 1 or int(mm) > 12:
        mm = input("Error! Coloque un mes válido: ")
    if len(mm) < 2:
        mm = f"0{mm}"

    yy = input("Año: ")
    while not yy.isnumeric() or int(yy) < 2023 or len(yy) > 4:
        yy = input("Error! Coloque un año válido: ")

    date = f"{dd}/{mm}/{yy}"


    name = input("Nombre del cliente: ")
    while not name.isalpha():
        name = input("Error! Coloca un nombre válido: ")
    lastname = input("Apellido del cliente: ")
    while not lastname.isalpha():
        lastname = input("Error! Coloca un apellido válido: ")

    client_name = f"{name.capitalize()} {lastname.capitalize()}"


    client_phone = input("Número telefónico: ")
    while not client_phone.isnumeric() or len(client_phone) != 11:
        client_phone = input("Error! Ingrese un número telefónico válido: ")

    order_number = input("Número de orden: ")
    while not order_number.isnumeric or int(order_number) < 1:
        order_number = input("Número de orden: ")

    purchase_order = {"address": address, "date": date, "client_name": client_name, "client_phone": client_phone, "order_number": order_number}

    shipping_service = input("""Escoja el servicio de envío:
        
1. MRW.
2. Zoom.
3. Delivery.

>> """)

    while not shipping_service.isnumeric() or int(shipping_service) not in range(1,4):
        shipping_service = input("""Error! Escoja una opción válida:

1. MRW.
2. Zoom.
3. Delivery.

>> """)

    if shipping_service == "1":
        shipping_service = "MRW"
        service_cost = 10
        motorizado = "Ninguno"
        envio = Shipping(purchase_order["order_number"], purchase_order["client_name"], purchase_order["client_phone"], purchase_order["date"], purchase_order["address"], shipping_service, motorizado, service_cost).convert_dicc()
    elif shipping_service == "2":
        shipping_service = "Zoom"
        service_cost = 12
        motorizado = "Ninguno"
        envio = Shipping(purchase_order["order_number"], purchase_order["client_name"], purchase_order["client_phone"], purchase_order["date"], purchase_order["address"], shipping_service, motorizado, service_cost).convert_dicc()
    elif shipping_service == "3":
        shipping_service = "Delivery"
        print("""Ingrese los datos del motorizado:
            """)

        name = input("Nombre del motorizado: ")

        phone_number = input("Número telefónico: ")
        while not phone_number.isnumeric() or len(phone_number) != 11:
            phone_number = input("Error! Ingrese un número telefónico válido: ")

        id = input("Cédula de identidad: ")
        while not id.isnumeric() or len(id) != 8:
            id = input("Error! Ingrese una cédula de identidad válida: ")

        license_plate = input("Número de placa: ")
        motorizado = Motorizado(name, phone_number, id,license_plate)
        service_cost = 3
        envio = Shipping(purchase_order["order_number"], purchase_order["client_name"], purchase_order["client_phone"], purchase_order["date"], purchase_order["address"], shipping_service, motorizado.show_name(), service_cost).convert_dicc()
    
    envios.append(envio)

    completed = input("""
El envío se ha registrado con exito!
    
1. Mostrar envío.
2. Salir.

>> """)
    
    if completed == "1":
        print(f"""
Número de orden: {purchase_order["order_number"]}
Nombre: {purchase_order["client_name"]}
Telefóno: {purchase_order["client_phone"]}
Dirección: {purchase_order["address"]}
Fecha: {purchase_order["date"]}
Servicio de delivery: {envio["shipping_service"]}
Costo del servicio: ${envio["service_cost"]}""")
    else:
        exit()

def search_delivery():
    '''Recibe un input
       Busca el input como un valor en una lista de diccionarios
       Inprime los productos cuyo valor coincide con el input.
    '''
    
    filter = input("""Para buscar el envío seleccione el filtro de búsqueda:

1. Cliente.
2. Fecha.
    
>> """)
    
    while not filter.isnumeric() or int(filter) not in range (1,3):
        filter = input("""Error! Selecciones una opción válida:

1. Cliente.
2. Fecha.
    
>> """)

    if filter == "1":
        found = 0
        print("""Ingrese la siguiente información acerca del cliente:
        """)

        name = input("Nombre del cliente: ")
        while not name.isalpha():
            name = input("Error! Coloca un nombre válido: ")
        lastname = input("Apellido del cliente: ")
        while not lastname.isalpha():
            lastname = input("Error! Coloca un apellido válido: ")

        client_name = f"{name.capitalize()} {lastname.capitalize()}"

        client_phone = input("Número telefónico del cliente: ")

        x = 1

        for envio in envios:
            if envio["client_name"] == client_name and envio["client_phone"] == client_phone:
                found += 1
                print(f"""
Envío #{x} de este cliente:

Número de orden: {envio["purchase_order"]}
Nombre: {envio["client_name"]}
Telefóno: {envio["client_phone"]}
Fecha: {envio["date"]}
Servicio de delivery: {envio["shipping_service"]}
Costo del servicio: ${envio["service_cost"]}""")
                x += 1
        if found == 0:
            print("No se encontro nigún envío.")
            exit()

    elif filter == "2":
        found = 0
        print("""Ingrese la fecha del pedido:
        """)
        
        dd = input("Día: ")
        while not dd.isnumeric() or int(dd) < 1 or int(dd) > 31:
            dd = input("Error! Coloque un día válido: ")
        if len(dd) < 2:
            dd = f"0{dd}"

        mm = input("Mes: ")
        while not mm.isnumeric() or int(mm) < 1 or int(mm) > 12:
            mm = input("Error! Coloque un mes válido: ")
        if len(mm) < 2:
            mm = f"0{mm}"

        yy = input("Año: ")
        while not yy.isnumeric() or int(yy) < 2023 or len(yy) > 4:
            yy = input("Error! Coloque un año válido: ")

        date = f"{dd}/{mm}/{yy}"

        x = 1

        for envio in envios:
            if envio["date"] == date:
                found += 1
                print(f"""
Envío #{x}:

Número de orden: {envio["purchase_order"]}
Nombre: {envio["client_name"]}
Telefóno: {envio["client_phone"]}
Fecha: {envio["date"]}
Servicio de delivery: {envio["shipping_service"]}
Costo del servicio: ${envio["service_cost"]}""")
                x += 1
        if found == 0:
            print("No se encontro nigún envío.")
            exit()


menu = input("""¡Bienvenido a Nature Store!

Por favor escoja algunas de las opciones a continuación:

1. Gestión de productos
2. Gestión de ventas
3. Gestión de clientes
4. Gestión de pagos
5. Gestión de envíos
6. Indicadores de gestión (estadísticas)
7. Salir

>> """)

while not menu.isnumeric() or int(menu) not in range (1,8):
    menu = input("""Error! Por favor escoja una opción válida:

1. Gestión de productos
2. Gestión de ventas
3. Gestión de clientes
4. Gestión de pagos
5. Gestión de envíos
6. Indicadores de gestión (estadísticas)
7. Salir

>> """)

if menu == "1":
    options = input("""Escoja la acción que desea realizar:
    
1. Agregar nuevo producto a la tienda.
2. Buscar producto.
3. Modificar la información de producto existente.
4. Eliminar producto de la tienda.

>> """)

    while not options.isnumeric() or int(options) not in range(1,5):
        options = input("""Error! Selecciones una opción válida:
    
1. Registrar nuevo cliente.
2. Modificar la información de un cliente existente.
3. Eliminar clientes de la tienda.
4. Buscar cliente.

>> """)            

    if options == "1":
        added_product = add_product(obtener_info_apis)

    elif options == "2":
        searched_product = search_product(obtener_info_apis)

    elif options == "3":
        modified_product = modify_product(obtener_info_apis)

    elif options == "4":
        deleted_product = delete_product(obtener_info_apis)

if menu == "2":
    
    options = input("""Escoja la acción que desea realizar:
    
1. Registrar venta.
2. Buscar venta.

>> """)
                    
    while not options.isnumeric() or int(options) not in range(1,3):
        options = input("""Error! Seleccione una opción válida:

1. Registrar venta.
2. Buscar venta.

>> """)
                        
    if options == "1":
        registered_sale = register_sale()

    if options == "2":
        searched_sale = search_sale()

if menu == "3":
    options = input("""Escoja la acción que desea realizar:
    
1. Registrar nuevo cliente.
2. Modificar la información de un cliente existente.
3. Eliminar clientes de la tienda.
4. Buscar cliente.

>> """)
                    
    while not options.isnumeric() or int(options) not in range(1,5):
        options = input("""Error! Seleccione una opción válida:
    
1. Registrar nuevo cliente.
2. Modificar la información de un cliente existente.
3. Eliminar clientes de la tienda.
4. Buscar cliente.

>> """)
                    
    if options == "1":
        registered_client = register_client()

    if options == "2":
        modified_client = modify_client()

    if options == "3":
        deleted_client = delete_client()

    if options == "4":
       searched_client = search_client()

if menu == "4":
    options = input("""Escoja la acción que desea realizar:
    
1. Registrar pago.
2. Buscar pago.

>> """)
                    
    while not options.isnumeric() or int(options) not in range(1,3):
        options = input("""Error! Escoja una opción válida:
    
1. Registrar pago.
2. Buscar pago.

>> """)

    if options == "1":
        registered_payment = register_payment()

    elif options == "2":
        searched_payment = search_payment()

if menu == "5":
    options = input("""Escoja la acción que desea realizar:
    
1. Registrar envío.
2. Buscar envío.

>> """)
    
    while not options.isnumeric() or int(options) not in range(1,3):
        options = input("""Error! Escoja una opción válida:
    
1. Registrar envío.
2. Buscar envío.

>> """)

    if options == "1":
        registered_delivery = register_delivery()

    elif options == "2":
        searched__delivery = search_delivery()

if menu == "7":
    exit()