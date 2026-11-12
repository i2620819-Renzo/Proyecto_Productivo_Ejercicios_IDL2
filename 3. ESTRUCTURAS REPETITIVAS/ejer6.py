"""Ejercicio 6. Crear un cronómetro en Python
Objetivo: Desarrollar un programa que muestre un cronómetro con horas, minutos y segundos (hh:mm:ss).

El ejercicio indica que el cronómetro será referencial, por lo que no necesitamos que funcione con la precisión de un reloj real."""

# Importamos una herramienta que permite hacer pausas.
import time

# Pedimos cuántos segundos durará el cronómetro.
duracion = int(input("Ingrese la duración en segundos: "))

# Comprobamos que el tiempo no sea negativo.
if duracion >= 0:

    # Repetimos el conteo desde cero hasta la duración.
    for segundo_total in range(duracion + 1):

        # Calculamos las horas completas.
        horas = segundo_total // 3600

        # Calculamos los minutos restantes.
        minutos = (segundo_total % 3600) // 60

        # Calculamos los segundos restantes.
        segundos = segundo_total % 60

        # Mostramos el tiempo con dos dígitos.
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

        # Esperamos aproximadamente un segundo.
        # No hacemos pausa después del último valor.
        if segundo_total < duracion:
            time.sleep(1)

else:
    print("Error: el tiempo no puede ser negativo.")

"""Explicación de las instrucciones:
Código	¿Qué significa?
import time	Permite utilizar funciones relacionadas con el tiempo.
range()	Genera una secuencia de números.
//	Realiza una división y obtiene la parte entera.
%	Obtiene el residuo de una división.
time.sleep(1)	Pausa el programa aproximadamente un segundo.
:02d	Muestra un número entero con al menos dos dígitos.

Conclusión: Este ejercicio nos enseña cómo utilizar un ciclo repetitivo para contar el tiempo y convertir segundos en horas, minutos y segundos."""

