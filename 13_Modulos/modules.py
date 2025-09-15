### Modules ###
## Son Librerías
#
# Importamos el módulo
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")

# Importamos las funciones del módulo

from my_module import sumValue, printValue

sumValue(5, 3, 1)
printValue("Hola Python!")

# Módulos del sistema

import math, random

print(math.pi)
print(math.pow(2, 8))

print(random.randint(1, 100))

# Podemos "renombrar" como llamamos a la función

from math import pi as PI_VALUE

print(PI_VALUE)