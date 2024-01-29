# str
# str methods(lower, upper, capitalize, isalpha, rfind, replace, startwith)


# first_symbol = float(input("1st num:  "))
# operator = input("please tipe an operator(can work with +, -, *, /):  ")
# second_symbol = float(input("2nd num:  "))
#
# result = 0
#
# # if operator != "+" or operator != "-" or operator != "*" or operator != "/":
# # if operator not in "+-/*" or len(operator) != 1:
# # if operator not in ["+", "-", "*", "/"]:
# if operator not in ("+", "-", "*", "/"):
#     result = "invalid method"
# elif operator == "+":
#     result = first_symbol + second_symbol
# elif operator == "-":
#     result = first_symbol - second_symbol
# elif operator == "*":
#     result = first_symbol * second_symbol
# elif operator == "/" and second_symbol == 0:
#     result = "ERROR - can't divide by zero"
# elif operator == "/" and second_symbol != 0:
#     result = first_symbol / second_symbol
# # else:
# #     result = "invalid method"
#
# print(result)


# original_list = [12, 5, 6, 7, 8]
#
# if len(original_list) > 1:
#     # last_element = original_list.pop()
#     original_list.insert(0, original_list.pop())
#
# print(original_list)




# str
# str methods(lower, upper, capitalize, isalpha, rfind, replace, startwith)

# String

# value_str = "Hello"

# print(value_str, id(value_str))

# value_str = "Nick SOMETHING oooooo"

# print(value_str, id(value_str))

# value_caps = value_str.upper()
# value_low = value_str.lower()
# capital_value = value_str.capitalize()
# title_value = value_str.title()
# swapcase_value = value_str.swapcase()

# "email@gmail.com"
# "Email@gmail.com"


# print(value_int.isdigit())
# print(value_int.isalpha())

# value_int = "12hku khhllj;l444 4kw"
# new_value_int = ""
#
# for digit in value_int:
#     if not digit.isdigit():
#     # if digit.isalpha():
#         new_value_int += digit
#
# print(new_value_int)

# print(swapcase_value)

# print(value.find("2")) # значення -1 якщо нічого не знайдено
# print(value.find("l"))
# print(value.rfind("l"))

# print(value[0])
# print(value[0:5])
# print(value[5:])
# print(value[::2])
# print(value[:])
# print(value[::-1])




# value = "Helloloooooooooooooooooooooollo"
# element = "l"
# count = 0
# found_index = value.find(element)
# found_index = value.index(element)
# print(found_index)
#
# for letter in value:
#     if letter == "l":
#         count += 1
#
# print(count)
#
# while found_index != -1:
#     count += 1
#     found_index = value.find(element, found_index + 1)
#
# print(count)

# print(value.count("l"))

# strip()

# name = "Nick Hello"
# print(name)
# print(name.strip("_"))
# print(name.strip())
# print(name.rstrip("_"))
# print(name.lstrip("_"))

# replace()

# name = "image.png"
# idex = name.rfind(".")
# new_name = name[:idex] + ".jpeg"
#
# print(name)
# print(new_name)

# print(name)
# print(name.replace(".png", ".jpeg"))

# split() join()

# name_list = name.split("/", 2)

# name = "C/Documents/fol.der/image_1.png"
# # name_list = name.split(".", 1)
# name_list = name.rsplit(".", 1)
# # name_list = name.split("/")
#
# name_list[-1] = "jpeg"
# print(name_list)
#
# new_name = ".".join(name_list)
# print(new_name)


# startswith()

# value = "hello"
# request = "he"
#
# print(value.startswith(request))



################# ASCII ################### стандарт кодування


# alphabet = ""
#
# for index in range(ord("a"), ord("z") + 1):
#     print(index)
#     alphabet += chr(index)
#
# print(alphabet)

# letter = "a"
# ord()
# print(ord(letter))

# address = 100
#
# print(chr(100))





# import this
#
# print(this)






























