"""
	@vysery98

	Problema 2:

	Dada la siguiente lista:

	notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

	Encontrar una lista como sigue:

	[20, 16, 20, 15]
"""

notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

# Se asigna valores a las variables valor según la posición de la cadena que ingrese
valorUno = lambda x: x[0]
valorDos = lambda x: x[1]
valorTres = lambda x: x[2]

# Se suma los tres valores determinados previamente del arreglo
suma = lambda x: (valorUno(x) + valorDos(x) + valorTres(x))

# Se realiza la operacion indicada en suma de la funcion anonima lambda, enviando los datos del arreglo "notas" y se presentan en lista
print(list(map(suma, notas)))