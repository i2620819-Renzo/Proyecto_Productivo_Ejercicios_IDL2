"""Se necesita saber la cantidad de dinero que un cajero automático debe 
proporcionar en diferentes denominaciones, teniendo en cuenta que el 
usuario debe ingresar la cantidad a retirar y el cajero tiene disponible las 
siguientes denominaciones de dinero: 200, 100, 50, 20, 10, 5, 1. Se debe 
buscar entregar la menor cantidad de dinero por parte del cajero. """

# Programa para distribuir dinero en un cajero automático

# Entrada de datos
monto = int(input("Ingrese el monto a retirar: S/ "))

if monto > 0:

    # Billetes de S/ 200
    b200 = monto // 200
    resto = monto % 200

    # Billetes de S/ 100
    b100 = resto // 100
    resto = resto % 100

    # Billetes de S/ 50
    b50 = resto // 50
    resto = resto % 50

    # Billetes de S/ 20
    b20 = resto // 20
    resto = resto % 20

    # Billetes de S/ 10
    b10 = resto // 10
    resto = resto % 10

    # Monedas de S/ 5
    m5 = resto // 5
    resto = resto % 5

    # Monedas de S/ 1
    m1 = resto // 1

    # Calcular la cantidad total de piezas
    total_piezas = b200 + b100 + b50 + b20 + b10 + m5 + m1

    # Mostrar los resultados
    print("Billetes de S/ 200:", b200)
    print("Billetes de S/ 100:", b100)
    print("Billetes de S/ 50:", b50)
    print("Billetes de S/ 20:", b20)
    print("Billetes de S/ 10:", b10)
    print("Monedas de S/ 5:", m5)
    print("Monedas de S/ 1:", m1)
    print("Total de piezas:", total_piezas)

else:
    print("Error: monto no válido")
