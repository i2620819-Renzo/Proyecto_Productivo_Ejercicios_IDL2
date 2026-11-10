"""2. Un estudiante realiza cuatro exámenes, los cuales tienen la misma
ponderación. Representen el algoritmo correspondiente para obtener el
promedio de las calificaciones obtenidas"""

# A. PROGRAMA PARA CALCULAR EL PROMEDIO DE4 EXAMENES.
# ENTRADA DE DATOS
nota1 = float(input("Ingrese la primera nota: ")) # float permite ingresar decimales y input es para q usuario ingrese lo solicitado
nota2 = float(input("Ingrese la segunda nota: ")) # float permite ingresar decimales y input es para q usuario ingrese lo solicitado
nota3 = float(input("Ingrese la tercera nota: ")) # float permite ingresar decimales y input es para q usuario ingrese lo solicitado
nota4 = float(input("Ingrese la cuarta nota: ")) # float permite ingresar decimales y input es para q usuario ingrese lo solicitado

# B. CALCULAR PROMEDIO
promedio = (nota1 + nota2 + nota3 + nota4)/4

# C. MOSTRAR RESULTADO
print("El promedio final es ", promedio)

# D. CONCLUSION 
"""Se desarrolló un algoritmo que permite calcular el promedio de cuatro exámenes con igual ponderación. Mediante 
la suma de las calificaciones y su división entre cuatro, se obtiene el promedio final del estudiante.
Con las notas utilizadas en el ejemplo (15, 17, 14 y 18), el resultado es 16, lo que demuestra el
 correcto funcionamiento del algoritmo, tanto en la prueba de escritorio como en su implementación en Python."""
