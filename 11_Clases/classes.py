### Clases ###
## Una clase es un molde para crear objetos, agrupando datos (atributos) y funciones (Métodos) relacionados.

class MyEmptyPerson:
    pass 



# def __ini__  Define el constructor de la clase. Con self, asignamos el valor a las propiedades de la clase

class Person:
    def __init__(self, name, nickname, ciudad = "Sin Ciudad"):
        self.name = name                            
        self.nickname = nickname
        self.full_name = f"{name} ({nickname}) {ciudad}"       # Propiedad almacenada

    def walk (self):
        print(f"{self.nickname} está caminando")    


my_person = Person("Hugo", "Reshi")

print(my_person.nickname)
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Reshi", "Khemri", "Granada")

print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León El loco de los perros"
print(my_other_person.full_name)