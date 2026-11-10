""" Realice un programa que representen el algoritmo donde se ingrese la
edad de un apersona para determinar aproximadamente cuántos
meses, semanas, días y horas ha vivido una persona."""
# PROGRAMA PARA CALCULAR EL TIEMPO VIVIDO DE UNA PERSONA
# ENTRADA DE DATOS
edad = int(input("Ingrese la edad de la persona: "))

# CALCULAR TIEMPOR VIVIDO.
meses = edad * 12
semanas = edad * 52
dias = edad * 365
horas = dias * 24

# SALIDA DE RESULTADOS.
print("meses vividos: ", meses)
print("semanas vividos: ", semanas)
print("dias vividos: ", dias)
print("horas vividos: ", horas) 

"""Conclusión
Se desarrolló un algoritmo que permite calcular aproximadamente los meses, semanas, días y horas que ha vivido una persona, utilizando su edad expresada en años.
Para una persona de 20 años, se obtuvo un resultado aproximado de 240 meses, 1,040 semanas, 7,300 días y 175,200 horas.
El seudocódigo, el diagrama de flujo, la prueba de escritorio y el programa en Python permiten comprobar el correcto funcionamiento del algoritmo.
Nota: Los resultados son aproximados porque no se consideran los años bisiestos, los meses de diferente duración ni los días transcurridos desde el último cumpleaños. Además, para las semanas se utiliza la aproximación de 52 semanas por año."""