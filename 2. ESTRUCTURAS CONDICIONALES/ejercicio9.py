"""Permita calcular el total a pagar por la compra de N camisas. Si se
compran entre 1 a 4 camisas se aplica un descuento del 12.5%, si se
compra una cantidad comprendida entre 5 y 8 camisas se aplica un
descuento del 20% y si se compran cantidades mayores, se aplica un
descuento del 31.5% sobre el total de la compra. Debe imprimirse en
pantalla la compra final sin descuento, monto del descuento y la
compra con descuento """
# Supongamos que un cliente compra 6 camisas a S/ 50.00 cada una.

#Programa para calcular el total de una compra de camisas
#Entrada de datos
cantidad = int(input("Ingrese la cantidad de camisas: "))
precio = float(input("Ingrese el precio unitario: S/ "))
#Validar los datos
if cantidad >= 1 and precio > 0:
#Calcular el subtotal
    subtotal = cantidad * precio
#Determinar el porcentaje de descuento
