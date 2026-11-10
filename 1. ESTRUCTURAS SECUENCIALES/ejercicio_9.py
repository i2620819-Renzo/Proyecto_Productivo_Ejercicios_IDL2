"""Cuanto pagaría un cliente por una compra con descuento y cuanto sería 
el cambio que recibiría en un pago en efectivo. Ingresar el monto base, 
el porcentaje de descuento y el con cuánto dinero está pagando el 
cliente. """

# SUPONIENDO QUE UN CLIENTE REALIZA UNA COMPRA DE S/ 200.00 RECIBE UN DESCUENTO DEL 10% Y PAGA CON S/250.00 EN EFECTIVO

# Programa para calcular descuento y cambio de una compra

# Entrada de datos
monto_base = float(input("Ingrese el monto de la compra: S/ "))
porcentaje_descuento = float(input("Ingrese el descuento (%): "))
pago_cliente = float(input("Ingrese el efectivo recibido: S/ "))

# Validar los datos ingresados
if monto_base >= 0 and 0 <= porcentaje_descuento <= 100 and pago_cliente >= 0:

    # Calcular el descuento
    descuento = monto_base * porcentaje_descuento / 100

    # Calcular el total a pagar
    total_pagar = monto_base - descuento

    # Mostrar el descuento y el total
    print("Descuento: S/", round(descuento, 2))
    print("Total a pagar: S/", round(total_pagar, 2))

    # Verificar si el pago es suficiente
    if pago_cliente >= total_pagar:

        # Calcular el cambio
        cambio = pago_cliente - total_pagar
        print("Cambio del cliente: S/", round(cambio, 2))
    else:
        faltante = total_pagar - pago_cliente
        print("Pago insuficiente. Falta: S/", round(faltante, 2))
else:
    print("Error: datos no válidos")