import os


def my_function ():
    os.system("cls")
    nombre = input("Introduce tu nombre: ")
    print("Hola, " + nombre + "!")
    age = int(input("Introduce tu edad: "))
    if age < 18:
        print("Eres menor de edad.")
    print(f"Tienes {age} años.")
    country, city = input("Introduce tu país y ciudad (separados por coma): ").split(",")
    print(f"Vives en {city}, {country}.")

def sum_two_values (first_number, second_number):
    print("Resultado: ", first_number+second_number)

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

def print_name (name, surname):
    print(f"Nombre: {name}, Apellidos: {surname}")

def print_name_with_default (name, surname, alias = "sin alias"):
    print(f"Nombre: {name}, Apellidos: {surname} y alias: {alias}")

def print_upper_texts (*texts):
    for text in texts:
        print(text.upper())

my_function()

# sum_two_values(20, 30)

# sum_two_values("20", "30")

# my_result = sum_two_values_with_return(50, 50)

# print(my_result)

# print(sum_two_values_with_return(1, 1))

# print_name("Azael", "Morell")

# print_name_with_default("Azael", "Morell", "PaperDev")

# print_upper_texts("Hola", "Pero", "Python")