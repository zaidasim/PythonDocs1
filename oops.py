def scope_test():
    def local():
        variable = "local variable"

    def non_local():
        nonlocal variable
        variable = "nonlocal variable"

    def glob_al():
        global variable
        variable = "global variable"

    variable = "test variable"
    local()
    print("After local assignment:", variable)
    non_local()
    print("After nonlocal assignment:", variable)
    glob_al()
    print("After global assignment:", variable)

scope_test()
print("In global scope:", variable)




#inheritance is a way that 1 class is derived from the second class so that class 1 can use its protected (_method) and public methods and variables directly

class ClassName:

    def __init__(self, value):
        self.data = value  # Set based on the constructor argument

    def __str__(self):
        return f"ClassName with data: {self.data}"
    
    def _protected_method(self):
        print("This is a protected method")

    def public_method(self):
        print("This is a public method")

class D_from_P(ClassName):#inheritence
    def __init__(self, value):

        self.data = value  # Overwrite or set additional data if needed

    def __str__(self):
        return f"D_from_P with data: {self.data}"
    def access_methods(self):
        self._protected_method()  
        self.public_method()      
   
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            print("Before")
            result = method(self, *args, **kwargs)
            print("After")
            return result
        return wrapper

    @decorator# decorator is a nested function that is used to de something before and after the function call
    def to_decorate(self):
        print("Middle")

# Create an instance and test the methods
P = D_from_P(5)
print(P.__str__())  # Use the __str__ method
P.to_decorate()     # Call the decorated method


#Abstraction is defining a base abstract class  and a virtual function, which defines an informal blue print to follow
class Shape:
  
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

circle = Circle(5)
square = Square(4)

print(circle.area())  
print(square.area())  
#Polymorphism is a way in which  the compiler automatically calls  functions that are of same name depending on object of the class
class Bird:
    def fly(self):
        print("Bird does")

class Aeroplane:
    def fly(self):
        print("Aeroplane does")

def flies(can_fly):
    can_fly.fly()

bird = Bird()
plane = Aeroplane()

flies(bird)  
flies(plane) 
#Encapsulation is a phenomenon in which class's members are made private with (__) at start making it fixed with in the class and only the same class members can access it
class Car:
    def __init__(self, making, wheels):
        self.making = making       
        self.__wheels = wheels   # here wheels is private and can only be accessed by a private member function and not  by it self

    def get_wheels(self):
        return self.__wheels

    def set_wheels(self, wheels):
        self.__wheels = wheels

meri_car = Car("Mehran", "2 wheeler")
print(meri_car.making)            
print(meri_car.get_wheels())  
#   print(meri_car.__wheels) ''''It is not allowed and will result in an error
print(meri_car._Car__wheels)