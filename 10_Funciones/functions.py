### Funciones ###
## Una función es un bloque de código reutilizable que puede recibir datos (parámetros) y devolver un resultado (return)

def my_function ():
    print("Esto es una función")

my_function ()

## Podemos indicar que tipo de valor queremos, pero al ser tipado dinámico daría igual

def sum_two_values (first_value: int, second_value: int):    
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(453234, 2341352)

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)

print(my_result)

def print_name (name, nickname):
    print(f"{name} {nickname}")

## Podemos indicar el orden de los parámetros:

print_name(name = "Hugo", nickname = "Reshi")

# Definimos parámetros por defecto

def print_name_with_default (name = "Sin nombre", nickname = "Sin alias", city = "Sin ciudad"):
    print(f"{name} {nickname} {city}")

print_name_with_default()
print_name_with_default("Hugo", "Reshi")

# Con el * en los parámetros, podemos pasarle los que queramos

def print_texts (*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Python", "Reshi")    
print_texts("Hola")

def print_upper_texts (*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Reshi")    
print_upper_texts("Hola")      