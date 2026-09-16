def get_sales_category(sales):
    """Devuelve la categoría de ventas según el monto alcanzado."""
    if sales >= 50000:
        return "Ventas superiores"
    elif sales >= 25000:
        return "Ventas altas"
    elif sales >= 10000:
        return "Ventas medias"
    else:
        return "Ventas bajas"


def format_money(amount):
    """Formatea un monto como moneda."""
    return f"${amount:,.2f}"


def create_seller_record(name, sales):
    """Crea un registro básico del vendedor utilizando un diccionario."""
    return {
        "name": name,
        "sales": sales
    }


def show_summary(name, sales, category, percentage, commission, bonus, total_income):
    """Muestra el resumen final de los resultados del vendedor."""
    print("\n===== RESUMEN DEL VENDEDOR =====")
    print("Nombre:", name)
    print("Ventas del mes:", format_money(sales))
    print("Categoría:", category)
    print("Porcentaje de comisión:", f"{percentage * 100:.0f}%")
    print("Valor de la comisión:", format_money(commission))
    print("Bono:", format_money(bonus))
    print("Ingreso total:", format_money(total_income))
