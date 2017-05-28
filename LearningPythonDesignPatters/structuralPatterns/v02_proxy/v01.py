#!/usr/bin/env python
# Written by: DGC

# http://sourcemaking.com/design_patterns/proxy
# give 4 good reasons for a proxy to be made.

# A virtual proxy is a placeholder for "expensive to create" objects. The real
# object is only created when a client first requests/accesses the object.
#
# A remote proxy provides a local representative for an object that resides in
# a different address space. This is what the "stub" code in RPC and CORBA 
# provides.

# A protective proxy controls access to a sensitive master object. The 
# "surrogate" object checks that the caller has the access permissions required
# prior to forwarding the request.

# A smart proxy interposes additional actions when an object is accessed. 
# Typical uses include: 
#   o Counting the number of references to the real object so that it can be 
#     freed automatically when there are no more references (aka smart pointer)
#   o Loading a persistent object into memory when it's first referenced,
#   o Checking that the real object is locked before it is accessed to ensure
#     that no other object can change it.


# The Proxy design pattern essentially does the following:
# - It provides a surrogate for another object so that you can control access to the original object
# - It is used as a layer or interface to support distributed access
# - It adds delegation and protects the real component from undesired impact


class Actor(object):
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print (type(self).__name__ , "is coccupied with current movie")

    def available(self):
        self.isBusy = False
        print (type(self).__name__, "is free for the movie")

    def getStatus(self):
        return self.isBusy

class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == '__main__':
    r = Agent()
    r.work()


