from typing import overload

class Animal():
    def __init__(self, name, age):
        print("Parent class")
        self.name = name
        self.age = age        
    
    def makeSound(self, sound):
        print("making a sound {}".format( sound))
    
class Dog(Animal):
    def __init__(self):
        pass
        
    def makeSound(self, sound):
        print("making a child sound {}".format( sound))    
    
    def doWalk(self):
        print("Walking")

dog = Dog()
dog.doWalk()