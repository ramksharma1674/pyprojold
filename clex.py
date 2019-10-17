import random
class die(object):
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)
    
d1 = die(18)

print(d1.roll())
print(d1.roll())    


class Greeter(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def hello(self):
        print("Hello " + self.name)
        print("You are " + self.age + " years old")
        
    def bye(self):
        print("Goodbye " + self.name)

g = Greeter("Ram", "20")

g.hello()
g.bye()

g1 = Greeter("Shyam", "30")

g1.hello()
g1.bye()
