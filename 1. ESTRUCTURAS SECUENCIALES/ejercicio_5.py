"""Suponga que un individuo desea invertir su capital en un banco y desea
saber cuánto dinero ganará después de un año si el banco paga a razón
de 2% mensual."""
# A. PROGRAMA PARA CALCULAAR INTERESES BANCARIOS
# ENTRADA DE DATOS

capital = float(input("Ingrese el capital a invertir: S/ "))

# B. DATOS ESTABLECIDOS.
tasa = 0.02 # intereses mensual son el 2 % segun enunciado
tiempo = 12 # un año tiene 12 meses segun enunciado

# C. CALCULAR LOS INTERESES
intereses = capital * tasa * tiempo

# D. CALCULAR EL MONTO TOTAL.
monto_total = capital + intereses

# MOSTRAR RESULTADOS
print("Intereses ganado: S/ ", intereses)
print("Monto total despues de un año: S/ ", monto_total)

"""Conclusión
Se desarrolló un algoritmo que permite calcular la ganancia generada por una inversión bancaria utilizando una tasa de interés simple del 2 % mensual durante un año.
Con un capital inicial de S/ 10,000, la persona obtiene una ganancia de S/ 2,400 en intereses y un monto total de S/ 12,400 al finalizar los 12 meses.
El seudocódigo, el diagrama de flujo, la prueba de escritorio y el código Python permiten comprobar el correcto funcionamiento del algoritmo.
Nota: Si el banco capitalizara los intereses cada mes (interés compuesto), el resultado sería diferente. En este ejercicio se ha considerado interés simple."""
