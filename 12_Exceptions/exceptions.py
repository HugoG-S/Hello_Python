### Manejo de Errores ###

numberOne, numberTwo = 5, 1

numberTwo = "1"

# Try Except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Try Except Else Finally (Opcionales Else y Finally)

try:
    print(numberOne + numberTwo)
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:
    # Se ejecuta siempre, pase lo que pase
    print("La ejecución continúa")    

## Captura de excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")    

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as e:
    print(e)       
except Exception as e:
    print(e)    