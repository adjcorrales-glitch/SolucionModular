# Caso 1: Gestión de ventas y comisiones
import validaciones
import calculos

"""
Una empresa comercial necesita una herramienta para calcular las comisiones de sus vendedores al finalizar el mes.

Cada vendedor registra el monto total de sus ventas. La empresa aplica diferentes porcentajes de comisión dependiendo
del nivel de ventas alcanzado. Además, algunos vendedores reciben un bono adicional cuando superan una meta mensual.
"""

def main():
    print("Sistema de Getión de Ventas y Comisiones")
    #Ingresar Datos

    #Relizar cálculos
    print(calculos.porcentage_of_commission())
    print(calculos.Total_of_the_Commission())
    print(calculos.calculate_bonus())
    print(calculos.sellers_total_of_the_commission())

    #Mostrar Resultados
    print(validaciones.ask_name())
