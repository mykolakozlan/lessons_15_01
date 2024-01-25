#  command + /(Mac) ctrl + /(Win)    comment line
#  command + d(Mac) ctrl + d(Win)    double line
#  command + option + l (Mac) ctrl + alt + l(Win)    PEP8



# some_input = int(input("enter some number(with 4 digits): "))

# thousands = some_input // 1000
# hundreds = some_input // 100 % 10
# tens = some_input // 10 % 10
# ones = some_input % 10
#
# print(f"{thousands}\n{hundreds}\n{tens}\n{ones}")

# print(f"{some_input // 1000}\n"
#       f"{some_input // 100 % 10}\n"
#       f"{some_input // 10 % 10}\n"
#       f"{some_input % 10}")


# thousands, d, *temp = [1, 2, 0, 7]
# # thousands, left_1 = divmod(my_input, 1000)
# print(thousands)
# print(d)
# print(temp)

# num_1, num_2 = 2, 3
#
# print(num_1)
# print(num_2)
#
# num_1, num_2 = num_2, num_1
#
# print(num_1)
# print(num_2)

# my_input = int(input("please add 4 digits: "))
#
# thousands, left_1 = divmod(my_input, 1000)
# hundreds, left_2 = divmod(left_1, 100)
# tens, ones = divmod(left_2, 10)
#
# print(thousands)
# print(hundreds)
# print(tens)
# print(ones)

# match/case
# list
# while
# break and continue
# while - else
# for
# for - else
# range()

# operator = "ooooo"
#
# # if operator == "+" or operator == "-":
# if (operator == "+") or (operator == "-"):
#     print("!!!!!!!!!!")
# else:
#     print("??????????")


# weather = "kkk"

# if weather == "cold":
#     print("cold")
# elif weather == "hot":
#     print("hot")
# else:
#     print("no weather")


# match/case

# match weather:
#     case "cold":
#         print("cold")
#     case "hot":
#         print("hot")
#     case _:
#         print("no weather")


# list

# value = 1
# value_1 = [1, 2, 3] # 88 byte

# value_1.append(1)  # 88 byte
# value_1.append(1)  # 88 byte
# value_1.append(1)  # 122 byte
# value_1.append(1)  # 122 byte
# print(value_1)
# value_1.insert(0, 4)
# print(value_1)
# value_1.insert(3, 5)
# print(value_1)
# value_1.insert(3, 6)
# print(value_1)

# value_1.clear()
# value_1.pop()
# print(value_1)
#
# # value_1.insert(3, 6)
# value_pop = value_1.pop()
#
# print(value_1)
# print(value_pop)
# value_1.insert(3, value_pop)
# print(value_1)


# reverse()
# value_1 = [1, 2, 8, 9, 1, 3]
# value_1 = ["bat", "apple", "", "berry"]    # ACII
# print(value_1)
# # value_1.reverse()
# # print(value_1, id(value_1))
# # print(value_1[::-1], id(value_1[::-1]))
#
# # sort() sorted()
#
# # value_1.sort(reverse=True, key=len)
# # print(value_1)
#
# value_1 = sorted(value_1, reverse=True, key=len)
# print(value_1)


# while
# break and continue
# while - else
# for
# for - else
# range()

######## Цикл ######### Loop

# while for
# value = 0
# is_true = True

# break continue
#
# while True:
#     value += 1
#     print(value)
#     if value > 10:
#         break
# else:
#     print("kkkkk")
#
#
# while is_true:
#     value += 1
#     print(value)
#     if value > 10:
#         is_true = False
# else:
#     print("kkkkk")
#
# print("ggggggg")


# while value < 10:
#     value += 1
#     if value % 2:
#         continue
#     print(value)


# value_list = [1, 2, 3]
# index = 0

# while index < len(value_list):
#     print(value_list[index])
#     index += 1

# for value in value_list:
#     print(value)

# range()
# range(9) від 0 до 9(виключно)0-8
# range(3, 9) 3-8
# range(3, 9, 2) 3 5 7 (з кроком 2)

# value_list = [1, 2, 3]
#
# for number in range(3, 9, 2):
#     print(number)


# value_str = 'apple'
value_list = ["a", "p", "l"]

# for letter in value_str:
#     print(letter)

# for index in range(len(value_list)):
#     print(index, value_list[index])

# enumerate()


# value_list = [1, 2, 3, 4]
#
# for index, letter in enumerate(value_list):
#     if index == 2:
#         continue
#     print(index, letter)
# else:
#     print("kkkkk")
#
# print("end")
