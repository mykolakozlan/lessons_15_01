
# def pow(x):
#     return x ** 2
#
#
# def some_gen(begin, end, func):
#     """
#      begin: перший елемент послідовності
#      end: кількість елементів у послідовності
#      func: функція, яка формує значення для послідовності
#     """
#     for _ in range(end):
#         yield begin
#         begin = func(begin)
#
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
#
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')


# def is_even(digit):
#     return digit % 2 == 0
# # def is_even(digit):
# #     if digit % 2 == 0:
# #         return True
# #     else:
# #         return False
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')

########### OOP ######### Обʼєктно орієнтовне програмування

####### 3 Принципи ООП: Інкапсуляція, Поліморфізм, Наслідування     +2 Абстракція та Композиція(не пітонівські)


# class Car:
# # class Car(object):
#     """Some doc string"""
#     # color = "green"   # атрибут
#     # engine = 2.0
#
#     def __init__(self, color, engine):
#         self.color = color
#         self.engine = engine
#         self.body = "body"
#
#
# car_1 = Car("red", 3.2)
# car_2 = Car("green2222", 1.6)
#
# print(car_1.color)
# print(car_1.body)
# print(car_2.color)
# print(car_2.body)
# # print(Car.color)



# class Cat:
#
#     def __new__(cls, *args, **kwargs): # метод, який насправді створює екземпляр класу
#         print("Creating Cat instance")
#         self = super().__new__(cls) # про функцію super() трохи пізніше
#         print(self)
#         return self # instance
#
#     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
#         print("Cat instance fields")
#         self.name = name
#         self.age = age
#         self.color = color
#
# cat = Cat('Barsik', 5, 'black')
# print(cat)
# # print(cat.age)


# class Cat:
#
#     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def get_voice(self):
#         return "Meow"
#
#     def __repr__(self):
#         return f"Cat: {self.name}"
#
#     def __str__(self):
#         return f"Hi my name is {self.name}, I'm {self.age} years old"
#
#
# cat = Cat('Barsik', 5, 'black')
# print(cat.__dir__())
# print(cat.__hash__())



# cat_1 = Cat('Tom', 15, 'white')
# print(cat)
# print(cat_1)
#
# cats_list = [cat, cat_1]
# print(cats_list)

# print(cat.get_voice())
# print(cat.age)








# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f'Phone {self.brand} {self.model} {self.price}'




# class Laptop:
#     def __init__(self, brand, model, price):
#         # Важливо, щоб набір полів був схожим на інші класи, які зберігаються на складі
#         self.brand = brand
#         self.price = price
#         self.model = model
#         # self.processor = processor
#
#     def __str__(self):
#         return f'Laptop {self.brand} {self.model} {self.price}'
#
#
# laptop1 = Laptop('HP', 'S11', 327000)



# # Створимо кілька екземплярів класу Phone
# phone1 = Phone('Samsung', 'A52', 7000)
# # print(phone1)
# phone2 = Phone('Samsung', 'S11', 37000)
# phone3 = Phone('Samsung', 'A12', 4000)
# phone4 = Phone('Xiaomi', 'Redmi Note 11 ', 8700)
# phone5 = Phone('Xiaomi', '12 Lite', 17000)
# # print(phone5)
#
# # print(hash(phone1))
#
#
# class Warehouse:
#
#     def __init__(self, address):
#         self.address = address
#         self.storage = {}
#
#     def add_to_storage(self, item, value):
#         """ Метод додавання товару на склад """
#         self.storage[item] = value
#
#     def remove_from_storage(self, item):
#         """ Метод видалення товару зі складу """
#         value = self.storage.pop(item, None)
#         return value
#
#     def get_item_value(self, item):
#         """ Метод отримання кількості товару на складі """
#         return self.storage.get(item)
#
#     def get_total_value(self):
#         """ Метод отримання загальної вартості товару на складі """
#         total = 0
#         for key, cnt in self.storage.items():
#             total += key.price * cnt
#         return total
#
#     def __str__(self):
#         """ Метод виведення інформації про склад """
#         tmp = ''
#         for item, cnt in self.storage.items():
#             tmp += f'{str(item)}: {cnt} pcs. \n'
#         return f'Warehouse at {self.address} contains:\n{tmp} '
#
# wh = Warehouse('Kyiv, vul. Viskozna, 135')
# print(wh.get_total_value())  # На складі нічого немає
# #  Додамо на склад кілька телефонів і перевіримо деякі методи
# wh.add_to_storage(phone1, 40)
# wh.add_to_storage(phone2, 23)
# # print(wh.get_total_value())
# # print(wh.get_item_value(phone2))
#
# wh.add_to_storage(phone3, 4)
# wh.add_to_storage(phone4, 52)
# wh.add_to_storage(phone5, 22)
# print(wh.get_total_value())
# print(wh)
# # # Видалимо кілька телефонів і перевіримо інформацію по складу
# print(wh.remove_from_storage(phone2))
# print(wh.get_item_value(phone2))
# print(wh)

# #  Додамо на склад кілька ноутбуків
# notebook = Laptop('HP', 'ProBook 450', 35000)
# notebook1 = Laptop('HP', 'Laptop 15s-eq2054ur', 42000)
# wh.add_to_storage(notebook, 10)
# wh.add_to_storage(notebook1, 3)
# # print(wh.get_total_value())
# print(wh)





# isinstance()

# value_num = 10
#
# if isinstance(phone1, Phone):
#     print("!!!!!")
#     value_num = int(value_num)
# elif isinstance(laptop1, Phone):
#     print("))))))))")
#     value_num = int(value_num)
#
# value_num += 1
# print(value_num)


# def get_voice(name):
#     return f"Meow {name}"
#     # return f"Meow"

# class Cat:
#
#     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __repr__(self):
#         return f"Cat: {self.name}"
#
#     def __str__(self):
#         return f"Hi my name is {self.name}, I'm {self.age} years old"
#
#     @staticmethod
#     def get_voice(name):
#         return f"Meow {name}"
#         # return f"Meow"
#
#
# cat = Cat('Barsik', 5, 'black')
# print(cat.get_voice("Tom"))
# print(Cat.get_voice("Tom"))



# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # # Дозволяє обчислити дані, і повернути новий екземпляр класу, з цими даними
#     @classmethod
#     def from_birth_year(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     # Метод, який не пов'язаний зі змінними ні цього класу, ні його екземплярів
#     @staticmethod
#     def is_adult(age):
#         return age > 18
#
#
# person1 = Person('Michael', 21)
# person2 = Person.from_birth_year('John', 1996)
#
# print(person1.age)
# print(person1.is_adult(person1.age))
# print(person2.name)
# print(person2.age)
# print(person3.age)




############### Наслідування ##############
#
# class Animal:
#
#     def __init__(self, name, food, color):
#         self.name = name
#         self.food = food
#         self.color = color
#
#     def animal_voice(self):
#         return "Animal sounds: "
#
#
# class Tiger(Animal):
#
#     def __init__(self, name, food, color, age):
#         super().__init__(name, food, color)
#         self.age = age
#
#     def animal_voice(self):
#         begin = super().animal_voice()
#         return begin + "Raughhhh"
#
#
# tiger_1 = Tiger("Sebastian", "meat", "yellow", 9)
#
# print(tiger_1.name)
# print(tiger_1.animal_voice())





from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, food, color):
        self.name = name
        self.food = food
        self.color = color

    @abstractmethod
    def animal_voice(self):
        pass


class Tiger(Animal):
    """Is doing something"""
    def __init__(self, name, food, color, age):
        super().__init__(name, food, color)
        self.age = age

    def animal_voice(self):
        begin = super().animal_voice()
        return begin + "Raughhhh"


tiger_1 = Tiger("Tom", "meat", "red", 10)

print(tiger_1.__doc__)