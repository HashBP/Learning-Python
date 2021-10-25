##  OOPS ##

##Class
# class teddy:
#     quantity = 200
# teddy1=teddy()
# teddy2=teddy()
# print(teddy1.quantity)
# teddy2.quantity=20
# print(teddy2.quantity)

# ##Instance Attribute Constructor
# class teddy:
#     quantity = 200

#     def __init__(self,name,color):     #Constructor
#         self.color=color
#         self.name=name
# ** self is reference to self object or simply it is a convenction to name the parent class.
# teddy1=teddy("Ted","Pink")
# print(teddy1.name)
# print(teddy1.color)
# teddy2=teddy("Ron","Red")
# print(teddy2.name)
# print(teddy2.color)

## OOPS way of writing code and Inheritance
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_data(self):
#         self.name = input("Please Enter Name")
#         self.age = input("Please Enter Age")

#     def put_data(self):
#         print(self.name)
#         print(self.age)

# st1=Student("","")
# st1.get_data()
# st1.put_data()

# class ScienceStudent(Student):
#     def science(Self):
#         print("Hii")S
# a=ScienceStudent("","")
# a.get_data()

# # # # # # # # # # # # # # # # # # # # # # # # # # # #
## Sets
# numbers = {1, 3, 4, 5, 6, 7, 8, 9, 0}
# numbers.add(2)
# print(numbers)
# numbers.remove(2)
# print(numbers)

# setA = {1, 2, 3, 4, 5}
# setB = {4, 5, 6, 7, 8, 9}
# print(setA | setB)
# print(setA & setB)

## Itertools
from itertools import count
for i in count(3):
    print(i)
    if i>=20:
        break
# from itertools import accumulate,takewhile
# number=list(accumulate(range(8)))
# print(number)
# print(list(takewhile(lambda x: x<=6,number)))