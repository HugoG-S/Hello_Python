### Type Hints ###
## Python tiene soporte para "anotaciones de tipos" opcionales (Type Hints). Estas anotaciones
# son una sintaxis especial que permite declarar el tipo de una variable. Al declarar tipos 
# para tus variables, los editores y herramientas te pueden proporcionar un mejor soporte.

my_string_variable = "My String Variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: str = "My Typed String Variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable: int = 5
print(my_typed_variable)
print(type(my_typed_variable))
