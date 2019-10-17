from temp import to_celcius
import random

c= to_celcius(70)
print (c)
number, number2, number3 = random.random(), random.randint(1,6), random.randrange(100,500,5)
#print("number=", random.random())
#number2 = random.randint(1,6)
#number3 = random.randrange(100,500,5)

print (number)
print (number2)
print (number3)

list1 = ["123", "456", 4 , 6.7, -1]

print(list1)

list1.append("Ram")

print(list1)

list1.reverse()

print(len(list1))

for item1 in list1:
    print (item1)