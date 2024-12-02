# # simple concept of object and class
# class Person:
#     def __init__(self,name1,age1):
#         self.name2=name1
#         self.age2=age1

#     def greet(self):
#         print(f"Hello guys. My anme is {self.name2} and i am {self.age2} years old ")
# neha=Person("Neha",22)
# neha.greet()

# ***********************************************************************************************************************************************

# # example for arithmetic operation
# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b

# calc=Calculator()
# print(calc.add(4,6))
# print(calc.mul(4,6))

# ***********************************************************************************************************************************************


# # understanding the concept of inheritance - it allows a class to inherit attributes from the parent class 
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print(f"{self.name} is eating")

# class Dog(Animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed=breed
#     def bark(self):
#         print(f"{self.name} is barking")
        
# dogobj=Dog("Kalu","Kukur")
# dogobj.bark()
# dogobj.eat()

# print(f"My dog name is {dogobj.name} and it is {dogobj.breed} breed")

# ***********************************************************************************************************************************************

