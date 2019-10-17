name = "andy"
age = 42
likes = "Python"

print(f"We have a person names {name} who is {age} year old and love to code in {likes}")

def retr():
    return 2,22

a,b = retr()
print(a,b)

l={1,2,3,4,5,6}
e=enumerate(l)
print(e)

for i in e:
    print(i)
    
counter =0

while counter < 6:
    print("Hello" + str(counter))
    counter = counter + 1

counter =0
while True:
    print("Still true")
    print(counter)
    counter = counter+1
    if (counter > 5):
        break