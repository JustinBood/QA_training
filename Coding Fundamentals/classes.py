from abc import ABC, abstractmethod

class Student:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def average(self, score1, score2, score3):
        return (score1 + score2 + score3) / 3
    
    def __repr__(self):
        return f"Student name: {self.name}, Stufent age: {self.age}, Student class: {self.class_}"

student1 = Student("Justin", 20, "DevOps")
student2 = Student("Bob", 30, "Art")

avr1 = student1.average(20,90,70)
print(f"{student1.name} average is: {avr1}")


class Bird(ABC):

    def __init__(self, fly, colour):
        self.fly = fly
        self.colour = colour

    @abstractmethod
    def extinct(self):
        pass

class Owl(Bird):
    def __init__(self, fly, colour, head_rotation):
        super().__init__(fly, colour)
        self.head_rotation = head_rotation

        def extinct(self):
            if self.extinct:
                return True
            return False

class Dodo(Bird):
    def __init__(self, fly, colour, ext):
        super().__init__(fly, colour)
        self.extinct = ext
    
        def extinct(self):
            if self.ext:
                return True
            return False
