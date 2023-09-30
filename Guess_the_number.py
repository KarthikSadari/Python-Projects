#guess the number
from random import randint

easy_level_turns = 10
hard_level_turns = 5

def check_answer(guess,answer,turns):
    if guess>answer:
        print("too high")
        return turns - 1
    elif guess<answer:
        print("too low")
        return turns - 1
    else:
        print(f"you got it the answer is {answer}.")
def set_difficulty():
    level = input("choose easy or hard: ")
    if level == 'easy':
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    
    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts reamining to guess the number")
        
        guess = int(input("guess a number: "))
        
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("you've run out of guesses,you lose.")
            print(f"the correct answer is {answer}.")
            return
        elif guess != answer:
            print("guess again.")
            
game()