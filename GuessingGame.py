#Sam
#This is a guessing numbers game!

#Let's choose a starting number and an ending number!
start = 1
end = 10

#We have to teach the computer how to chose a random
#Number!
import random
computers_num = random.randint(start,end)

#Lets get user input!

tries = 5
for i in range(0,tries):
                guess = int(input("Guess a number between %s and %s!" %(start,end)))
#Recall our if statements from last class!
if guess == computers_num: #The question marks won't work!
                print("The computer chose %s, you chose %s" %(computers_num, guess))
elif guess < computers_num:
                print("Your number is too low!")
elif guess > computers_num:
                print("Your number is too high!")
#TO run multiple times we will use a for loop!               
                
