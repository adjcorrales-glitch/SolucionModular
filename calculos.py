# Aquí se define el porcentaje de comisión que corresponde según el monto de ventas.
def percentage_of_commission(sales):
    if sales >= 50000:
        return 0.10
    elif sales >= 25000:
        return 0.07
    elif sales >= 10000:
        return 0.05
    else:
        return 0.03


# Aquí se calcula el valor de la comisión del vendedor.
def total_of_the_commission(sales):
    percentage = percentage_of_commission(sales)
    commission = sales * percentage
    return commission


# Aquí se calcula el bono si el vendedor alcanza o supera la meta de 70000.
def calculate_bonus(sales):
    if sales >= 70000:
        bonus = 1500
    else:
        bonus = 0

    return bonus


# Aquí se calcula el ingreso total obtenido entre comisión y bono.
def sellers_total_income(commission, bonus):
    total_income = commission + bonus
    return total_income
