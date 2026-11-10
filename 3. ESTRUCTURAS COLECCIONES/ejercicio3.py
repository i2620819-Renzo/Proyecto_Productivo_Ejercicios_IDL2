"""Para tributar un determinado impuesto se debe ser mayor de 18 años
y tener unos ingresos iguales o superiores a S/3000 mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos
mensuales y muestre por pantalla si el usuario tiene que tributar o no
y mostrar el monto a tributar que siempre es el 5% del ingreso
mensual."""
# Supongamos que una persona tiene 25 años y percibe ingresos mensuales de S/ 4,000.

# Programa para determinar si una persona debe tributar

# Entrada de datos
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: S/ "))

# Evaluar las condiciones para tributar
if edad > 18 and ingresos >= 3000:

    # Calcular el impuesto del 5%
    impuesto = ingresos * 0.05

    # Mostrar los resultados
    print("Usted SI debe tributar")
    print("Impuesto a pagar: S/", impuesto)

else:
    impuesto = 0

    print("Usted NO debe tributar")
    print("Impuesto a pagar: S/", impuesto)

"""Conclusión
Se desarrolló un algoritmo que permite determinar si una persona está obligada a tributar según su edad y sus ingresos mensuales.
Se comprobó que, para cumplir las condiciones del ejercicio, la persona debe tener más de 18 años y percibir ingresos iguales o superiores a S/ 3,000 mensuales.
Con el ejemplo de una persona de 25 años que gana S/ 4,000 mensuales, se obtuvo un impuesto de S/ 200.00, equivalente al 5 % de sus ingresos.
El seudocódigo, el diagrama de flujo, la prueba de escritorio y el programa en Python permiten verificar el correcto funcionamiento del algoritmo mediante estructuras condicionales."""