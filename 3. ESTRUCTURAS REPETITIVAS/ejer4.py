"""Ejercicio 4. Encontrar el número mayor y menor
Objetivo: Ingresar N números e identificar el valor máximo y mínimo."""

# Pedimos cuántos números se van a ingresar.
n = int(input("¿Cuántos números ingresará?: "))

if n > 0:

    # Pedimos el primer número.
    numero = float(input("Ingrese el número 1: "))

    # Al principio, consideramos que este número
    # es tanto el mayor como el menor.
    mayor = numero
    menor = numero

    # Pedimos los números restantes.
    for i in range(2, n + 1):

        numero = float(input(f"Ingrese el número {i}: "))

        # Si encontramos un número más grande,
        # actualizamos la variable mayor.
        if numero > mayor:
            mayor = numero

        # Si encontramos un número más pequeño,
        # actualizamos la variable menor.
        if numero < menor:
            menor = numero

    # Mostramos los resultados.
    print("El número mayor es:", mayor)
    print("El número menor es:", menor)

else:
    print("Error: N debe ser mayor que cero.")

"""Ejemplo: Para los números 15, 8, 25, 12, 4, el mayor es 25 y el menor es 4.

Para principiantes: Las variables mayor y menor funcionan como dos casillas donde guardamos los valores extremos que vamos encontrando."""