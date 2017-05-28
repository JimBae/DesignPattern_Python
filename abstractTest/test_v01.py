import os,sys
from abc import ABCMeta, abstractmethod

class AbstractAnimal(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        pass

# Error!!!
#class Dog(AbstractAnimal):
#    pass

class Dog(AbstractAnimal):
    def run(self):
        print "running like a dog..."


obj = Dog()

