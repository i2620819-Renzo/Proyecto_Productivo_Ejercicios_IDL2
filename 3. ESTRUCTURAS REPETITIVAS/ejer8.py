"""Ejercicio 8. Registro de asistentes a una fiesta
Objetivo: Registrar las edades y sexos de los asistentes a una fiesta y calcular la cantidad de hombres, mujeres, sus promedios de edad y las edades máxima y mínima.

El programa debe permitir registrar por lo menos una persona y preguntar si deseamos continuar."""

# Creamos contadores para hombres y mujeres.
hombres = 0
mujeres = 0

# Creamos variables para sumar las edades.
suma_edades_hombres = 0
suma_edades_mujeres = 0

# Contador general de asistentes.
total_asistentes = 0

# Variables para guardar la edad mayor y menor.
edad_mayor = None
edad_menor = None

# Indicamos que inicialmente sí registraremos personas.
continuar = "s"

# Repetimos mientras el usuario desee continuar.
while continuar == "s":

    # Pedimos la edad del asistente.
    edad = int(input("Ingrese la edad: "))

    # Verificamos que la edad sea válida.
    while edad < 0:
        print("La edad no puede ser negativa.")
        edad = int(input("Ingrese nuevamente la edad: "))

    # Pedimos el sexo para la clasificación del ejercicio.
    sexo = input("Ingrese sexo (H/M): ").strip().upper()

    # Comprobamos que se ingrese H o M.
    while sexo not in ("H", "M"):
        print("Ingrese H para hombre o M para mujer.")
        sexo = input("Ingrese sexo (H/M): ").strip().upper()

    # Contamos a la persona registrada.
    total_asistentes += 1

    # Si es hombre, sumamos su edad al grupo de hombres.
    if sexo == "H":
        hombres += 1
        suma_edades_hombres += edad

    # Si es mujer, sumamos su edad al grupo de mujeres.
    else:
        mujeres += 1
        suma_edades_mujeres += edad

    # Actualizamos la edad mayor registrada.
    if edad_mayor is None or edad > edad_mayor:
        edad_mayor = edad

    # Actualizamos la edad menor registrada.
    if edad_menor is None or edad < edad_menor:
        edad_menor = edad

    # Preguntamos si desea registrar otra persona.
    continuar = input("¿Registrar otro asistente? (S/N): ").strip().lower()

    # Solo aceptamos S o N.
    while continuar not in ("s", "n"):
        continuar = input("Ingrese S o N: ").strip().lower()


# Calculamos el promedio de edad de los hombres.
if hombres > 0:
    promedio_hombres = suma_edades_hombres / hombres
else:
    promedio_hombres = None

# Calculamos el promedio de edad de las mujeres.
if mujeres > 0:
    promedio_mujeres = suma_edades_mujeres / mujeres
else:
    promedio_mujeres = None

# Mostramos el resumen de asistentes.
print("\n=== RESUMEN DE LA FIESTA ===")
print("Total de asistentes:", total_asistentes)
print("Cantidad de hombres:", hombres)
print("Cantidad de mujeres:", mujeres)

# Mostramos los promedios cuando hay personas en el grupo.
if promedio_hombres is not None:
    print("Promedio de edad de hombres:", round(promedio_hombres, 2))
else:
    print("No se registraron hombres.")

if promedio_mujeres is not None:
    print("Promedio de edad de mujeres:", round(promedio_mujeres, 2))
else:
    print("No se registraron mujeres.")

print("Edad de la persona mayor:", edad_mayor)
print("Edad de la persona menor:", edad_menor)

"""La persona menor tiene 20 años y la mayor tiene 40 años.

Para principiantes: while permite registrar varias personas sin conocer de antemano cuántas asistirán. Los contadores almacenan cantidades y los acumuladores guardan sumas."""