""" Cada ejercicio debe de tener
1. Enuncia
2. Analisis
3. Psedocodigo
4. Diagrama de flujo
5. Prueba en escritorio
"""
#============================================================
"""1. Determina la velocidad final de un auto si su velocidad inicial es 0 km/h
y su aceleración es 0.8 m/s2; y el tiempo transcurrido es de 30 segundos."""
#DESARROLLO.
# 1. PROGRAMA PARA CALCULAR LA VELOCIDAD FINAL DEL AUTO.
# DATOS DE ENTRADA.
velocidad_inicial = 0   # metros por segundo m/s
aceleracion = 0.8       # metros por segundo m/s
tiempo = 30             # metros en segundo

# 2. CALCULAR LA VELOCIDAD FINAL
velocidad_final = velocidad_inicial + (aceleracion * tiempo)
"""
1 km = 1000 netros
1 hora = 3600 segundos
al transformar  unidades se relacionan las fracciones
3600/1000 = 3.6 ms  --- Indica cuántos km/h equivalen a 1 m/s (es decir, 1 m/s == a 3.6 km/h
"""
# 3. CONVERTIR LA VELOCIDAD  DE M/S A KM/H
velocidadfinalkh = velocidad_final * 3.6

# MOSTRAR RESULTADO.
print("Velocidad final en m/s", velocidad_final)
print("Velocidad final en km/h", velocidadfinalkh)

 # CONCLUSION 
"""7. Conclusión
Se determinó que un automóvil que parte del reposo y mantiene una aceleración constante de 0.8 m/s² 
durante 30 segundos alcanza una velocidad final de 24 m/s, equivalente a 86.4 km/h.
Mediante el seudocódigo, el diagrama de flujo, la prueba de escritorio y la implementación
 en Python, se demuestra que el algoritmo permite resolver correctamente el problema planteado."""




