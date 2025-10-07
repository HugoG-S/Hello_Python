### File Handling ###

import os

# .txt file
txt_file = open("Intermediate/myfile.txt", "w+") # r+ para leer y escribir - w+ para leer y sobreescribir

txt_file.write("My name is Reshi \nMy surname is Ladrian \nI am 34 years old " \
"\nMy favorite programming language is Python")

#print(txt_file.read()) # - Leer el archivo
print(txt_file.read(10)) # - Lee los 10 primeros dígitos del archivo
print(txt_file.readline()) # - Lee una línea entera 

# readlines lee todas las lineas, las junta en un listado y con un for las iteramos
for line in txt_file.readlines(): 
    print(line)

txt_file.write("\nAlthough I also like Java") # - write nos permite escribir en el archivo
print(txt_file.readline())

txt_file.close() # - Cerramos flujo de archivo (Buena Práctica)

with open("Intermediate/myfile.txt", "a") as my_other_file:
    my_other_file.write("\nAnd C#")

#os.remove("Intermediate/myfile.txt") - Con os.remove(ruta del archivo) eliminamos el archivo

# .json file 

import json

json_file = open("Intermediate/myfile.json", "w+")

# Creamos un diccionario que será lo que almacenaremos en el json

json_test = {
    "name":"Reshi",
    "surname":"Ladrian", 
    "age":34, 
    "languages": ["Python", "Java", "C#"],
    "website" : "https://youtube.es"}


# Con .dump, almacenamos la información del diccionario al archivo json, si añadimos más dump, 
# escribirá a continuación de lo escrito.
# con indent haremos la "ordenación" de filas en el archivo, y con el número indicamos los espacios que tendrá
json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Intermediate/myfile.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# Pasamos un json a un diccionario para poder modificarlo
json_dict = json.load(open("Intermediate/myfile.json"))
print(json_dict)
print(json_dict["name"])

# .csv file

import csv
csv_file = open("Intermediate/myfile.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Reshi", "Ladrian", 34, "Python", "youtube"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/myfile.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file

#import xlrd debe instalarse el módulo 

# .xml file

import xml