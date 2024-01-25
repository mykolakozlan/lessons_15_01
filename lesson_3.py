# Bool, None types
# Logic operators
# Зведення типів
# Duck typing
# If statement (programming golf, Тернарний оператор)
# list
# змінні не змінні типи даних різниця
# методи list(append(), pop(), sort(), copy())
# функція sorted()


# int
# float
# Decimal
# complex

# str

# None
# bool

# tuple
# list
# set
# dict

######### NoneType ####

# value = None
# value_int = 11111
#
# # value_address = id(value_int)
# value_address = print(value_int)
#
# print(value_address)

########### Boolean ########## True/False

# is_email_confirmed = True

# value_int = -1
# value_float = -0.0000001
# value_str = "Hello"

# value_bool = True
# print(value_bool * 2)

# value = 100
# print(bool(value) * 4)

# value_int = 5
# value_float = 5.0


# print(value_1 == value_2) # >, <, >=, <=, ==, !=, in, not, is(===)

# print("he" in "hello")
# print(not value_1) # зворотнє значення

# is (===)
# print(value_int != value_float)
# print(value_int is value_float)

# if певна умова:
#    певну дію

# weather = "cold"
#
# if weather == "cold":
#     print("It's cold")
# else:
#     print("It's not cold")
#
# print("end")

# value_int = 12
#
# # or and
#
# if (value_int > 0) and (value_int < 10): #else if
# # if not value_int > 0 or not value_int < 10:
# # if 0 < value_int < 10:
#     print(f"{value_int} is bigger than 0")
# elif value_int > 10:
#     print(f"{value_int} is bigger than 10")
# else:
#     print(f"{value_int} is not bigger than zero")
#
# print("end")
#


# a = 2
# b = 330
#
# operator = "-"
#
# if operator == "+":
#     result = num_1 + num_2
# elif operator == "-":
#     result = num_1 - num_2

# #     result = "A"
# # else:
# #     result = "B"
#
# result = "A" if a > b else "B"
#
# print(result)


############ Зведення типів #############


# value = 10.6
# # value_str = str(value)
# # value_float = float(value)
# # value_bool = bool(value)
# value_int = int(value)
#
# print(value_int, type(value_int))


########## list #########

# value_list = list()

# value_list = [2, 3.2, "hello", True, [1, 2, 3], 9, 4, 5] # 0,1,2,3

# print(value_list[len(value_list) - 1])

# index = len(value_list) - 1
# index = -1
#
# print(value_list[-len(value_list)])

# print(value_list)
# print(value_list[4])
# print(value_list[-1])
# print(value_list[3:]) # від 3 і далі
# print(value_list[3:5]) # від 3 до 5(виключно) (індекси 3-4)
# print(value_list[0:5:2]) # від 0 до 5(виключно) з кроком в 2 (0,2,4)
# print(value_list[1:5:2]) # від 1 до 5(виключно) з кроком в 2 (1, 3)
# print(value_list[::-1]) # перекручує ліст


# ############################################

# base_list = [1, 2, 3]
# my_new_list = base_list * 4
# my_new_list = [obj, obj]
# # print(my_new_list)
#
# base_list[0] = 10
#
# print(f"base_list {base_list}")
# print(f"my_new_list {my_new_list}")

# # # ######################################
# copy
# deepcopy

from copy import deepcopy

base_list = [1, 2, 3, [True, False, 8, [1, 2, 3]]]

my_new_list = [base_list.copy()] * 4
# my_new_list = [deepcopy(base_list)] * 4
# my_new_list = [link, link, link, link]
print(my_new_list)
#
base_list[-1][0] = 10
print(f"base_list {base_list}")
print(my_new_list)
# print(f"my_new_list {my_new_list}")

# # # ######################################
