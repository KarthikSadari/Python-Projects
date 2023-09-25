#day7
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
word_list = ["computer", "programming", "hangman", "python", "developer", "language", "variable", "function", "debugging", "algorithm", "software", "keyboard", "internet", "database", "framework", "iteration", "conditional", "operator", "debugging", "openai",
             "apple", "banana", "chocolate", "elephant", "fireplace", "giraffe", "hamburger", "island", "jazz", "kangaroo", "lighthouse", "mountain", "notebook", "octopus", "penguin", "quokka", "rainbow", "sunshine", "tiger", "umbrella", "volcano",
             "waterfall", "xylophone", "yacht", "zeppelin", "acoustic", "ballet", "carousel", "dolphin", "eclipse", "flamingo", "garden", "harmony", "iceberg", "jigsaw", "kiwi", "leopard", "marathon", "nautical", "ocean", "paradise", "quicksilver",
             "rhinoceros", "saxophone", "tropical", "unicorn", "vortex", "watermelon", "xylophone", "yogurt", "zephyr", "astronomy", "benevolent", "cantaloupe", "dandelion", "eccentric", "flourish", "gargoyle", "honeycomb", "illusion", "juxtapose", "kaleidoscope",
             "labyrinth", "magnificent", "nebulous", "oblivion", "paradox", "quixotic", "resplendent", "serendipity", "tranquility", "ubiquitous", "vivacious", "whimsical", "xenophile", "yesterday", "zenith"]

chosen_word = random.choice(word_list)


display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)

game_over = False
while not game_over:
    guessed_letter = input("\nGuess a Letter:--> ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
            if '_' not in display:
                print('You win!!')
                game_over = True
    print('\n',display)
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"\n  '{guessed_letter}' is Not in the Word!!")
        if lives == 0:
            print("\n You Lose!!")
            game_over = True
            print('The Word is -->',chosen_word)
    print(stages[lives])