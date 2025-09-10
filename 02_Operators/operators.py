### Operadores Aritmeticos. ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)
print(10 % 3)

# Realiza la división y termina aproximada a un número entero
print(10 // 3) 

# Calcular un exponente
print(2 ** 3) 

print(2 ** 3 + 3 - 7 / 1 //4)

# Concatenamos los string
print("Hola " + "Python") 

# Convertirmos el int 5 a string para poder concatenarlos
print("Hola " + str(5)) 

print("Hola " * 5)
print("Hola " * (2 ** 3))

# Utilizamos int() para transformar el valor de my_float de float a int
my_float = 2.5 * 2
print("Hola " * int(my_float))


### Operadores Comparativos. ###

print(3 > 4)    # Mayor que
print(3 < 4)    # Menor que
print(3 >= 4)   # Mayor o igual
print(3 <= 4)   # Menor o igual
print(3 == 4)   # Igual que
print(3 != 4)   # Diferente de

# También se puede usar varios operadores comparativos
print(3 > 4 == 2)

# Podemos usarlos también para comparar entre string
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

print("Hola" >= "Zola") # Ordenación alfabética
print(len("Hola") >= len("Zola")) # Ordenación caracteres


### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python") 
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python") 
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or "Hola" > "Python" and 4 == 4)

# Not niega la condición
print(not(3 > 4))