""" Un vendedor recibe su sueldo base más 25% extra por comisión de sus
ventas; el vendedor desea saber cuánto dinero recibirá por concepto de
comisiones por lastres ventas que realiza en el mes y el total que recibirá
en el mes tomando en cuenta sueldo base y comisiones"""
# PROGRAMA PARA CALCULAR EL SUELDO DE UN VENDEDOR
# ENTRADA DE DATOS

sueldo_base = float(input("Ingrese el sueldo base; S/ "))
venta1 = float(input("Ingrese la primera venta: S/ "))
venta2 = float(input("Ingrese la segunda venta: S/ "))
venta3 = float(input("Ingrese la tercera venta: S/ "))

# B. SUMAR LAS TRES VENTAS
total_ventas = venta1 + venta2 + venta3

# C. CALCULAR LA COMISION DEL 25%
comision = total_ventas * 0.25

# D. CALCULAR SUELDO TOTAL
sueldo_total = sueldo_base + comision

# E. SALIDA DEL RESULTADO
print("total de ventas: S/ ", total_ventas)
print("comision obtenida: S/ ", comision)
print("total sueldo mensual: S/ ", sueldo_total)

"""Conclusión
Se desarrolló un algoritmo que permite calcular la comisión y el sueldo mensual de un vendedor a partir de tres ventas realizadas.
Con los datos utilizados en el ejemplo, el vendedor obtiene una comisión de S/ 1,500, equivalente al 25 % de sus ventas, y un sueldo total mensual de S/ 3,000.
El seudocódigo, el diagrama de flujo, la prueba de escritorio y el programa en Python permiten comprobar que el procedimiento funciona correctamente
"""