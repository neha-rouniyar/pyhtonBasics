# #parameterized function(single parameter)
# def func1(name):
#     return f"Helllo,{name}"

# print(func1("HEllo world")) 


# #non parameterized
# def hie_cutie():
#     return "Hey Neha"
# print(hie_cutie())

# #parameterized function(multiple parameter)
# def sum(a,b):
#     c=a+b
#     return f"The sum is : {c}"
# print(sum(4,5))

# #function calling another function
# def fucn1():
#     return "Hey babe"

# def func2():
#    return fucn1()
# print(func2())

# #function returning multiple values
# def arithmetic_operations(a,b):
#     return a+b, a-b , a/b
# add,sub,div=arithmetic_operations(10,2)
# print(add,sub,div)

# #Understand return values and use them in functions.
# def square(num):
#     return num*num
# result=square(7)
# print(result)

# #using return value in another function
# def add(a,b):
#     return a+b
# def subtract(a,b,c):
#     result=add(a,b)
#     return result-c
# final_result=subtract(3,5,1)
# print(final_result)
    
# # lambda functions (these are anonymous functions that take any number of arguments and only a single expression)
# # syntax : lambda arguments:expression
# # for eg calculating cube of a number using lambda function
# cube=lambda a:a*a*a
# print(cube(2))
