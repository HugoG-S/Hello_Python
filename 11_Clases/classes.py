### Clases ###
## Una clase es un molde para crear objetos, agrupando datos (atributos) y funciones (Métodos) relacionados.

class MyEmptyPerson:
    pass 



# def __ini__  Define el constructor de la clase. Con self, asignamos el valor a las propiedades de la clase

class Person:
    def __init__(self, name, nickname, ciudad = "Sin Ciudad"):
        self.name = name                                       # Propiedad pública
        self.nickname = nickname
        self.full_name = f"{name} ({nickname}) {ciudad}"       # Propiedad almacenada
        self.__name = name              ## Añadiendo __ delante de la variable, las hacemos privadas de la clase
        self.__nickname = nickname

## Creamos un "Getter" para poder ver la información del nombre (privado)

    def get_name (self):
        return self.__name

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

## Hay que tener cuidado con el tipado dinámico, las variables de clase pueden ser alteradas fácilmente

my_other_person.full_name = 666
print(my_other_person.full_name)

print(my_person.get_name())