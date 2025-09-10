### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)


# Formateo de texto

name, nickname, age = "Hugo", "Reshi", 34
print("My name is {} and my nickname is {} and my age is {}".format(name, nickname, age))
print("My name is %s and my nickname is %s and my age is %d" %(name, nickname, age)) # Con %d nos aseguramos de que sea un número

# Inferencia (Formateo)
print(f"My name is {name} and my nickname is {nickname} and my age is {age}")

# Desempaquetado de caracteres

language = "Python"
a, b , c, d, e, f= language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3] 
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())    # capitalize pone la primera letra en mayúscula
print(language.upper())         # upper pone todo el texto en mayuscula
print(language.count("t"))      # count cuenta el número de la letra especificada
print("1".isnumeric())          # isnumeric nos dirá si es un número
print(language.isnumeric())     # En este caso da false porque no lo es
print(language.lower())         # Pone todas las letras en minúscula
print(language.upper().isupper()) # isupper comprueba que está en mayúscula. También vemos como se pueden concatenar funciones.