def ask_name():
    while True:
        name = input("Ingrese el nombre del vendedor: ").strip()

        if name != "":
            return name

        print("Error: El nombre no puede estar vacío.")


def ask_sale():
    while True:
        try:
            sale = float(input("Ingrese el monto total de ventas del mes: "))

            if sale < 0:
                print("Error: El monto de ventas no puede ser negativo.")
            else:
                return sale

        except ValueError:
            print("Error: Por favor ingrese un número válido para el monto de ventas.")
