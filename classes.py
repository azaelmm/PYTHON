

class MyEmptyPerson:
    pass


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname    
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"Esta caminando {self.name}...")

my_person = Person("Azael", "Morell")
print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)