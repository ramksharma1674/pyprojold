state_capital={
    "MP" : "Bhopal",
    "UP" : "Lucknow",
    "Bihar" : "Patna",
    "Goa" : "Panjim",
    "Delhi" : "Delhi",
    "Rajasthan" : "Jaipur"
    }



import random

states = list(state_capital.keys())
for i in range(1,6):
    state = random.choice(states)
    capital = state_capital[state]
    
    answer = input("What is the capital of " + state + " ?\n")
    if answer.lower() == capital.lower():
        print("Awsesome")
    else:
        print("Ooops, capital of " + state + " is " + capital+"\n")

print ("All done")

#print(random.randint(1,101))

#movie={}
#movie["Akshay"]=["Padman"]

#print(movie)