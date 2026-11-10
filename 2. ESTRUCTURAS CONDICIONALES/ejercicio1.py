"""Calcular el total que una persona debe pagar en una llantera, si el
precio de cada llanta es de S/150 si se compran menos de 5 llantas y
de S/120 si se compran 5 o más."""
# A. PROGRAMA PARA CALCULAR COSTO DE LA COMPRA DE LLANTAS
#INGRESAR DATOS
cantidad = int(input("Ingrese la cantidad de llantas; "))

# B. VALIDAR CANTIDAD INGRESADA.
if cantidad > 0 :               #dice, si cantidad es mayor a 0 y si cantidad es menor a 5  entocnes precio es de 150
    if cantidad < 5:
        precio = 150
    else:                       # de lo contrario precio es 120 quiere decir q si cantidad es mayore a 5 sera 120 el precio
        precio = 120
    
    total = cantidad * precio
    print("precio de la llanta es S/ ", precio)
    print("total a pagar es S/ ", total)

else:
    print("Error: cantidad no valida ")

"""Conclusión
Se desarrolló un algoritmo que permite calcular el costo total de compra de llantas aplicando una estructura condicional para determinar el precio unitario.
Se comprobó que, al comprar menos de 5 llantas, el precio unitario es S/ 150.00, mientras que al comprar 5 o más, se aplica el precio especial de S/ 120.00.
Para una compra de 6 llantas, el cliente deberá pagar S/ 720.00.
El seudocódigo, el diagrama de flujo, la prueba de escritorio y el programa en Python permiten verificar el correcto funcionamiento del algoritmo y la aplicación de las condiciones establecidas."""

