#!/usr/bin/python
# -*- coding: utf-8 -*-

#================================
# A simple static factory method
#================================

#from __future__ import generators
#import random
#
#class Shape(object):
#    #Create based on class name
#    def factory(type):
#        # return eval(type + "()")
#        if type == "Circle": return Circle()
#        if type == "Square": return Square()
#        assert 0, "Bad shape creation: " + type
#    factory = staticmethod(factory)
#
#class Circle(Shape):
#    def draw(self): print("Circle.draw")
#    def erase(self): print("Circle.erase")
#
#class Square(Shape):
#    def draw(self): print("Square.draw")
#    def erase(self): print("Square.erase")
#
## Geneate shape name strings:
#def shapeNameGen(n):
#    types = Shape.__subclasses__()
#    for i in range(n):
#        yield random.choice(types).__name__
#
#shapes = [ Shape.factory(i) for i in shapeNameGen(7)]
#
#for shape in shapes:
#    shape.draw()
#    shape.erase()


#================================
# Preventing direct creation
#================================
#import random
#
#class Shape(object):
#    types = []
#
#def factory(type):
#    class Circle(Shape):
#        def draw(self): print("Circle.draw")
#        def erase(self): print("Circle.erase")
#
#    class Square(Shape):
#        def draw(self): print("Square.draw")
#        def erase(self): print("Square.erase")
#
#    if type == "Circle": return Circle()
#    if type == "Square": return Square()
#    assert 0, "Bad shape creation: " + type
#
#def shapeNameGen(n):
#    for i in range(n):
#        yield factory(random.choice(["Circle", "Square"])
#
#for shape in shapeNameGen(7):
#    shape.draw()
#    shape.erase()


#================================
# Polymorphic Factories
#================================

from __future__ import generators
import random

class ShapeFactory:
    factories = {}
    def addFactory(id, shapeFactory):
        ShapeFactory.factories.put[id] = shapeFactory
    addFactory = staticmethod(addFactory)
    # A Template Method:
    def createShape(id):
        if not ShapeFactory.factories.has_key(id):
            ShapeFactory.factories[id] = \
              eval(id + '.Factory()')
        return ShapeFactory.factories[id].create()
    createShape = staticmethod(createShape)

class Shape(object): pass

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")
    class Factory:
        def create(self): return Circle()

class Square(Shape):
    def draw(self):
        print("Square.draw")
    def erase(self):
        print("Square.erase")
    class Factory:
        def create(self): return Square()

def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [ ShapeFactory.createShape(i)
           for i in shapeNameGen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()


#================================
# Abstract Factories
#================================

class Obstacle:
    def action(self): pass

class Character:
    def interactWith(self, obstacle): pass

class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a",
        obstacle.action())

class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a",
        obstacle.action())

class Puzzle(Obstacle):
    def action(self):
        print("Puzzle")

class NastyWeapon(Obstacle):
    def action(self):
        print("NastyWeapon")

# The Abstract Factory:
class GameElementFactory:
    def makeCharacter(self): pass
    def makeObstacle(self): pass

# Concrete factories:
class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self): return Kitty()
    def makeObstacle(self): return Puzzle()

class KillAndDismember(GameElementFactory):
    def makeCharacter(self): return KungFuGuy()
    def makeObstacle(self): return NastyWeapon()

class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()
    def play(self):
        self.p.interactWith(self.ob)

g1 = GameEnvironment(KittiesAndPuzzles())
g2 = GameEnvironment(KillAndDismember())
g1.play()
g2.play()





# Simplified Abstract Factory.

class Kitty:
    def interactWith(self, obstacle):
        print("Kitty has encountered a",
        obstacle.action())

class KungFuGuy:
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a",
        obstacle.action())

class Puzzle:
    def action(self): print("Puzzle")

class NastyWeapon:
    def action(self): print("NastyWeapon")

# Concrete factories:
class KittiesAndPuzzles:
    def makeCharacter(self): return Kitty()
    def makeObstacle(self): return Puzzle()

class KillAndDismember:
    def makeCharacter(self): return KungFuGuy()
    def makeObstacle(self): return NastyWeapon()

class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()
    def play(self):
        self.p.interactWith(self.ob)

g1 = GameEnvironment(KittiesAndPuzzles())
g2 = GameEnvironment(KillAndDismember())
g1.play()
g2.play()






#from abc import ABCMeta, abstractmethod
#
#class Animal():
#    __metaclass__ = ABCMeta
#
#    @abstractmethod
#    def do_say(self):
#        pass
#
#class Dog(Animal):
#    def do_say(self):
#        print("Bhow Bhow!!")
#
#class Cat(Animal):
#    def do_say(self):
#        print("Meow Meow!!")
#    
#class ForestFactory(object):
#    def make_sound(self, object_type):
#        return eval(object_type)().do_say()
#
### client code
#if __name__ == '__main__':
#    ff = ForestFactory()
#    animal = input("Which animal should make_sound Dog or Cat?")
#    ff.make_sound(animal)


