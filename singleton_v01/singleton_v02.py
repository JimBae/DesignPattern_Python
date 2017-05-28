#!/usr/bin/python

import os, sys

# To avoid this limitation, 
# Alex Martelli proposed an alternative implementation based on shared state called Borg.

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass(Borg):
    a = 1

one = MyClass()
two = MyClass()
two.a = 3
print one.a

class MyOtherClass(MyClass):
    b=2

three = MyOtherClass()
print three.b
print three.a

three.a = 2
print one.a
