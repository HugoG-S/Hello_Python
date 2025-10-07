### Error Types ###
##               ##
#                 #

# SyntaxError
#print "Hola comunidad!"
print("Hola Comunidad!")


# NameError - No declarar variables y usarlas en un print por ejemplo
#print(name)
name = "Reshi"
print(name)


# IndexError - Da error si intentamos acceder a una posición que está fuera de rango.
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
#print(my_list[5]) 

# ModuleNotFoundError - Importación erronea de un módulo
#import mathS
import math

# AttributeError - Mala implementación de atributo de módulo
#print(math.PI)
print(math.pi)

# KeyError - Error de sintaxis en la clave del diccionario
my_dict = {"Nombre":"Hugo", "Nickname":"Reshi", "Edad":34, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"])

# TypeError - Acceder por un error de tipo a algo, en este caso, es una lista y no tiene clave/valor que es como se intenta acceder
#print(my_list["Nombre"])


# ImportError - Importar mal la librería del módulo, en este caso pi
#from math import PI
from math import pi
print(pi)


# ValueError - 
#my_int = int("10 Años")
my_int = int("10")
print(type(my_int))

# ZeroDivisionError - Dividir entre 0
#print(4/0)
print(4/2)