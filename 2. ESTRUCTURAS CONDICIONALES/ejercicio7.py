"""Calcular el pago de una llamada, el cobro es por el tiempo que ésta
dura, de tal forma que los primeros cinco minutos cuestan S/ 1.00 c/u,
los siguientes tres, S/0.80 c/u, los siguientes dos minutos, S/0.70 c/u,
3
y a partir del décimo minuto, S/0.50 c/u. Además, se carga un
impuesto de 3 % cuando es domingo, y 5% si es domingo de turno
nocturno. Realice un algoritmo para determinar cuánto debe pagar
por cada concepto una persona que realiza una llamada. """
# Supongamos que una persona realiza una llamada de 12 minutos, un domingo en turno nocturno.

# Programa para calcular el costo de una llamada

# Entrada de datos
minutos = int(input("Duración de llamada (minutos): "))
domingo = input("¿Es domingo? (SI/NO): ").upper()
turno = input("Turno (DIURNO/NOCTURNO): ").upper()

if (minutos > 0 and
    domingo in ("SI", "NO") and
    turno in ("DIURNO", "NOCTURNO")):

    # Calcular los costos por tramo
    costo1 = min(minutos, 5) * 1.00
    costo2 = min(max(minutos - 5, 0), 3) * 0.80
    costo3 = min(max(minutos - 8, 0), 2) * 0.70
    costo4 = max(minutos - 10, 0) * 0.50

    # Calcular subtotal
    subtotal = costo1 + costo2 + costo3 + costo4

    # Determinar el impuesto
    if domingo == "SI":
        if turno == "NOCTURNO":
            tasa = 0.05
        else:
            tasa = 0.03
    else:
        tasa = 0

    impuesto = subtotal * tasa
    total = subtotal + impuesto

    # Mostrar los resultados
    print(f"Costo primeros 5 min: S/ {costo1:.2f}")
    print(f"Costo siguientes 3 min: S/ {costo2:.2f}")
    print(f"Costo siguientes 2 min: S/ {costo3:.2f}")
    print(f"Costo minutos restantes: S/ {costo4:.2f}")
    print(f"Subtotal: S/ {subtotal:.2f}")
    print(f"Impuesto: S/ {impuesto:.2f}")
    print(f"TOTAL A PAGAR: S/ {total:.2f}")

else:
    print("Error: datos no válidos")

"""Conclusión
Se desarrolló un algoritmo que permite calcular el costo de una llamada telefónica considerando las tarifas progresivas por minuto y los impuestos establecidos para los domingos.
Se comprobó que una llamada de 12 minutos realizada un domingo en turno nocturno tiene un costo de S/ 9.80, un impuesto de S/ 0.49 y un total a pagar de S/ 10.29.
El seudocódigo, el diagrama de flujo, la prueba de escritorio y el programa en Python demuestran cómo utilizar operaciones aritméticas y estructuras condicionales para resolver el problema."""