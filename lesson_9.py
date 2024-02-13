

# def say_hi(name, age):
#     # return f"Hi. My name is {name} and I'm {age} years old"
#     # return "Hi. My name is {} and I'm {} years old".format(name, age)
#
#     return "Hi. My name is " + name + " and I'm " + str(age) + " years old"
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'say_hi error: '
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('OK')


# def dot_check(tx):
#     # if correct_text[-1] != '.':
#     if not tx.endswith("."):
#         tx += "."
#     return tx
#
#
# def capital_check(tx):
#     if tx[0].islower():
#         # if not tx[0].isupper():
#         tx = tx[0].upper() + tx[1:]
#     return tx

# def validate(tx):
#     # if correct_text[-1] != '.':
#     if not tx.endswith("."):
#         tx += "."
#     if tx[0].islower():
#         # if not tx[0].isupper():
#         tx = tx[0].upper() + tx[1:]
#     return tx
#
#
# def correct_sentence(text):
#
#     # correct_text = capital_check(text)
#     # correct_text = dot_check(correct_text)
#
#     correct_text = validate(text)
#
#     return correct_text
#
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'correct_sentence error: Capital letter'
# assert correct_sentence("Hello") == "Hello.", 'correct_sentence error: Check for dot'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('OK')


# *args, **kwargs

# def draw_rectangle(w, h, fill):
#     for i in range(w):
#         for j in range(h):
#             print(fill, end="")
#
#     return None
#
# # draw_rectangle(7, 5, "*")
#
# # payload = [7, 5, "*"]
# # arguments = (7, 5, "*")
# arguments = 7, 5, "*"
# draw_rectangle(*payload)

# def my_sum(num_1, num_2):
#     return num_1 + num_2
#
#
# # def my_sum(num_1, num_2):
# #     return 100
#
#
# print(my_sum(3, 4))



# def my_sum(num_1, num_2):
#     return num_1 + num_2
#
# my_func = my_sum
# print(my_func)
# print(my_func(3, 4))


# def my_sum(num_1, num_2):
#     return num_1 + num_2
#
#
# def my_mul(num_1, num_2):
#     return num_1 * num_2
#
# func_list = [my_mul, my_sum]
# # print(func_list[0](3, 6))
#
# for func in func_list:
#     print(func(2, 3))

# choice = 1
#
# if choice == 1:
#     def my_func(n):
#         if n > 0:
#             return n
#         else:
#             return None
# else:
#     def my_func(n):
#         if n < 0:
#             return n
#         else:
#             return None
#
# print(my_func(5))


# ""
# ''
# """"""
# ''''''


# def my_func(n):
#     """
#     This func is doing something useful. Arg_1: ALWAYS STR
#     """
#
#     # This func is doing something useful. Arg_1: ALWAYS STR
#     if n > 0:
#         return n
#     else:
#         return None

# print(my_func)
# print(my_func.__name__)
# print(my_func.__module__)
#
# if __name__ == "__main__":
#     pass

# print(my_func.__doc__)
# print(str.find.__doc__)

# my_func()


# def my_sum(x, y, z):
#     """Counting"""
#
#
# def call_my_sum(my_list):
#     """call my_sum"""


# Рекурсія

# def fibo(n):
#
#     a = 0
#     b = 1
#
#     for i in range(2, n + 1):
#         a, b = b, a + b
#
#     return b
#
# print(fibo(10))


# def fibo(num):
#     if num in (1, 2):
#         return 1
#     # else:
#     #     return fibo(num-1) + fibo(num-2)
#     return fibo(num - 1) + fibo(num - 2)
#
# print(fibo(10))


# def fibo(num):
#
#     print(num)
#
#     if num in (1, 2):
#         return 1
#     return fibo(num - 1) + fibo(num - 2)
#
# print(fibo(5))


# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num - 1)
# # 5 * (4 * (3 * (2 * (1 * 1))))
#
# print(factorial(5))


#  lambda()

# def my_filter(seq, predicate):
#     result = []
#
#     for el in seq:
#         if predicate(el):
#             result.append(el)
#
#     return result
#
#
# sequence = [0, 9, -4, 1, 7, 8]
#
# # def bigger_than_zero(x):
# #     return x > 0
#
# bigger_than_zero = lambda x: x > 0

# print(my_filter(sequence, bigger_than_zero))
# print(my_filter(sequence, lambda x: x > 0))
# print(my_filter(sequence, bigger_than_zero))

# print(my_filter(sequence, lambda x: not x % 2 == 0))
# print(my_filter(sequence, lambda x: not x % 2 == 0 if x != 9 else False))

# map(), filter(), zip()

# value_str = "1234"
# value_str = ["1", "2", "3", "4"]
# # value_str = ("1", "2", "3", "4")
#
# val_list = []
#
# # for num in value_str:
# #     val_list.append(int(num))
# #
# # print(val_list)
#
# # new_list = list(map(int, value_str))
# new_list = list(map(lambda x: int(x)**2, value_str))
#
#
# print(new_list)


# filter()

# def my_filter(seq, predicate):
#     result = []
#
#     for el in seq:
#         if predicate(el):
#             result.append(el)
#
#     return result
#
#
# def bigger_than_zero(x):
#     return x > 0


# numbers = [1, 2, 3, -4, 7]
# numbers = (1, 2, 3, -4, 7)
#
#
#
# # filter_nums = filter(None, numbers)
# filter_nums = filter(lambda x: x > 0, numbers)
#
# print(list(filter_nums))


# zip()

# my_list_1 = [1, 2, 3, 4]
# my_list_2 = ["apple", "red", "green"]
# # my_list_3 = [True, False, 8, 9]
# my_list_3 = "123"
#
# for i in zip(my_list_1, my_list_2, my_list_3):
#     print(i)
#



# gen = range(10000)
# print(gen)
# print(type(gen))
# print(list(gen))

import sys

# print(sys.getsizeof(gen))
# print(sys.getsizeof(list(gen)))

# count_list = [0, 1, 2, 3, 4]
#
# for i in range(5):
# # for i in count_list:
#     print("Hello")


def add_one(num):
    return num + 1


def count(start, func):
    while True:
        yield start
        start = func(start)
        # yield start




counter = count(0, add_one)


# print(counter)
print(next(counter))
print(next(counter))
print(next(counter))

print("Hello")


print(next(counter))





