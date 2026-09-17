# Caso 1: Gestión de ventas y comisiones
"""
Una empresa comercial necesita una herramienta para calcular las comisiones
 de sus vendedores al finalizar el mes.

Cada vendedor registra el monto total de sus ventas. La empresa aplica
 diferentes porcentajes de comisión dependiendo del nivel de ventas alcanzado.
Además, algunos vendedores reciben un bono adicional cuando superan una meta
 mensual.
"""

import validaciones
import calculos
import operaciones


def main():
    print("===== Sistema de Gestión de Ventas y Comisiones =====")

    # Ingresar y validar datos del vendedor.
    name = validaciones.ask_name()
    sales = validaciones.ask_sale()

    # Registrar los datos básicos del vendedor.
    seller = operaciones.create_seller_record(name, sales)

    # Realizar cálculos.
    percentage = calculos.percentage_of_commission(seller["sales"])
    commission = calculos.total_of_the_commission(seller["sales"])
    bonus = calculos.calculate_bonus(seller["sales"])
    total_income = calculos.sellers_total_income(commission, bonus)

    # Determinar la categoría de ventas.
    category = operaciones.get_sales_category(seller["sales"])

    # Mostrar resultados.
    operaciones.show_summary(
        seller["name"],
        seller["sales"],
        category,
        percentage,
        commission,
        bonus,
        total_income
    )


if __name__ == "__main__":
    main()
