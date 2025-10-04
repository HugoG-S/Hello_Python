### Higher Order Functions ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

## Funcion de orden superior, donde desde otras funciones enviamos datos (en este caso +1 y +5)
def sum_two_values_and_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_one(5, 2, sum_one))
print(sum_two_values_and_one(5, 2, sum_five))

### Closures ###
## Sin parámetro
def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()

print(add_closure(5))

## Con parámetro
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)

print(add_closure(5))

print(sum_ten(5)(1))

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21]

# Map

def multiply_two(number):
    return number * 2

# Como map es una funcion de orden superior, añadimos una función dentro para que multiplique *2 en la lista que le hemos añadido
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))