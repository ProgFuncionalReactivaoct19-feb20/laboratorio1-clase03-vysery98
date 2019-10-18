"""
	@vysery98

	Problema 1:

	Dado el siguiente conjunto de promedios de estudiantes; determinar los estudiantes que pasan de ciclo.
	Todos los estudiantes que pasan de ciclo son aquellos que tienen un promedio de 16.5 o mayor.

	promedios.txt
"""

# Se abre el documento promedios.txt: "r" - read
documento = open("promedios.txt", "r")

# Lee el contenido del archivo y lo lee
promedios = documento.read()

# Se los presenta como lista, segun el separador ","
promedios = promedios.split(",")

print(promedios)

documento.close()