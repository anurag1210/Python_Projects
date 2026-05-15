# class SomeClass:
#     print('This is done')

# SomeClass()#Shows the memory location of the Class 

# Class:
# A class is a blueprint used to create objects.

# self:
# In instance methods, especially __init__, self refers to the current object
# or this specific instance.

# __init__:
# __init__ is used to initialize an object after it is created.

# Return value of __init__:
# __init__ should not explicitly return anything.
# It implicitly returns None, like any Python function with no return statement.

# isinstance()
# Checks whether an object belongs to a given type or class.
# Returns True or False.
# Safer than type() when inheritance is involved.
#
# Example:
# isinstance(5, int) -> True
# isinstance("hi", str) -> True



class Rectangle:
    def __init__(self, width,height):
        self.width=width
        self.height=height


rectangle=Rectangle(13,15)
print(rectangle.width)
print(rectangle.height)


#Using isInstance to check the datatypes in the class is compatible with the values 


# class Rectangle:
#       def __init__(self,width,height):
#            if not(isinstance(width,(int,float)) and width >0):
#                 raise ValueError(f"positive width expected , got {width}")
#            self.width=width
#            if not(isinstance(height,(int,float)) and height >0):
#                 raise ValueError(f"positive height expected, got {height}")
#            self.height=height



rectangle=Rectangle(-21,42)



#Using super 
# super() is used in a child class to call methods from the parent class,
# most commonly the parent's __init__(). This helps reuse parent logic
# and avoids rewriting the same initialization code.


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate


class Teacher(Person):
    def __init__(self, name, birthdate):
        super().__init__(name, birthdate)
        print(f"The Teacher name is {name} and birthdate is {birthdate}")


class Student(Person):
    def __init__(self, name, birthdate):
        super().__init__(name, birthdate)
        print(f"The Student name is {name} and birthdate is {birthdate}")


anurag = Student("Anurag", "2001-02-07")


#Default Argument 

# This example shows how default argument values make class initializers
# more flexible. They let you create objects with different sets of
# arguments depending on what you need.


class Greeter:
    def __init__(self, name, formal=False):
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print(f"Good morning, {self.name}!")
        else:
            print(f"Hello, {self.name}!")

informal_greeter = Greeter("Pythonista")
informal_greeter.greet()
formal_greeter = Greeter("Pythonista", formal=True)
formal_greeter.greet()