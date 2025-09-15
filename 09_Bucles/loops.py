### Bucles de Control ###
## Son una serie de mecanismos que nos sirve para iterar (Pasar por el mismo código varias veces)
#
##
### While: Se repite mientras una condición sea verdadera. Admite else (Es opcional).

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1    
else: 
    print("Mi condición es mayor o igual que 10")    

print("La ejecución continúa después del while")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        print("Se detiene la ejecución")
        break                              # Utilizamos break para detener la ejecución
    print(my_condition)



### For: Se usa para iterar sobre una secuencia (Lista, string, rangos...)(También podemos añadir else)

my_list = [35, 24, 62, 52, 30, 30, 17]

print("Listado de my_list con for:")

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Hugo", "Reshi", "Hugo")

for element in my_tuple:
    print(element)

my_set = {"Hugo", "Reshi", 34}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Hugo", 
           "Nickname":"Reshi", 
           "Edad":34, 
           "Lenguajes":{"Python", "Java", "Dart"},
           1:1.77
           }

for element in my_dict:                 # En el caso del diccionario, recoge las claves, no los valores
    print(element)


## Probando .values para sacar los valores del diccionario

for element in my_dict.values():        
    print(element)
else:
    print("El bucle for para diccionario ha finalizado")


## For con if y else

for element in my_dict:       
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")


for element in my_dict:       
    print(element)
    if element == "Edad":
        continue                        # continue continua con la ejecución del programa desde el punto donde esté declarado
else:
    print("El bucle for para diccionario ha finalizado")    

## For con range

i = 0
for i in range(100):
    print(i)