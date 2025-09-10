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

my_other_list.remove("Verde")       # remove elimina el elemento que escribas
print(my_other_list)

my_list.remove(30)                  # En este caso, solo elimina un solo 30
print(my_list)

my_list.pop()                       # 
print(my_list)





my_list = "Hola Python"
print(my_list)
print(type(my_list))        #Cuidado con cambiar el tipo de la variable (Tipado dinámico)