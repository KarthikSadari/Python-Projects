rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

****ROCK****
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

****PAPER****
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

****SCISSORS****
'''

 
game_imgs = [rock,paper,scissors]



def game(rock_paper_scissors):
    if user_choice >= 3 or user_choice < 0: 
      print("You typed an invalid number, you lose!")
    else:
        print(game_imgs[user_choice])

        import random

        computer_choice = random.randint(0,2)
        print("--- Computer's turn ---")
        print(game_imgs[computer_choice])


        if user_choice == 0 and computer_choice == 2:
          print("^^^ You win! ^^^")
        elif computer_choice == 0 and user_choice == 2:
          print("~~~ You lose ~~~")
        elif computer_choice > user_choice:
          print("~~~ You lose ~~~")
        elif user_choice > computer_choice:
          print("^^^ You win! ^^^")
        elif computer_choice == user_choice:
          print("___It's a draw___")

player_choice = True

while player_choice:
                
    player_choice = input("\n Press '-->SPACE BAR<--' and Enter to continue the game: ")
    if player_choice == ' ':
        user_choice = int(input("\t ### your's turn ### \n What do you choose? 0 for Rock , 1 fo Paper and 2 for Scissors: "))
        game(user_choice)
    else:
        player_choice = False
        print("~~~~~~THE END~~~~~~")
        
