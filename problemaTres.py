"""
	@vysery98

	Problema 3:

	Dada la siguiente frase:

	"No hay medicina que cure lo que no cura la felicidad"

	Encuentre el listado que sigue:

	["No", "hay", "que", "lo", "que", "no", "la"]
"""

frase = "No hay medicina que cure lo que no cura la felicidad"

def palabras_validas (x):

	# el tamaño de lo que reciba la funcion palabras_validas debe ser menor a 3
	if len(x) <= 3:
		return True
	else:
		return False

# Se presenta unicamente las palabras que cumplan con la condicion que sea menor a 3
resultado = filter(palabras_validas, frase.split(" "))

# .split(" ") separa el contenido de la frase segun el separador " "
print(list(resultado))
