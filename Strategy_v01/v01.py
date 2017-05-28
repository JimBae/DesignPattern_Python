#!/usr/bin/python

from abc import ABCMeta, abstractmethod
from collections import namedtuple
      
Customer = namedtuple( 'Customer', 'name fidelity' )

class LineItem:

    def __init__( self, product, quantity, price ):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total( self ):
        return self.price * self.quantity

# the Context
class Order:

    def __init__( self, customer, cart, promotion=None ):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total : {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

# the Strategy: an Abstract Base Class
class Promotion:
    __metaclass__ = ABCMeta

    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""

# first Concrete Strategy
class FidelityPromo(Promotion):
    """ 5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

# second Concrete Strategy
class BulkItemPromo(Promotion):
    """ 10% discount for each LineItem with 20 or more units"""
    
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

# third Concrete Strategy
class LargeOrderPromo(Promotion):
    """ 7% discount for orders with 10 or more distinct items"""
    
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0

## Example
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('apple', 10, 1.5),
        LineItem('banana', 10, 0.5),
        LineItem('watermellon', 5, 5.0)]

orderObj = Order(joe, cart, FidelityPromo())
print(orderObj)

orderObj = Order(ann, cart, FidelityPromo())
print(orderObj)

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]

orderObj = Order(joe, banana_cart, BulkItemPromo())
print(orderObj)

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

orderObj = Order(joe, long_order, LargeOrderPromo())
print(orderObj)

orderObj = Order(joe, cart, LargeOrderPromo())
print(orderObj)




# Test for __repr__, __str__
#class Foo(object):
#    def __init__(self, bar):
#        self.bar = bar
#    def __repr__(self):
#        return "<Foo bar:%s>"%self.bar
#    #def __str__(self):
#    #    return "<Foo bar:%s>"%self.bar
#fooObj = Foo(42)
#print(fooObj)


#class Vector2d:
#    typecode = 'd'
#
#    def __init__(self, x, y):
#        self.__x = float(x)
#        self.__y = float(y)
#
#    @property
#    def x(self):
#        return self.__x
#
#    @property
#    def y(self):
#        return self.__y
#
#    def __iter__(self):
#        return (i for i in (self.x, self.y))

    


