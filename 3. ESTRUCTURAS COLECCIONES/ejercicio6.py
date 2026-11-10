"""Elabore un programa que lea la hora (HH MM SS) y muestre por
pantalla la hora N segundos después."""
# Supongamos que la hora inicial es 14:35:50 y deseamos conocer qué hora será después de 90 segundos.

# Programa para calcular la hora después de N segundos

# Entrada de datos
HH = int(input("Ingrese la hora (HH): "))
MM = int(input("Ingrese los minutos (MM): "))
SS = int(input("Ingrese los segundos (SS): "))
N = int(input("Ingrese los segundos adicionales: "))

# Validar los datos
if (0 <= HH <= 23 and
    0 <= MM <= 59 and
    0 <= SS <= 59 and
    N >= 0):

    # Convertir la hora inicial a segundos
    total_segundos = HH * 3600 + MM * 60 + SS

    # Sumar los segundos adicionales
    nuevo_total = total_segundos + N

    # Ajustar al reloj de 24 horas
    segundos_dia = nuevo_total % 86400

    # Convertir nuevamente a horas, minutos y segundos
    hora_final = segundos_dia // 3600
    minuto_final = (segundos_dia % 3600) // 60
    segundo_final = segundos_dia % 60

    # Mostrar la hora en formato HH:MM:SS
    print(f"Hora resultante: {hora_final:02d}:{minuto_final:02d}:{segundo_final:02d}")

else:
    print("Error: datos no válidos")

"""Conclusión
Se desarrolló un algoritmo que permite calcular la hora resultante después de agregar una cantidad N de segundos a una hora inicial.
Se comprobó que, al ingresar la hora 14:35:50 y agregar 90 segundos, el resultado es 14:37:20.
Asimismo, el algoritmo considera correctamente el cambio de día cuando el tiempo supera las 23:59:59, utilizando el operador módulo para mantener el formato de 24 horas.
El seudocódigo, el diagrama de flujo, la prueba de escritorio y el programa en Python permiten verificar el funcionamiento del algoritmo mediante operaciones aritméticas y estructuras condicionales."""