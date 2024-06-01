import random
from hangman_words import word_list
from hangman_arts import stages, logo


print(logo)
# Randomly choose a word from the list of words and store
chosen_word = random.choice(word_list)

# Number of lives = 6
lives = 6

# Empty list 
display = []

# Create number of dashes as in the chosen_word in a list 
for letter in chosen_word:
    display += "_"

end_of_game = False

while not end_of_game:
    # Ask a user to guess a letter
    guess = input("guess a letter:").lower()

    if guess in display:
        print(f"Youve already guessed {guess}")

    # Check if the letter is in the the chosen word and replace the "_" position in the list
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    # Check for wrong guesses
    # Not under for loop because you dont want to end it while counting number of positions 
    # You only want to end it when guesses are wrong 6 times
    if guess not in chosen_word:
        print(f"You guessed {guess} that is not in the word; You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])