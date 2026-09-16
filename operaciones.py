# operaciones.py

def validate_sales(sales):
    """|
    Valida que el importe de venta no sea negativo.
    """
    return sales >= 0


def validate_name(name):
    """
    validar que el nombre del vendedor no esté vacío.
    """
    return name.strip() != ""


def get_sales_category(sales):
    """
    Devuelve la venta de ventas basada en el monto de ventas.
    """
    if sales >= 50000:
        return "ventas superiores"
    elif sales >= 25000:
        return "ventas altas"
    elif sales >= 10000:
        return "ventas medias"
    else:
        return "ventas bajas"


def format_money(amount):
    """
    Formatea un monto como moneda.
    """
    return f"${amount:,.2f}"


def create_seller_record(name, sales):
    """
    Crea un registro de vendedor utilizando un diccionario.
    """
    return {
        "nombre por favor: ": name,
        "ventas realizadas: ": sales
    }
    
    #hjhjj