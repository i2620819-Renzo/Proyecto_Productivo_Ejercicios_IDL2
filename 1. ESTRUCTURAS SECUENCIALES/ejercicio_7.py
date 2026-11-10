"""Un estacionamiento requiere determinar el cobro que debe aplicar a las 
personas que lo utilizan. Considere que el cobro es con base en las 
horas que lo disponen y que las fracciones de hora se toman como 
completas y realice un programa que permita determinar el cobro. El 
pago por hora es de S/5.00 y el pago por los minutos restantes de S/0.10 
por minuto."""

# A. PROGRAMA PARA CALCULAR EL COBRO DE UN ESTACIONAMIENTO
# ENTRADA DE DATOS
horas = int(input("Ingrese las horas utilizadas: "))
minutos = int(input("Ingrese los minutos adicinales: "))

# B. TARIFAS DEL ESTACIONAMIENTO
tarifa_hora = 5.00
tarifa_minutos = 0.10

# C. VALIDAR EL TIEMPO INGRESADO
if horas >= 0 and 0 <= minutos < 60 and (horas + minutos) > 0:

# Calcular el costo de las horas
    costo_horas = horas * tarifa_hora

    # Calcular el costo de los minutos
    costo_minutos = minutos * tarifa_minutos

    # Calcular el total a pagar
    total_pagar = costo_horas + costo_minutos

    # Mostrar los resultados
    print("Costo por horas: S/", round(costo_horas, 2))
    print("Costo por minutos: S/", round(costo_minutos, 2))
    print("Total a pagar: S/", round(total_pagar, 2))
else:
    print("Error: tiempo no válido")

