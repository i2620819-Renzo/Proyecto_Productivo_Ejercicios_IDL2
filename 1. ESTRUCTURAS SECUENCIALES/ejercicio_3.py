"""Tres personas deciden invertir su dinero para fundar una empresa. Cada
una de ellas invierte una cantidad distinta. Obtener el porcentaje que
cada uno invierte con respecto a la cantidad total invertida. """
#  A. PROGRAMA PARA CALCULAR EL PORCENTAJE DE INVERSION.
# ENTRADA DE DATOS
inversion1 = float(input("Insersion del socio 1: S/ "))
inversion2 = float(input("Insersion del socio 2: S/ "))
inversion3 = float(input("Insersion del socio 3: S/ "))

# B. CALCULAR EL CAPITAL TOTAL
total = inversion1 + inversion2 + inversion3

# C. VALIDAR LOS MONTOS
if total > 0 and min(inversion1, inversion2, inversion3) >=0:  # IF significa  si .... y  AND significa  y ...osea si cumplen 2 condiciones
   porcentaje1 = (inversion1/total) *100
   porcentaje2 = (inversion2/total) *100
   porcentaje3 = (inversion3/total) *100

   print("inversion total es", total )
   print("porcentaje socio 1:", round(porcentaje1,2), "%" )  # • Esta función toma la variable o el valor llamado porcentaje 1 y lo redondea a 2 posiciones decimales. Por ejemplo, si el valor original es 45.6789, lo convierte en 45.68. y agrega el % como texto
   print("porcentaje socio 2:", round(porcentaje2,2), "%" )
   print("porcentaje socio 2:", round(porcentaje3,2), "%" )

else:
   print("error: inversiones no validad")
   
# D. CONCLUSION 
"""Se desarrolló un algoritmo que permite calcular el porcentaje de participación de tres socios en la 
inversión inicial de una empresa.
Con los valores utilizados en el ejemplo, se determinó que el primer socio participa con el 20 %, 
el segundo con el 30 % y el tercero con el 50 %, representando conjuntamente el 100 % del capital invertido.
El seudocódigo, el diagrama de flujo, la prueba de escritorio y el programa en Python permiten comprobar
que el procedimiento es correcto."""