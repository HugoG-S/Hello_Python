### Regular Expressions ###
##
#

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion número 6: Manejo de Ficheros"

# .match empieza a buscar desde el principio del string

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la leccion", my_other_string)
#if not(match == None): Otra forma de hacerlo
#if match is not None: Otra forma de hacerlo
if match != None:    
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# seach

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

split = re.split(":", my_string)
print(split)

#sub

print(re.sub("Expresiones Regulares", "RegEx", my_string))
print(re.sub("lección|Lección", "LECCIÓN", my_string))
print(re.sub("[l|L]ección", "Lección", my_string))

# Patterns

pattern = r"[l|L]ección"
print(re.findall(pattern, my_string))

pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

# emaul validation regular expression

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+$"
    return re.match(pattern, email)

email_valid = "reshi@reshi.com"
email_invalid = "reshi.com"
print(is_valid_email(email_valid))
print(is_valid_email(email_invalid))