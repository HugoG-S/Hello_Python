### Python Package Manager ###
##

# PIP - Gestor de paquetes de Python
# Para instalar paquetes desde terminal: python3 -m pip install "SomeProject"

import numpy # python3 -m pip install "numpy"

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array * 2)


import pandas # python3 -m pip install "pandas"

# pip list - Lista de los módulos instalados - python3 -m pip list

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1,4))