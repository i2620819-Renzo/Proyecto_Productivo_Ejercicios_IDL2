"""Determinar mediante el ingreso de los 3 lados de un triángulo, si este
es Equilátero (Mostrar el perímetro del), Isósceles (Indicar que lados
son Iguales) o Escaleno (triángulo mostrar el área del triángulo)."""

import math

# Ingreso de los tres lados
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

# Validar que se pueda formar un triángulo
if (lado1 > 0 and lado2 > 0 and lado3 > 0 and
    lado1 + lado2 > lado3 and
    lado1 + lado3 > lado2 and
    lado2 + lado3 > lado1):

    # Verificar si es equilátero
    if lado1 == lado2 and lado2 == lado3:
        perimetro = lado1 + lado2 + lado3

        print("El triángulo es EQUILÁTERO")
        print("Perímetro:", round(perimetro, 2))

    # Verificar si es isósceles
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es ISÓSCELES")

        if lado1 == lado2:
            print("Los lados iguales son: 1 y 2")
        elif lado1 == lado3:
            print("Los lados iguales son: 1 y 3")
        else:
            print("Los lados iguales son: 2 y 3")

    # Si los tres lados son diferentes, es escaleno
    else:
        s = (lado1 + lado2 + lado3) / 2

        area = math.sqrt(
            s * (s - lado1) *
            (s - lado2) * (s - lado3)
        )

        print("El triángulo es ESCALENO")
        print("Área:", round(area, 2))

else:
    print("No es un triángulo válido")
