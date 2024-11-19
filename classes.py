

class MyEmptyPerson:
    pass


class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name
        self.surname = surname    
        self.full_name = f"{name} {surname} ({alias})"

    def get_name (self):
        return self.__name

    def walk(self):
        print(f"Esta caminando {self.__name}...")

my_person = Person("Azael", "Morell")
print(f"{my_person.get_name} {my_person.surname}")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Azael", "morell", "AzaelDev")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Oscar Garcia (El ciclista)"
print(my_other_person.full_name) 