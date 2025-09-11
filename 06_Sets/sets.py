### Sets ###
# Los Sets no tienen una estructura ordenada

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))   # Inicialmente si lo declaramos con {} nos dice que es un diccionario

my_other_set = {"Hugo", "Reshi", 34}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Granada")
print(my_other_set)        
my_other_set.add("Granada")
print(my_other_set)         # Un set no admite repetidos

print("Reshi" in my_other_set)      # Busqueda y comprobación de datos dentro del set
print("Reshik" in my_other_set)

my_other_set.remove("Hugo")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

#del my_other_set   del elimina el objeto directamente, dará error: name 'my_other_set' is not defined. Porque lo hemos eliminado
#print(my_other_set)

my_set = {"Hugo", "Reshi", 34}
my_list = list(my_set)
print(my_list)
print(my_list[0])           # Podemos convertir un set a una lista y poder acceder a sus elementos (No recomendable)

my_other_set = {"Java", "Python", "Dart"}

my_new_set = my_set.union(my_other_set)     # Con union, unimos sets
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))  # Ignora los dos primeros union (Datos repetidos) pero el último si lo añade (En el print, no lo almacena en el set)

print(my_new_set.difference(my_set))        # Vemos la diferencia entre sets