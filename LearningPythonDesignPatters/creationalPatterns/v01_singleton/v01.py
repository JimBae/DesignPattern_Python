#=====================
# Classical singleton 
#=====================
#class Singleton(object):
#    def __new__(cls):
#        if not hasattr(cls, 'instance'):
#            cls.instance = super(Singleton, cls).__new__(cls)
#        return cls.instance
#
#s = Singleton()
#print ("Object created " , s )
#
#s1 = Singleton()
#print ("Object created " , s1 )

#=============================================
# Lazy instantiation in the singleton pattern
#=============================================
print "Lazy==============================="
class Singleton(object):
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance alreay created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
print ("Object created " , s )
print("Object created", Singleton.getInstance())
s1 = Singleton()
print ("Object created " , s1 )

#=============================================
# The Monostate Singleton pattern
#=============================================
print "Monnostate ==============================="

class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state

b = Borg()
b1 = Borg()
b.x = 4 

print("Borg Object 'b' : ", b)
print("Borg Object 'b1' : ", b1)
print("Object State 'b' : ", b.__dict__)
print("Object State 'b1' : ", b1.__dict__)

class Borg(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

b = Borg()
b1 = Borg()
b.x = 4 

print("Borg Object 'b' : ", b)
print("Borg Object 'b1' : ", b1)
print("Object State 'b' : ", b.__dict__)
print("Object State 'b1' : ", b1.__dict__)


#=============================================
# Singletons and metaclass
#=============================================
print "metaclass ==============================="

# A metaclass is a class of class, 
# which means that the class is an instance of its metaclass.

# name : This is the name of the class
# base : This is the base class
# dict : This is the attribute variable
#A = type(name, bases, dict)

# for Python 3.
#class MyInt(type):
#    def __call__(cls, *args, **kwds):
#        print("**** Here's my int ****", args)
#        print("Now do whatever you want with these object...")
#        return type.__call__(cls, *args, **kwds)
#
#class int(metaclass = MyInt):
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#i = int(4,5)
#
#class MetaSingleton(type):
#    _instances = {}
#    def __call__(cls, *args, **kwargs):
#        if cls not in cls._instances:
#            cls._instances[cls] = super(Metasingleton,cls).__call__(*args, **kwargss)
#        return cls._instances[cls]
#
#class Logger(metaclass = MetaSingleton):
#    pass
#logger1 = Logger()
#logger2 = Logger()
#print(logger1, logger2)





