"""
	@vysery98

	Problema 5:

	Dadas las siguientes edad:

	[10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

	Se ha generado una lista denominada black_edades, formada así:

	[10, 14, 30, 32, 40, 16]

	Generar el listado de edades que no estén dentro de las black_edades.
"""

edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

# Metodo para comparar las edades
def edades_validas (x):

	# Lista de edades que no van a ser validas
	black_edades = [10, 14, 30, 32, 40, 16]
	
	# Comparacion de los numeros del arreglo "edades" que sean igual a cualquiera de los valores del arreglo "black_edades"
	if x in black_edades:
		return False
	else:
		return True

# Unicamente se filtran aquellos que no sean iguales a los numeros del segundo arreglo, el resultado de la comparacion debe ser igual a True y se presentan
print(list(filter(edades_validas, edades)))