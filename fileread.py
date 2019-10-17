import sys
import random


if len(sys.argv) < 2 :
    print("Please input name of flash card file.")
    exit(1)
    
fc_file = sys.argv[1]

count_dict = {}

f=open(fc_file, "r")

for line in f:
    entry = line.strip().split(",")
    question = entry[0]
    answer = entry[1]
    
    count_dict[question]= answer

f.close()

print("Welcome to the flashcard quizzer. Please type 'quit' anytime to exit the game")

questions = list(count_dict.keys())

while True:
    ques = random.choice(questions)
    ans = count_dict[ques]
    
    print("Question " + ques)
    print("Answer " + ans)
    user_input = input("Your guess : ")
    
    if user_input == "quit":
        break
    elif user_input.lower() == ans.strip().lower():
        print("Correct")
    else:
        print("Sorry, correct answer was" + ans)
        

























#f=open("countries.txt", "w")
#qn=input("Do you want to add any new country ?")
#if(qn=='y' or qn=='yes'):
#    qn=input("Enter the country name - ")
#    f.write(qn + "\n")
#else:
#    print("Thanks for reading the list..")

#f.close()