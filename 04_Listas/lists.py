### Lists ###

# Diferentes maneras de declarar una lista

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Hugo", "Reshi"]
print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[1])
print(my_other_list[-2])
print(my_other_list[-4]) 
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

print(my_other_list.count("Hugo"))  # count da el número de ocurrencias encontradas en la lista
print(my_list.count(30))            # Aquí nos está contando 2 veces el 30 definido en la lista

# Añadimos a las diferentes variables (siempre en el mismo orden) los datos de la lista

age, height, name, nickname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("ReshiDev")    # Con append añadimos un nuevo elemento, siempre al final
print(my_other_list)

my_other_list.insert(1, "Verde")    # Con insert añadimos un elemento en la posición que se le indique
print(my_other_list)

my_other_list[1] = "Rojo"           # Modificamos un valor

my_other_list.remove("Rojo")        # remove elimina el elemento que escribas
print(my_other_list)

my_list.remove(30)                  # En este caso, solo elimina un solo 30
print(my_list)

my_pop_element = my_list.pop(2)     # Desapila el elemento de la lista que escribas y lo almacena en la variable que crees
print(my_pop_element)
print(my_list)

del my_list[2]                      # Eliminamos el elemento de la lista por indice
print(my_list)

my_new_list = my_list.copy()        # Copiamos la referencia

my_list.clear()                     # Eliminamos la lista entera
print(my_list)
print(my_new_list)

my_new_list.reverse()               # Invertimos el orden
print(my_new_list)

my_new_list.sort()                  # Ordenamos la lista según criterio (Por defecto lo ordena de mayor a menor)
print(my_new_list)

print(my_new_list[1:3])             # Sublistas


my_list = "Hola Python"             #Cuidado con cambiar el tipo de la variable (Tipado dinámico)
print(my_list)
print(type(my_list))        