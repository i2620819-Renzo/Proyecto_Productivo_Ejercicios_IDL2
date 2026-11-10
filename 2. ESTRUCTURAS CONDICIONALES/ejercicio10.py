"""El costo de llamadas telefónicas internacionales depende de clave
(identifica a la zona geográfica) en la que se encuentra el destino y
del número de minutos hablados. En la siguiente tabla se presenta el
costo del minuto por zona. A cada zona se le ha asociado una clave.
Construya un diagrama de flujo que permita mostrar en nombre del
área y calcular e imprimir el costo total de una llamada y el nombre
de la zona a la cual llamó."""
"""10	América del norte	S/ 2.20
   12	América del centro	S/ 2.50
   20	América del sur	S/ 1.20
   22	Asia	S/ 3.50
   30	Europa	S/ 3.00
   32	África	S/ 3.20"""
# Supongamos que una persona realiza una llamada de 10 minutos a Europa (código 30).

# Programa para calcular llamadas internacionales

# Ingreso de datos
codigo = int(input("Ingrese el código de la zona: "))
minutos = float(input("Ingrese los minutos hablados: "))

# Inicializar variables
tarifa = 0
zona = "No válida"

# Identificar zona y tarifa
if codigo == 10:
    zona = "América del norte"
    tarifa = 2.20

elif codigo == 12:
    zona = "América del centro"
    tarifa = 2.50

elif codigo == 20:
    zona = "América del sur"
    tarifa = 1.20

elif codigo == 22:
    zona = "Asia"
    tarifa = 3.50

elif codigo == 30:
    zona = "Europa"
    tarifa = 3.00

elif codigo == 32:
    zona = "África"
    tarifa = 3.20

# Validar y calcular
if tarifa > 0 and minutos > 0:
    total = minutos * tarifa

    print("Zona geográfica:", zona)
    print(f"Costo por minuto: S/ {tarifa:.2f}")
    print(f"Total a pagar: S/ {total:.2f}")

else:
    print("Error: código o duración no válida")
