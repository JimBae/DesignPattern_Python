#!/usr/bin/python

class Singleton(object):

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
print one.a
two = MyClass()
two.a = 3
print one.a

# Limitation
class MyOtherClass(MyClass):
    b = 2
three = MyOtherClass()
# Error
#print three.b






