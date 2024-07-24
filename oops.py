def scope_test():
    def do_local():
        variable = "local variable"

    def do_nonlocal():
        nonlocal variable
        variable = "nonlocal variable"

    def do_global():
        global variable
        variable = "global variable"

    variable = "test variable"
    do_local()
    print("After local assignment:", variable)
    do_nonlocal()
    print("After nonlocal assignment:", variable)
    do_global()
    print("After global assignment:", variable)

scope_test()
print("In global scope:", variable)
class ClassName:
    def __init__(self, value):
        self.data = value  # Set based on the constructor argument

    def __str__(self):
        return f"ClassName with data: {self.data}"

class D_from_P(ClassName):
    def __init__(self, value):

        self.data = value  # Overwrite or set additional data if needed

    def __str__(self):
        return f"D_from_P with data: {self.data}"

    @staticmethod
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            print("Before")
            result = method(self, *args, **kwargs)
            print("After")
            return result
        return wrapper

    @decorator
    def to_decorate(self):
        print("Middle")

# Create an instance and test the methods
P = D_from_P(5)
print(P.__str__())  # Use the __str__ method
P.to_decorate()     # Call the decorated method
