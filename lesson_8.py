# Глобальні та локальні змінні.
# Передача аргументів.
# Правило доступу до змінних LEGB
# Використання іменованих параметрів.
# аргументи за замовчуванням
# Використання змінної кількості аргументів
# Використання змінної кількості іменованих аргументів
# Тонкощі використання аргументів
# Розпакування кортежу в низку фактичних параметрів
# Розпакування словника в низку фактичних параметрів
# Особливості використання функцій




# persons = [{"name": "John", "age": 15},
#            {"name": "Anna", "age": 23},
#            {"name": "Dan", "age": 5},
#            {"name": "Maximus", "age": 24},
#            {"name": "Olha", "age": 25},
#            {"name": "Volodymyr", "age": 5},
#            {"name": "Jack", "age": 45}]
#
#
# def exercise_6_1(persons_dict):
#     young_list = []
#     long_name_list = []
#     min_age = 1000
#     max_name_len = 0
#     av_age = 0
#
#     for person in persons_dict:
#         age = person.get("age")
#         name_len = len(person.get("name"))
#         av_age += age
#
#         # а
#         if age == min_age:
#             young_list.append(person.get("name"))
#         elif age < min_age:
#             young_list.clear()
#             young_list.append(person.get("name"))
#             min_age = age
#         # б
#         if name_len == max_name_len:
#             long_name_list.append(person.get("name"))
#         elif name_len > max_name_len:
#             long_name_list.clear()
#             long_name_list.append(person.get("name"))
#             max_name_len = name_len
#
#     # в
#     av_age = round(av_age / len(persons_dict))
#
#     return [young_list, long_name_list, av_age]
#
#
# young_persons, longname_person, avrg_age = exercise_6_1(persons)
# print(f"Min ege is: {young_persons,} {longname_person}, {avrg_age}")

# my_dict_1 = {1:1, 2:2}
# my_dict_2 = {11:11, 2:22}
#
# def exercise_6_2(dict_1, dict_2):
#
#     dict_1_list = dict_1.keys()
#
#     result_1 = list(set(dict_1_list).intersection(set(dict_2.keys())))
#
#     result_2 = list(set(dict_1.keys()).difference(set(dict_2.keys())))
#
#     # result_3 = {}
#     # for key in result_2:
#     #     # result_3.update({key: dict_1[key]})
#     #     result_3[key] = dict_1[key]
#
#     result_3 = {key: dict_1[key] for key in result_2}     # дікт компрехеншн
#
#     result_4 = dict_1.copy()
#     for key in dict_2:
#         if key in result_4:
#             result_4[key] = [result_4[key], dict_2[key]]
#         else:
#             result_4[key] = dict_2[key]
#
#     return result_1, result_2, result_3, result_4
#
#
# print(exercise_6_2(my_dict_1, my_dict_2))


# def add(num_1, num_2):
#     return num_1 + num_2
#
#
#
# def calc(num_1, num_2):
#     res = 0
#
#     if num_2 == 0:
#         res = "Error"
#     else:
#         res = add(num_1, num_2)
#
#     return None



#  LEGB правила доступу до змінних

# res = 500
#
# def add(num_1, num_2):
#     res = num_1 + num_2
#     return res
#
#
# print(res)
# print(add(1, 2))
# print(res)



# def add(my_list):
#     my_list[0] = 5
#     return my_list
#
# some_list = [1, 2 ,3]
# some_list_2 = [1, 2 ,3, 5, 6, 7]
#
# print(some_list_2)
# print(add(some_list_2))
# print(some_list_2)







from math import pi

# pi = "Global"
# def outer():
#     pi = "Enclosing"
#
#     def inner():
#         # pi = "Local"
#         pi += "!"
#         print(pi)
#
#     inner()
#
# outer()

# num += 1
# num = 9
#
# print(num)


# import operator
#
# actions = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv,
# }
#
# num_1 = float(input("num_1: "))
# action = input("action: ")
# num_2 = float(input("num_2: "))
#
# func = actions.get(action)
# if not func:
#     print("Error")
# else:
#     print(func(num_1, num_2))

# IS_DEBUG = False

# def print_line(w, fill, is_send_email=False, is_debug=False):
#     for i in range(w):
#         print(fill, end='')
#
#     if is_send_email:
#         print("llll")
#
#     if is_debug:
#         print("eeeeeeeeee")
#
#     return None
#
# # print_line(33, "*")
# # print_line(w=33, fill="*")
# print_line(33, "*", IS_DEBUG)


# args

# value_tuple = (1, 2, 3, 7, 8)
# val_1, val_2, *tmp = value_tuple
#
# print(val_1)
# print(val_2)
# print(tmp)


# def teachers_group(*args):
#     print(args)
#     group_dict = {"teacher": "Nick", "group_list": list(args)}
#     # for i in args:
#     #     group_dict['group_list'].append(i)
#
#     return group_dict
#
# print(teachers_group("John", "Tom", "Jessy", "Fin"))

# def get_min(*args):
#     if args:
#         min_val = args[0]
#         for i in args:
#             if i < min_val:
#                 min_val = i
#     else:
#         min_val = "error"
#     return min_val
#
# print(get_min())

# min()
# max()
# sum()


# print(1, 3, "dddd")



# **kwargs  {}




# def say_hello(name):
#     print(f"Hello {name}")


# def say_age(age):
#     print(f"Your are {age} years old")
#
#
# def print_line(w, fill, **kwargs):
#     print(kwargs)
#     for i in range(w):
#         print(fill, end='')
#     if kwargs.get("name"):
#         say_hello(kwargs.get("name"))
#     if kwargs.get("age"):
#         say_age(kwargs.get("age"))
#     return None
#
#
# # print_line(3, "*", name="Nick")
# # print_line(3, "*", age=18)
# print_line(w=3, fill="*", name="Nick", age=18, age_2=17)


# print_line(3, name="Nick", default, *args, **kwargs)   #шпаргалка за яким порядком треба викликати значення
