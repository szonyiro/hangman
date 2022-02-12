# import modules
import random  # module to generate random word from the list
from hangman_art import *  # module that contains the ASCII art
from hangman_words import *  # modula that contains the list of words
from replit import clear  # module to clear screen when running script


print(logo)
words_list = word_list
random_word = random.choice(words_list)
# print(f"Hint: {random_word}")  # prints out the random word for debug

# loop for creating blank spaces for the word to be guessed
display = []
for letter in random_word:
    display += "_"

# takes an input containing a letter, then checks if the letter
# is in the word or not.
lives = 6
end_of_game = False
while not end_of_game:
    print(" ".join(display))
    guess = input("Guess a letter: ")
    guess = guess.lower()
    clear()
    if guess in display:
        print(f"You already guessed letter {guess}.")
    # if the letter is in the word then replaces the blank space _ with the
    # guessed letter.
    for position in range(len(random_word)):
        letter = random_word[position]
        if guess == letter:
            display[position] = letter
    # if the letter is not in the word then takes a life away and prints a
    # statement.
    if guess not in random_word:
        lives -= 1
        print(f"You guessed letter {guess}, that's not in the word. You lose a life.")
    print(stages[lives].center(24, " "))
    # checks if all the blank spaces _ have been replaced. If yes, the game is over
    # and prints out You win!
    if "_" not in display:
        end_of_game = True
        print("You win!")
    # checks if all lives are lost. If yes, game is over and prints out You lose!
    if lives == 0:
        end_of_game = True
        print("You lose!")
        print(f"The word was: {random_word}")
