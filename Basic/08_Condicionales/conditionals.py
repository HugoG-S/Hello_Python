### Conditionals ###
# Representan la manera de establecer flujos de ejecución de nuestro código

my_condition = False

if my_condition: 
    print("Se ejecuta la condición del if")


my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo IF")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")    
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


print("La ejecución continúa")    

my_string = "Mi cadena de texto"

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooo":
    print("Estas cadenas de texto coinciden")

my_second_string = ""

if not my_second_string:
    print("La cadena de texto está vacía")