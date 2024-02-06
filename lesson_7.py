# import string, keyword

# my_string = '_'  # Вивід: True
# my_string = 'x'  # Вивід: True
# my_string = 'get_value'  # Вивід: True
# my_string = 'get value'  # Вивід: False
# my_string = 'get!value'  # Вивід: False
# my_string = 'some_super_puper_value'  # Вивід: True
# my_string = 'Get_value'  # Вивід: False
# my_string = 'get_Value'  # Вивід: False
# my_string = 'getValue'  # Вивід: False
# my_string = '3m'  # Вивід: False
# result = True
#
# if my_string[0].isdigit():
#     result = False
# elif my_string in keyword.kwlist:
#     result = False
#
# for letter in my_string:
#     if not result:
#         break
#     elif (letter.isupper() or
#           letter in string.punctuation or
#           letter.isspace()):
#         result = False
#         break
#     elif letter == "_":
#         continue
#
# print(result)




# my_string = 'myString'  # Вивід: True
# result = False
#
# if my_string.isidentifier():
#     if my_string == "_" or my_string.islower():
#         result = True
#
# print(result)


#  _


# def adding():
#     pass
#
# def sub():
#     pass
#
# def mult():
#     pass
#
# def calc(num_1, num_2, action):
#     if action == "+":
#         result = num_1 + num_2
#     elif action == "-":
#         result = sub(num_1, num_2)
#     elif action == "*":
#         result = mult(num_1, num_2)
#
#     return result




# Modified calculator
# while True:
#     number_1 = input('Enter the first number: ')
#     action = input('Enter the operator: ')
#     number_2 = input('Enter the second number: ')
#
#     if not number_1.isdigit() or action not in ('+', '-', '/', '*') or not number_2.isdigit():
#     # if not number_1.isdigit() or action not in ('+', '-', '/', '*') or not number_2 or not number_2.isdigit():
#         print('Undefined number! Try again.')
#         continue
#
#     number_1 = float(number_1)
#     number_2 = float(number_2)
#
#     result = 0
#
#     if action == '+':
#         result = number_1 + number_2
#     elif action == '-':
#         result = number_1 - number_2
#     elif action == '*':
#         result = number_1 * number_2
#     elif action == '/' and number_2 == 0:
#         result = str('Ділення на нуль неможливе!')
#     else:
#         result = number_1 / number_2
#
#     print(result)
#
#
#     var_cont = input('Do you want to stop? Y/N? ')  #Y y
#     if var_cont.lower() != 'y':
#         print('Good bye!')
#         break


# Множина (set)
#     Доступні методи
#     Порівняння множин
#     Frozenset

# my_set = set()
# my_set = {1, 2, 3}
# my_set = {"apple", "red", "red2"}
# my_set_2 = {"adding",}
# print(my_set)
# val_pop = my_set.pop()
# print(val_pop)

# my_set.remove("red2")
# print(my_set)

# my_set.add("adding")
# print(my_set)

# difference()
# intersection()
# union()
# my_set = {"apple", "red", "red2"}
# my_set_2 = {"adding", "apple"}

# my_set.update(my_set_2)
# dif_set = my_set.difference(my_set_2)   # my_set - my_set_2
# intersect_set = my_set.intersection(my_set_2)
# union_set = my_set.union(my_set_2)

# print(union_set)

# val_list = [1, 3, 4, 5, 6, 6, "apple", 6, 7, "red", 3, 1, 4]

# print(val_list)
# print(set(val_list))


############################################# Function ################################

# method and func


# def get_set_make_my_formule(number_1, number_2):
#
#     res = number_1 + number_2
#     if res < 0:
#         res = None
#
#     return res
#
#
# result = get_set_make_my_formule(5, -6)
# print(result)


# send_email
# set_email_body
# get_email_from_client







# def my_formule():
# def my_formule(num_1, num_2):
#
#     res = num_1 + num_2
#
#     return res
#
#
# number_1 = 9
# number_2 = 8
# result = 0
#
# print(my_formule(number_1, number_2))
#
# print(result)

# def my_formule(num_1, num_2):
#
#     # result = num_1 + num_2
#     result.append(num_1 + num_2)
#
#     return result
#
#
# number_1 = 9
# number_2 = 8
# result = [1, 2, 3]
#
# print(my_formule(number_1, number_2))
#
# print(result)


# def my_formule(num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9):
#
#     result = num_1
#     # result.append(num_1 + num_2)
#
#     return result


# def correct_sentence(text):
#     pass

# def correct_sentence(text):
#     """This func do something"""



# def my_formule(num_1, num_2):
#     return num_1 + num_2
#
#
#
#
# assert my_formule(1, 2) == 3, 'Test1'
# assert my_formule(5, 5) == 10, 'Test2'
# print('ОК')




