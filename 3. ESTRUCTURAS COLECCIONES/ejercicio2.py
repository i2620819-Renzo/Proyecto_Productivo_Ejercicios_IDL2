"""Cómo se podría determinar ¿Cuál de los 3 números brindados por
usuario es el menor y mayor de todos ellos?"""
 # Supongamos que el usuario ingresa los números 15, 8 y 25.

 # Programa para determinar el mayor y menor de 3 números

# Entrada de datos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Inicializar las variables
mayor = num1
menor = num1

# Comparar el segundo número
if num2 > mayor:               # SI num2 es mayor a num1 entonces
    mayor = num2

if num2 < menor:
    menor = num2

# Comparar el tercer número
if num3 > mayor:
    mayor = num3

if num3 < menor:
    menor = num3

# Mostrar los resultados
print("El número mayor es:", mayor)
print("El número menor es:", menor)