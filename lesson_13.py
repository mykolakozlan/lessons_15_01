# def simple_num(num):
#     div = 1
#     div_list = []
#     while div <= num:
#         if num % div == 0:
#             div_list.append(div)
#         div += 1
#
#     return True if len(div_list) == 2 else False
#
# def simple_num(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# #
# #
# def prime_generator(end):
#     _number = 1
#     while _number <= end:
#         if simple_num(_number):
#             yield _number
#         _number += 1
#
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')




# def is_even(number):
    # list_num = list(str(number))
    # num_list = ['0', '2', '4', '6', '8']

    # if list_num[-1] in num_list:
    #     res = True
    # else:
    #     res = False

    # return res

    # return str(number)[-1] in ('0', '2', '4', '6', '8')


# def is_even(number):
#     return (number & 1) == 0


# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print('Ok')











# class Animal(object):
# class Animal:
#     """Клас, в якому знаходяться поля, характерні для великої підгрупи.
#        У всіх тварин є вік, раціон харчування та забарвлення
#     """
#     age = 10
#
#     def __init__(self, age, ration, color):
#         self.age = age
#         self.ration = ration
#         self.color = color
#
#     def get_voice(self):
#         """Базовий метод, не прив'язаний до конкретного типу тварин  """
#         return 'Animal'
#
#     def __repr__(self):
#         return f"age = {self.age}"
#
#     def __str__(self):
#         return f"age = {self.age}, ration = {self.ration}, color = {self.color}"
#
#
#
#
# # animal_1 = Animal(10, "meat", "red")
# # print(animal_1)
# # print([animal_1,])
# # print(Animal.age)
#
# class Cat(Animal):  # клас Cat є спадкоємцем Animal
#
#     def __init__(self, age, ration, color, name, cat_type):
#         # Для того, щоб був ініційований екземпляр Animal, необхідно в явному вигляді викликати метод __init__ цього класу
#         super().__init__(age, ration, color)  # функція super "знає", хто є батьком цього класу
#         self.name = name
#         self.cat_type = cat_type
#
#     def get_voice(self):
#         # за допомогою функції super, отримаємо результат роботи методу з батьківського класу
#         res = super().get_voice()
#         return res, "Meow"
#
#     def __str__(self):
#         return f"Cat: {super().__str__()} , name = {self.name}, cat_type = {self.cat_type}"
#
#
# barsik = Cat(3, 'meat', 'black', 'barsik', 'pers')
# # print(barsik)
# print(barsik.get_voice())
#
#
#
# class Dog(Animal):
#
#     def __init__(self, age, ration, color, name, dog_type):
#         super().__init__(age, ration, color)
#         self.name = name
#         self.dog_type = dog_type
#
#     def get_voice(self):
#         # за допомогою функції super, отримаємо результат роботи методу з батьківського класу
#         res = super().get_voice()
#         return res, "Woof"
#
# dog = Dog(3, 'meat', 'black', 'Рes', 'BullDog')
# print(dog.get_voice())
#
#









from abc import ABC, abstractmethod

# class Animal(ABC):  # Вказуємо клас ABC як батьківський
#
#     def __init__(self, age, ration, color):
#         self.age = age
#         self.ration = ration
#         self.color = color
#
#     @abstractmethod  # Створюємо метод, який обертаємо за допомогою декоратора
#     def get_voice(self):  # raise TypeError
#         pass



# class Fox(Animal):
#
#     def __init__(self, age, ration, color, name, fox_type):
#         super().__init__(age, ration, color)
#         self.name = name
#         self.fox_type = fox_type
#
#     def get_voice(self):
#         return "Fox"



# fox = Fox(3, 'meat', 'black', 'fox', 'red_fox')
# print(fox.get_voice())













# class Base:
#     def price(self):
#         return 10
#
# class InterFoo(Base):
#     def price(self):
#         return Base.price(self) * 1.1
#
# class Discount(InterFoo):  # <--
#     def price(self):
#         return InterFoo.price(self) * 0.8



# class Base:
#     def price(self):
#         return 10
#
# class InterFoo(Base):
#     def price(self):
#         return super().price() * 1.1 # Тут через super().price() ми звертаємося до методу price у класі Base
#
# class Discount(InterFoo):
#     def price(self):
#         return super().price() * 0.8 # Тут через super().price() ми звертаємося до методу price у класі InterFoo









# class A:  # (object)
#     def print_smile(self):
#         print(":)")
#
#
# class B(A):
#     def print_sad_smile(self):
#         print(":(")
#
# class C(A):
#     def print_both_smile(self):
#         print(":( :)")
#
# class D(C):
#
#     def print_sad_smile(self):
#         print("^)")
#
# example = D()
# example.print_sad_smile()
# example.print_smile()
# example.print_both_smile()
#
# # MRO – (Method Resolution Order)
# print(D.mro())
# print(D.__mro__)


# if __name__ == "__main__":


# class D:
#     def print_smile(self):
#         print (":P)")
#
# class A(D):
#     pass
#
# class B:
#     def print_smile(self):
#         print(":(")
#
# class C(A, B):
#     pass
#
# my_var = C()
# print(C.__mro__)
# my_var.print_smile() # Пошук атрибутів у класах батьках, завжди йде зліва направо, і знизу вгору






############ Exeptions/Вийнятки ################

# num = 10 / 0
#
# try:
#     # num = 10 / 0
#     # res = "3" + 2
#     # val_list = []
#     # val_list[0]
#     val_list = {}
#     print(val_list["name"])
# except (ZeroDivisionError, TypeError):
#     print("You can divide by zero")
# except IndexError:
#     print("IndexError")
# except Exception as e:
#     print("Oops something goes wrong. Please try again later")
#     print("Exception")
#     print("Error some_func: ", e)
# else:
#     print("else")
# finally:
#     print("finally")

# try:
# else:

# try:
# finally:

# with open() as file:
#     pass


# except:
#     print("Oops something goes wrong. Please try again later")



# print("end")
#

# class UserException(Exception):
#
#     def __init__(self, message, obj):
#         super().__init__()
#         self.message = message
#         self.obj = obj
#
#     def get_exception_message(self):
#         return self.message
#
#
# def positive(num):
#     if num < 0:
#         raise UserException("Error positive()", num)
#     return num


# def negative(num):
#     if num > 0:
#         raise UserException("Error negative(): ", num)
#         # raise ZeroDivisionError
#     return num
#
#
# try:
#     print(positive(-3))
#     print(negative(3))
# except UserException as err:
#     print(err.get_exception_message())
#     print(err.obj)
















