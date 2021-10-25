## Dictionary
# people={"John":30,"Sac":20}
# print(people["John"])

# numbers = {
#      1:"one",
#      2:"two",
#      3:"three"
# }
# print(5 in numbers)
# print(numbers.get(5,"Key not found"))

## Tuples
# fruits = ("Apple","Mango","Peach")
# print(fruits[2])

## List Comprehension
# list = [x**2 for x in range(5) if x**2%2==0]
# print(list)

## String Formatting
# number=[1,2,3]
# newstring ="Numbers are - {0},{1},{2}".format(number[0],number[1],number[2])
# print(newstring)

##String Function
# print("/".join(["Apple","Peach","Banana"]))
# print("Hello There".replace("There","World"))
# print("Hello There".upper())

##Numeric Function 
# print(min(1,2,3,4,5))
# print(abs(-1))

## Lambda
# print((lambda x: x**2)(20))

## Map Function
# def add(x):
#     return x+2
# newlist=[1,2,3,4,5,6,7]
# reslt= list(map(add,newlist))
# print(reslt)

# newlist = [1,2,3,4,5]
# reslt =lambda x:x*2 
# print(list(map(reslt,newlist)))

## Filter Function with Lambda Function
newlist = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2==0,newlist)))