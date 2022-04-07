# /package/module.py

class Example_class():

    def __init__(self):
        print("example_class instance loaded")
        self.attribute = False

    def example_method1(self):
        print("example_method executed")
        self.attribute = True
        return self.attribute

    def example_method2(self):
        print("example_method2 executed")
        if self.attribute == True:
            raise Exception('example_method1 was already executed')
        else:
            return self.example_method1()


def method():
    print("method executed")
