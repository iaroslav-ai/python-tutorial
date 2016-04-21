# class declaration
class MyClass():
    def __init__(self, value):
        # this is how to define new class field
        self.var = value
    def myfunction(self, arg):
        self.arg = arg
        return self.var + " " + self.arg

cls = MyClass("hello")
print cls.myfunction("world")