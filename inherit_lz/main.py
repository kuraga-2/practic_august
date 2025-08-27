import inherit as inh
name = input("Введите имя животного - ")
species = input("Введите вид животного - ")
age = input("Введите сколько ему лет - ")
obj = inh.Animal(name, age, species)
if species == "Собака" or "собака":
    breed = input("Введите породу собаки - ")
    guard_status = input("Умеет ли ваша собака охранять дом? (Да/Нет) - ")
    obj = inh.Dog(name, age, species, breed, guard_status)
    obj.get_info()
    obj.guard_house()
        
else:
    obj = inh.Animal(name, age, species)
    obj.get_info()
    obj.make_sound()
