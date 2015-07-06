# The computer must select a word at random from the list of words in the file /usr/share/dict/words

# Mystery word game:
# 1: Let the user choose a level of difficulty at the beginning of the program.
# Easy mode only has words of 4-6 characters;
# normal mode only has words of 6-8 characters;
# hard mode only has words of 8+ characters.
#
# 2: At the start of the game, let the user know how many letters the computer's word contains.
#
# 3: Ask the user to supply one guess (i.e. letter) per round.
# This letter can be upper or lower case and it should not matter.
# If a user enters more than one letter, tell them the input is invalid and let them try again.
#
# 4: Let the user know if their guess appears in the computer's word.
#
# 5: Display the partially guessed word, as well as letters that have not been guessed.
#
# A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
#
# A user loses a guess only when they guess incorrectly.
# If they guess a letter that is in the computer's word, they do not lose a guess.
#
# If the user guesses the same letter twice, do not take away a guess. Instead,
# print a message letting them know they've already guessed that letter and ask them to try again.
#
# The game should end when the user constructs the full word or runs out of guesses.
# If the player runs out of guesses, reveal the word to the user when the game ends.
#
# When a game ends, ask the user if they want to play again. The game begins again if they reply positively


import re
import random


def game_mode():
    # Selects the game mode and should pull in the mystery word depending on the mode
    users_choice = input("Please select [E]asy, [M]edium, or [H]ard: ").lower()

    with open("/usr/share/dict/words", 'r') as words:

        dict_list = words.read().lower()

        if users_choice[0] == 'e':

            the_mystery_words = re.findall(r"\b\w{4,6}\b", dict_list)
            # Using re.findall we are able to set boundary anchors with \b ,
            # then we search for words based on length with \w{'', ''}
            the_mystery_word = random.choice(the_mystery_words)
            return the_mystery_word
        elif users_choice[0] == 'm':

            the_mystery_words = re.findall(r"\b\w{6,8}\b", dict_list)
            the_mystery_word = random.choice(the_mystery_words)
            return the_mystery_word
        elif users_choice[0] == 'h':

            the_mystery_words = re.findall(r"\b\w{8,}\b", dict_list)
            the_mystery_word = random.choice(the_mystery_words)
            return the_mystery_word

        else:
            print("That was not a valid choice.")
            return game_mode()


def mystery_word_game(the_mystery_word):
    # This function is running the game
    guessed = ""
    guesses_remaining = int(8)
    valid_guesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    mystery_word_length = len(the_mystery_word)

    game_mystery_word = "_ " * len(the_mystery_word)
    print(" ".join(game_mystery_word))

    while guesses_remaining > (0):
        guess = input("Please guess a letter: ").lower()

        if guess not in valid_guesses or guess == int:
            print("That is not a valid guess. Please try again: ")

        elif guess not in guessed:
            guessed += guess
            user_guessed_word = " ".join(letter if letter in guessed else "_" for letter in the_mystery_word)
            # If the guessed letter is in the mystery word add it or if not continue fill blanks with "_"
            print("Mystery Word: ", user_guessed_word)

            for letter in guess:
                if "_" not in user_guessed_word:
                    print("YOU WIN!")
                    play_again = input("Would you like to play again? Y/N?: ").lower()
                    if play_again == 'y':
                        the_mystery_word = game_mode()
                        mystery_word_game(the_mystery_word)
                    else:
                        print("Thank you for playing MYSTERY WORD GAME!")
                        exit()
                elif letter in the_mystery_word:
                    print(guess + " is in your mystery word!")
                    print("Mystery Word: ", user_guessed_word)
                elif letter not in the_mystery_word:
                    guesses_remaining -= 1
                    print("Sorry, " + guess + " is not in your mystery word.")
                    print(guesses_remaining)

        elif guess in guessed:
            print("You have already guessed that letter. Please try again.")

    else:
        print("GAME OVER. Your mystery word was " + the_mystery_word.upper())
        play_again = input("Would you like to play again? Y/N?: ").lower()

    if play_again == 'y':
        the_mystery_word = game_mode()
        mystery_word_game(the_mystery_word)
    else:
        print("Thank you for playing MYSTERY WORD GAME!")

if __name__ == '__main__':
    the_mystery_word = game_mode()
    mystery_word_game(the_mystery_word)
