"""Ejercicio 7. Calcular el factorial de dos números
Objetivo: Pedir dos números, calcular el factorial de cada uno y determinar hasta qué factor coinciden sus multiplicaciones.

El factorial consiste en multiplicar todos los números enteros positivos desde 1 hasta el número elegido.

Por ejemplo:
\[
5!=1\times2\times3\times4\times5=120

\]"""

# Creamos una función para calcular el factorial.
def calcular_factorial(numero):

    # Empezamos el resultado en 1 porque
    # multiplicar por 1 no cambia el valor.
    resultado = 1

    # Creamos una lista para guardar los factores.
    factores = []

    # Recorremos los números desde 1 hasta el indicado.
    for i in range(1, numero + 1):

        # Multiplicamos cada número.
        resultado = resultado * i

        # Guardamos el factor como texto.
        factores.append(str(i))

    # Unimos los factores con el símbolo de multiplicación.
    operacion = " x ".join(factores)

    # Para cero factorial, el resultado es 1.
    if numero == 0:
        operacion = "1"

    # Devolvemos el factorial y su operación.
    return resultado, operacion


# Pedimos los dos números.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Comprobamos que ambos números sean válidos.
if num1 >= 0 and num2 >= 0:

    # Calculamos el factorial del primer número.
    factorial1, operacion1 = calcular_factorial(num1)

    # Calculamos el factorial del segundo número.
    factorial2, operacion2 = calcular_factorial(num2)

    # Mostramos las multiplicaciones y sus resultados.
    print(f"{num1}! = {operacion1} = {factorial1}")
    print(f"{num2}! = {operacion2} = {factorial2}")

    # Identificamos el último factor que comparten.
    coincidencia = min(num1, num2)

    # Mostramos hasta dónde coinciden.
    print("Coinciden hasta el factor:", coincidencia)

else:
    print("Error: los números no pueden ser negativos.")

"""Explicación para principiantes:
- def permite crear una función, es decir, un conjunto de instrucciones que podemos reutilizar.
- return devuelve el resultado calculado por la función.
- min() identifica el menor de dos números.
- join() une varios textos utilizando un separador.
Conclusión: Aprendemos a utilizar funciones para evitar repetir código y a emplear ciclos para realizar multiplicaciones sucesivas."""

