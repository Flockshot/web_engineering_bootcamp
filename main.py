import marshal

# print("Hello")
#
# # List funcs
#
# my_list = [1, 2, 9, 4, 5]
# print(my_list)
#
# print(my_list[0])
# print(my_list[1:3])
# print(my_list[::-1])
# print(my_list * 3)
#
# print(my_list.reverse())
# print(sorted(my_list))
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list))
# print(my_list.insert(0, 0))
# print(my_list.index(9))
#
# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9)
# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple[1:3])
# print(my_tuple[::-1])
# print(my_tuple * 3)
#
# print(my_tuple.count(9))
# print(my_tuple.index(9))
# print(my_tuple)
#
# x = (5) # int
# y = (5,) # tuple
# z = (5,6) # tuple
#
#
# x = int(input("Enter your start number: "))
# y = int(input("Enter your end number: "))
#
# if x < y:
#     for z in range(x, y+1):
#         if z % 2 == 0:
#             print(f"{z} is even")
#         else:
#             print(f"{z} is odd")

# for i in range(4):
#     while True:
#         marks = int(input(f"Enter subject {i + 1} marks: "))
#         if marks >= 0 and marks <= 100:
#             break
#         print("Invalid marks")

class Test1:
    def __init__(self):
        self.print_me()

    def print_me(self):
        print("Parent")

class Test2(Test1):

    def print_me(self):
        print("Child")







