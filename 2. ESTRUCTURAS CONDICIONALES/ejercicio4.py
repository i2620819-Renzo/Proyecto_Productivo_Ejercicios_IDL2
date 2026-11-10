""" En una escuela la colegiatura de los alumnos se determina según el
número de materias que cursan (Solicitar al usuario). El costo de
todas las materias es el mismo S/100. Se ha establecido un programa
para estimular a los alumnos, el cual consiste en lo siguiente: si el
promedio obtenido por un alumno en el último periodo es mayor o
igual que 18, se le hará un descuento del 50% sobre la mitad de los
cursos; si el promedio obtenido es menor que 18 deberá pagar la
colegiatura completa. Obtener cuanto debe pagar un alumno."""
# Programa para calcular la colegiatura de un alumno

# Entrada de datos
materias = int(input("Ingrese la cantidad de materias: "))
promedio = float(input("Ingrese el promedio del alumno: "))

# Validar los datos
if materias > 0 and 0 <= promedio <= 20:

    # Calcular el costo de todas las materias
    costo_total = materias * 100

    # Evaluar si corresponde el descuento
    if promedio >= 18:
        descuento = (costo_total / 2) * 0.50
    else:
        descuento = 0

    # Calcular el importe final
    total_pagar = costo_total - descuento

    # Mostrar los resultados
    print("Costo total: S/", costo_total)
    print("Descuento: S/", descuento)
    print("Total a pagar: S/", total_pagar)

else:
    print("Error: datos no válidos")
