import random
import requests


def get_random_word_from_api():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return results[0]
    else:
        return None


def show_existing_letter(placeholder, word, letter):
    placeholder = list(placeholder)
    for i in range(len(word)):
        if word[i] == letter:
            placeholder[i] = letter
    return "".join(placeholder)


def hungman(word):
    print("H A N G M A N")
    attempts = 8
    placeholder = "-"*len(word)
    used_letters = set()
    while attempts > 0:
        if placeholder == word:
            return True
        else:
            print(f"\n{placeholder}")
        letter_guess = input(f"Input a letter: > ")
        if len(letter_guess) != 1:
            print("Please, input a single letter.")
        elif not letter_guess.isalpha() or letter_guess.isupper():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter_guess in used_letters:
            print("You've already guessed this letter.")
        elif letter_guess not in word:
            attempts -= 1
            used_letters.add(letter_guess)
            if attempts != 0:
                print("That letter doesn't appear in the word.")
        else:
            used_letters.add(letter_guess)
            placeholder = show_existing_letter(placeholder, word, letter_guess)
        if attempts != 0:
            print(f"You have {attempts} attempts left")
    return False


if __name__ == "__main__":
    menu = "Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: > "
    order = input(menu)
    wins, losses = 0, 0
    while True:
        if order == "exit":
            break
        elif order == "results":
            print(f"You won: {wins} {'times' if wins > 1 else 'time'}")
            print(f"You lost: {losses} {'times' if losses > 1 else 'time'}")
            order = input(menu)
        elif order == "play":
            word = get_random_word_from_api()
            if hungman(word):
                wins += 1
                print(f"You guessed the word {word}!")
                print("You survived!")
                order = input(menu)
            else:
                losses += 1
                print("You lost!")
                order = input(menu)
        else:
            print("Please, enter a valid command")
            order = input(menu)
    print("thnak you for playing!")
