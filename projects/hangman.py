import random
import hangman_words
import hangman_art
import random


end_of_game = False


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
print(f"Chosen word is {chosen_word}")

display = []
stages_pos= len(hangman_art.stages)-1
for _ in chosen_word:
    display += "_"
print(display)
blanks=len(display)
blank_count=blanks

while not end_of_game:
    blanks=blank_count
    guess = input("Guess a letter ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter




    if guess not in chosen_word:

        if stages_pos == 0:
            end_of_game=True
            print("Gameover :/")

        else:
           print(f"You guessed {guess}, it's not in the word. You lose a life")
           stages_pos = stages_pos - 1

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You win")

    print(hangman_art.stages[stages_pos])
