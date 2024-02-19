# text = "When I was One I had just begun When I was Two I was nearly new"
# words = ['i', 'was', 'three', 'near']
#
#
# # def popular_words(text: str, words: list) -> dict:
# def popular_words(txt, wrds):
#     text_words = txt.lower().split()
#
#     # # popular_dict_words = {word: 0 for word in words}
#     popular_dict_words = {}
#
#     # # for word in text_words:
#     # #     if word in words:
#     # #         popular_dict_words[word] = text_words.count(word)
#
#     for word in wrds:
#         popular_dict_words[word] = text_words.count(word)
#     #
#     # popular_dict_words = {word: text_words.count(word) for word in words}
#     #
#     return popular_dict_words
#     # return {word: text.lower().split().count(word) for word in words}
#
#
# print(popular_words(text, words))

# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')



# def difference(*numb_args):
#     if numb_args:
#         result = max(numb_args) - min(numb_args)
#         return round(result, 2)
#         # return round((max(numb_args) - min(numb_args)), 2)
#
#     return 0
#
#
# def difference(*numb_args):
#     if not numb_args:
#         return 0
#
#     result = max(numb_args) - min(numb_args)
#     return round(result, 2)
#
# print(difference(5, -5))

# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')


############### Works With File   #############

# write
# filename = "test.txt"

# my_file = open(filename, "w")  # "w", "r", "a"
#
# my_file.write("Hello World!\n")
# my_file.write("Hello World!\n")
# my_file.write("Hello World!\n")
#
# my_file.close()


# with open(filename, "w") as my_file:
#     my_file.write("Hello World!\n")





# writelines

# val_list = ["hello World\n", "red\n", "green", "yellow"]
# val_list = ["hello World", "red", "green", "yellow"]
#
# filename = "tmp/test.txt"
#
# my_file = open(filename, "w")  # "w", "r", "a"
# for i in val_list:
#     my_file.writelines(i + "\t")
#
# my_file.close()

# val_list = ["hello World", "red", "green", "yellow"]
#
#
# with open(filename, "w") as my_file:
#     for i in val_list:
#         my_file.writelines(i + "\n")

########## read


filename = "test.txt"
#
# my_file = open(filename, "r")  # "w", "r", "a"
#
# data = my_file.read()
#
# my_file.close()
#
# print(data, type(data))


# with open(filename, "r") as my_file:
#     data = my_file.read()
#
# print(data, type(data))


# with open(filename, "r") as my_file:
#     data = my_file.readlines()

# with open(filename, "r") as my_file:
#     data = my_file.readline()
#     # print(my_file.readline())

# print(data, type(data))


# with open(filename, "a+") as my_file:
#     data = my_file.write("\n!!!!!!!!!!")
#
#     my_file.seek(4)
#     ctx = my_file.read()
#
# print(ctx)

# with open(filename, "rb") as my_file:  # read binary file
#     data = my_file.readlines()

# with open(filename, "r", encoding="UTF-8") as my_file:  # read binary file
#     data = my_file.readlines()




########### OOP ################


# class Car:
#     """Some doc string"""
#     color = "green"   # атрибут
#     engine = 2.0
#
#
# car_1 = Car()     # екземпляр(instance)/обʼєкт класу
# car_2 = Car()
#
# # print(car_1)
# # print(car_1.color)
# car_1.color = "red"
# car_1.body = "sedan"
# # print(car_1.color)
# print(car_1.body)      # атрибут екземпляра класу
# # print(car_2.body)
# # print(car_2.color)
#
#
# value_str = "test"
# # value_str.join()
# # print(type(value_str))








