my_condition = 0

# while my_condition < 30:
#     print(my_condition)
#     my_condition+=2

#     if my_condition == 14:
#         print("se detiene")
#         break


my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (19, 1.80, "Azael", "Morell", "Martinez")
my_set = {"Azael", "Morell", 19}
my_dict = {"Nombre":"Azael", "Apellido":"Morell", "Edad":19, 1:"python"}

print(my_tuple[::2])

for element in my_tuple:
    print(element)
print()

for element in my_set:
    print(element)
print()

for element in my_dict:
    print(element)

for element in list(my_dict.values()):
    print(element)
    if element == 19:
        print("Se acabo lo que se daba!")
        break
    print("Se ejecuta...")

else:
    print("El bucle for ha finalizado")

for element in list(my_dict.values()):
    print(element)
    if element == 19:
        continue
    print("loading...")
else:
    print("El bucle for ha finalizado")