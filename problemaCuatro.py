"""
	@vysery98

	Problema 4:

	Dado el siguiente listado:

	notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

	Filtrar aquellos que tiene la calificación cualitativa "Regular o Bueno"
"""

notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

# Arreglo donde se van a ingresar aquellos con la calificacion Regular o Bueno
notas_filtradas = []

# Recorre todas las posiciones del arreglo
for x in notas:
	
	# La posicion 3 del arreglo se va a comparar y seran validos solo aquellos  con la calificacion Regular o Bueno
	if x[3] == "Regular" or x[3] == "Bueno":

		# Se ingresa la tupla a notas_filtradas se cumple con la condicion
		notas_filtradas.append(x)

# Salida
print(notas_filtradas)