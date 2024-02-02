# tuple
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())



# my_list = [0, 9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# # for index in range(len(my_list)):
# #     if my_list[index] == 0:
# #         my_list.remove(0)
# #         my_list.append(0)
#
# my_list.sort(reverse=True, key=bool)
#
# # new_list = sorted(my_list, reverse=True, key=bool)
# #
# #
# print(my_list)
# # print(new_list)


# my_list = [0, 1, 7, 2, 4, 8]
# result = 0
#
# # if my_list:
# if len(my_list) > 1:
#     # for i in range(0, len(my_list), 2):
#     #     result += my_list[i]
#
#     result = sum(my_list[::2]) * my_list[-1]
#
# print(result)


# змінна "_"
# tuple
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())



# _ = "name"

# my_list = [1, 2]
# value_1, _ = my_list
# print(value_1)
# print(_)
#
#
# for _ in range(3):
#     print("llll")


############################## Tuple ######################################################## незмінний тип даних

# my_list = [
#     1,
#     2,
#     3,
#     9,
# ]
#
# my_tuple = (
#     1,
#     2,
#     3,
# )
#
#
# print(my_list, type(my_list))
# print(my_tuple, type(my_tuple))


# some_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# # print('some_tuple =', some_tuple.__sizeof__())
# # print('some_list =', some_list.__sizeof__())
#
# value_str = "hello"
#
# for index, letter in enumerate(value_str):
#     print(index, letter)


# some_tuple = (1, 2, 3)
# print(some_tuple, type(some_tuple))
#
# some_tuple[-1]. append(True)
#
# print(some_tuple, type(some_tuple))

# sum()
# max()
# min()



############### dict ################## змінний   ключ: значення

# my_dict = dict()
# my_dict = {"name": "Nick", "age": 18, "country": "Ukraine"}
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
#     1: "Ukraine",
#     1.3: "Ukraine",
#     True: "Ukraine1",
#     None: "Ukraine2",
#     (2, 2, 2): "blue",
# }
# print(hash(1.5))
# print(hash("name"))
# print(my_dict)

# print(my_dict["name"])
#
# my_dict["name"] = "Nikolas"
# my_dict["name_2"] = "John"

# print(my_dict["name"])
# email = my_dict.get("email", False)
# if not email:
#     print("this is mandatory field")

# print(email)



# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }

# for key in my_dict:
#     print(key, my_dict[key])

# for key in my_dict.keys():
#     print(key, my_dict[key])

# for val in my_dict.values():
#     print(val)

# for key, val in my_dict.items():
#     print(key, val)


# update()
# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
#
# value_pop = my_dict.pop("age")
#
# print(my_dict)
# print(value_pop)

# my_dict.update({"city": "Kyiv"})
# my_dict["city"] = "Kyiv"



# fromkeys
#
# some_dict = dict.fromkeys(("name", "age", "country"), [])
# print(some_dict)
# some_dict["name"].append(1)
# print(some_dict)


# some_dict = dict.fromkeys(("name", "age", "country"), False)
# print(some_dict)
# some_dict["name"] = "Nick"
# print(some_dict)

# popitem()
# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
#
# my_dict["city"] = "kkkkk"
#
# print(my_dict)
#
# value_pop = my_dict.popitem()
# print(my_dict)

# list comprehension

# some_list = []
#
# for num in range(5):
#     if num % 2:
#         some_list.append(num**2)

# some_list = [num ** 2 for num in range(5)]
# some_list = [num ** 2 for num in range(5) if num % 2]
#
# print(some_list)


# dict comprehension
#
# some_dict = {num: f"hello {num}" for num in range(5)}
# print(some_dict)

# OrderDict

# from collections import OrderedDict, defaultdict, namedtuple
#
# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
#
# print(my_dict)
#
# my_ordered_dict = OrderedDict(my_dict)       # [("name", "Nick"), ("age", 18), ("country", "Ukraine")]
# print(my_ordered_dict)

# fromkeys() vs defaultdict

# my_dict = defaultdict(list)
#
# for num in range(5):
#     my_dict[num].append(num * 5)
#
# print(my_dict)

# namedtuple
# from collections import namedtuple
#
# fields = ("color", "engine")
#
# car = namedtuple("Car", fields)
#
# car_1 = car("red", 2000)

# print(car_1)
# print(car_1.color)

# color, engine = car_1
#
# print(color)
# print(engine)











