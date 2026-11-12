"""Ejercicio 10. Análisis de notas de estudiantes
Objetivo: Registrar las calificaciones de entre 5 y 20 estudiantes y calcular once resultados, incluyendo notas máximas, mínimas, promedios, aprobados y desaprobados.

Para este ejercicio utilizaremos notas enteras de 0 a 20, porque también debemos contar cuántas notas son pares e impares. La nota mínima aprobatoria es 13."""

# PROGRAMA PARA ANALIZAR LAS NOTAS DE UN SALÓN

# Pedimos la cantidad de estudiantes.
n = int(input("Ingrese la cantidad de estudiantes (5 a 20): "))

# Comprobamos que la cantidad esté entre 5 y 20.
while n < 5 or n > 20:
    print("Error: debe ingresar entre 5 y 20 estudiantes.")
    n = int(input("Ingrese nuevamente la cantidad: "))

# Creamos una lista vacía para guardar las notas.
notas = []

# Repetimos el ingreso según la cantidad de estudiantes.
for i in range(n):

    # Pedimos la nota del estudiante.
    nota = int(input(f"Ingrese la nota del estudiante {i + 1}: "))

    # Verificamos que la nota esté entre 0 y 20.
    while nota < 0 or nota > 20:
        print("Error: la nota debe estar entre 0 y 20.")
        nota = int(input("Ingrese nuevamente la nota: "))

    # Guardamos la nota en la lista.
    notas.append(nota)


# A. Encontramos la nota más alta.
mayor_nota = max(notas)

# B. Encontramos la nota más baja.
menor_nota = min(notas)

# C. Contamos cuántos alumnos tienen la nota más alta.
cantidad_mayor = notas.count(mayor_nota)

# D. Contamos cuántos alumnos tienen la nota más baja.
cantidad_menor = notas.count(menor_nota)

# E. Sumamos todas las notas y calculamos el promedio.
promedio = sum(notas) / n


# Creamos contadores para clasificar las notas.
pares = 0
impares = 0
aprobados = 0
desaprobados = 0

# Recorremos cada nota de la lista.
for nota in notas:

    # F. Comprobamos si la nota es par.
    if nota % 2 == 0:
        pares += 1

    # G. Si no es par, entonces es impar.
    else:
        impares += 1

    # H. Si la nota es 13 o más, está aprobado.
    if nota >= 13:
        aprobados += 1

    # I. Si la nota es menor de 13, está desaprobado.
    else:
        desaprobados += 1


# J. Calculamos el porcentaje de aprobados.
porcentaje_aprobados = (aprobados / n) * 100

# K. Calculamos el porcentaje de desaprobados.
porcentaje_desaprobados = (desaprobados / n) * 100


# MOSTRAMOS TODOS LOS RESULTADOS.

print("\n=== RESULTADOS DEL SALÓN ===")

print("a) Mayor nota:", mayor_nota)
print("b) Menor nota:", menor_nota)
print("c) Alumnos con la mayor nota:", cantidad_mayor)
print("d) Alumnos con la menor nota:", cantidad_menor)
print("e) Promedio del salón:", round(promedio, 2))
print("f) Cantidad de notas pares:", pares)
print("g) Cantidad de notas impares:", impares)
print("h) Alumnos aprobados:", aprobados)
print("i) Alumnos desaprobados:", desaprobados)
print("j) Porcentaje de aprobados:", porcentaje_aprobados, "%")
print("k) Porcentaje de desaprobados:", porcentaje_desaprobados, "%")

"""Código	Explicación sencilla
notas = []	Crea una lista vacía para guardar calificaciones.
append()	Agrega una nota a la lista.
max()	Encuentra la nota más alta.
min()	Encuentra la nota más baja.
count()	Cuenta cuántas veces aparece una nota.
sum()	Suma todas las notas.
len()	Cuenta cuántos elementos tiene una lista.
while	Repite instrucciones mientras se cumpla una condición.
for	Recorre los elementos de una lista.
round()	Redondea los resultados decimales."""