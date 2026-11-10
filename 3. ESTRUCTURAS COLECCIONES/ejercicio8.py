"""Solicite a usuario 3 números enteros (validar que sean diferentes) y
en que orden lo desean ver, para luego, mostrarlos a usuario, pero
ordenados de manera ascendente o descendente según los que
indique el usuario."""

# Programa para ordenar tres números enteros diferentes

# Solicitar los números hasta que sean diferentes
while True:                                                        # (El bucle infinito)
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    if num1 != num2 and num1 != num3 and num2 != num3:
        break                                                      # La instrucción break en Python es una palabra clave que se utiliza para terminar o romper un bucle de manera inmediata (for o while)
    else:
        print("Error: los números deben ser diferentes")

# Inicializar las variables
menor = num1
medio = num2
mayor = num3

# Ordenar mediante comparaciones
if menor > medio:
    menor, medio = medio, menor

if menor > mayor:
    menor, mayor = mayor, menor

if medio > mayor:
    medio, mayor = mayor, medio

# Solicitar el orden deseado
while True:
    print("1. Ascendente")
    print("2. Descendente")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1 or opcion == 2:
        break
    else:
        print("Opción no válida")

# Mostrar los resultados
if opcion == 1:
    print("Orden ascendente:", menor, medio, mayor)
else:
    print("Orden descendente:", mayor, medio, menor)