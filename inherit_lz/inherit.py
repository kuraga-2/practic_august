import pandas as pd
class Animal():
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        print(self.name," издает звук")

    def get_info(self):
        print(f"Животное вида {self.species} зовут {self.name} ему/ей {self.age} года/лет",)

class Dog(Animal):
    def __init__(self,name, age, species, breed, guard_status):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.guard_status = guard_status


    def guard_house(self):
        if self.guard_status == "Да" or "да":
            print(f"{self.name} охраняет дом")
        else:
            print(f"{self.name} не умеет охранять дом")
    
    def get_info(self):
        super().get_info()
        if self.guard_status == "Да" or "да":
            print(f"Его/её порода {self.breed} и он/она умеет охранять дом")
        else:
            print(f"Его/её порода {self.breed} и он/она не умеет охранять дом")



        