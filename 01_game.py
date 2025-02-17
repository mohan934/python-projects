import random

# take input from user 
def guessgame(): # create a function first
    A = int(input("enter range minimum value:- ")) #here we take input from user for minimum value 
    B = int(input("enter range maximum value:- ")) #here we take input from user for maximum value

    if A > B:
        print("A cannot greater than B ")
        return
    
    secretnumber = random.randint(A,B) #select secreat number value between A and B
    attempt = 0   #count attempt

    print(f"\nI've select the random number between {A} and {B} can you guess it\n")

    #here we applay guessing loop
    while True:
        try:
            guess = int(input("enter number : -")) #ask to user for number guessing
            attempt += 1 #count guessing number attempt from user
            if guess > secretnumber:
                print("number is too high")
            
            elif guess < secretnumber:
                print("number is too low")
               
            elif guess == secretnumber:
                print(f"congratulation you guess correct {secretnumber} value in {attempt} attempts")
                break  #find true value then break statement
            else:
                print(f"enter a value between {A} and {B}") # if user enters value not between A and B
        except ValueError: #if user enter non interger value 
            print("enter an integer value ")


guessgame() #call above function
