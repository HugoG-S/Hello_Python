### Dictionaries ###
# Los Diccionarios almacenan datos con clave valor

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Hugo", "Nickname":"Reshi", "Edad":34, 1:"Python"}
print(my_other_dict)

# Formato más claro para ver mejor los datos añadidos

my_dict = {"Nombre":"Hugo", 
           "Nickname":"Reshi", 
           "Edad":34, 
           "Lenguajes":{"Python", "Java", "Dart"},
           1:1.77
           }

print(my_dict)

print(len(my_other_dict))   # Con len nos cuenta las claves del diccionario
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Anacleto"
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle San Pablo"    # Añadimos un nuevo campo
print(my_dict)

del my_dict["Calle"]                    # Podemos eliminar campos con del
print(my_dict)

print("Hugo" in my_dict)
print("Nombre" in my_dict)              # Con in busca por el campo

print(my_dict.items())
print(my_dict.keys())                   # Nos devuelve las claves
print(my_dict.values())                 # Nos devuelve todos los valores

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) #Crea un diccionario nuevo con las claves, pero no los valores
print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys((my_list))  # Tambien podemos de una lista a un diccionario
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Hugo", "Reshi")) # Así añadimos a todas las claves los valores indicados
print(my_new_dict)

print(list(my_new_dict))
print(tuple(my_new_dict))               # Podemos convertir el diccionario en tupas, listas y sets, pero solo cogería la clave
print(set(my_new_dict))

print(list(my_new_dict.values()))       # Con values si podremos almacenar en una lista, set y tupla el contenido de los valores