# ZD_3

from abc import ABC, abstractmethod

class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass

class MyObject(Prototype):
    def __init__(self, agr1, agr2):
        self.field1 = agr1
        self.field2 = agr2

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        obj = MyObject(self.field1, self.field2)
        obj.performed_operation = self.performed_operation
        return obj

a = MyObject(5,10)
b = MyObject(4,7)
b.clone() ???