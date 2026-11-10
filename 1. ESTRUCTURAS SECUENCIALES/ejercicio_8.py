"""Una empresa constructora vende terrenos con la forma A de la figura. 
Obtener el área respectiva de un terreno de medidas ingresando el valor 
de los 3 lados."""
# A. PROGRAMA CALCULAR EL AREA DE UN TERRENO.
# ENTRADA DE DATOS.

A = float(input("Ingrese el lado A en metros: "))
B = float(input("Ingrese el lado B en metros: "))
C = float(input("Ingrese el lado C en metros: "))  

# B. CALCULAR AREA DEL RECTANGULO.
area_rectangulo = B*C

# C. CALCULAR AREA DEL TRIANGULO.
area_triangulo = (B * (A - C))/2

# D. CALCULAR EL AREA TOTAL DEL TERRENO.
area_total = area_rectangulo + area_triangulo

# E. MOSTRAR LOS RESULTADOS.
print("Área del rectángulo:", area_rectangulo, "m²")
print("Área del triángulo:", area_triangulo, "m²")
print("Área total del terreno:", area_total, "m²")