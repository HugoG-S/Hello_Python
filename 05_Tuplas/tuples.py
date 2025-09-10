### Tuples ###
# La diferencia con las listas es, que las tuplas son inmutables, constantes, no se pueden modificar

# Métodos de definir una tupla

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Hugo", "Reshi", "Hugo")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Hugo"))
print(my_tuple.index("Reshi"))          # index nos dice el indice del elemento dentro de la tupla

#my_tuple[1] = 1.80                     # Daría error al intentar modificarlo, puesto que las tuplas son inmutables


my_sum_tuple = my_tuple + my_other_tuple # Si podríamos concatenarlas
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)                # Convertimos la tupla en una lista

print(type(my_tuple))

my_tuple[4] = "ReshiDev"
my_tuple.insert(1, "Azul")

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
#print(my_tuple)        # NameError: name 'my_tuple' is not defined. No podemos eliminar elementos de la tupla ni la tupla en si