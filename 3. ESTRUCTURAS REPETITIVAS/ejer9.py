"""Ejercicio 9. Producto de números utilizando arrays
Objetivo: Calcular el producto de la secuencia 100 × 98 × 96 × 94 × ..., utilizando un arreglo o lista.

El enunciado termina en 1, aunque al comenzar en 100 y disminuir de dos en dos se llega a 2. Para conservar el patrón, multiplicaremos los números pares desde 100 hasta 2."""

# Creamos una lista vacía para guardar los números.
numeros = []

# Recorremos los números pares desde 100 hasta 2.
# El -2 indica que disminuimos de dos en dos.
for numero in range(100, 0, -2):

    # Guardamos cada número en la lista.
    numeros.append(numero)

# Creamos una variable para guardar el producto.
producto = 1

# Recorremos todos los números guardados.
for numero in numeros:

    # Multiplicamos cada número por el producto acumulado.
    producto = producto * numero

# Mostramos la lista utilizada.
print("Números del arreglo:")
print(numeros)

# Mostramos la cantidad de números.
print("Cantidad de elementos:", len(numeros))

# Mostramos el producto final.
print("Producto total:", producto)

"""En el ejercicio original se multiplican 50 números pares, por lo que el resultado es mucho mayor.

Para principiantes: Una lista permite guardar varios valores en una sola variable. append() agrega elementos y el ciclo for permite recorrerlos para realizar operaciones."""

