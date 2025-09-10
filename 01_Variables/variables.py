# Variables 
# Al contrario de Java, utiliza Snake Case para declarar variables. Ejemplo: my_variable (Utilizamos barra baja para separar palabras)

print('====== Variables ======')

my_variable = "My String Variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

#Funcion str para convertir un tipo de dato a string
my_int_to_str_variable = str(my_int_variable) 
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable) 

# Funciones del sistema
# len cuenta los caracteres
print(len(my_variable))

# Variables en una sola línea. ¡ Cuidado con abusar de esta sintaxis !
# No es recomendable si son muchas variables, no es buena práctica

name, surname, alias, age = "Hugo", "Gallego", "Reshi", 34 

print(surname,"Mi edad es:", age, "Mi nombre es:", name, "Y mi alias es:", alias)

# Inputs 
name = input('¿Cual es tu nombre? ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)

#Cambiamos el valor a las variables, de str a numero entero y viceversa
name = 35
age = "Hugo"

print(name)
print(age)

# ¿Forzamos el tipo de la variable? Python al ser de tipado dinámico, 
# podemos dejar constancia del tipo de variable como está abajo,pero es un tipado débil
address: str = "Mi dirección"
address = 32

print(address)

# Con Type vemos el tipo de dato
print(type("Hola Python")) # Tipo 'str'
print(type(5)) # Tipo 'int'
print(type(1.5)) # Tipo 'float'
print(type(1 + 2j)) # Tipo 'complex' 
print(type(True)) # Tipo 'bool'