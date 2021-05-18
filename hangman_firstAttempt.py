import random
from nltk.corpus import words

dictionary = words.words()


def hangman(someString, letterInput):
    string_list = list(set(list(someString)))
    if len(letterInput) == 1:
        if letterInput in string_list:
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False
    else:
        print("Only insert one letter at a time!")
        return False


def state_of_things(word, guess):
    word_list = list(word)
    guess_list = list(guess)
    empty_list = []

    for letter in word_list:
        if letter in guess_list:
            empty_list.append(letter)
        else:
            empty_list.append("_")

    joined_list = "".join(empty_list)
    print(joined_list)


guessWord = dictionary[random.randrange(0, len(dictionary))]

correctAnswers = 0
correctLetters = len(list(set(list(guessWord))))
guessLimit = correctLetters + 7
guesses = ""

state_of_things(guessWord, guesses)

while correctAnswers < correctLetters and guessLimit > 0:
    letter = input("Input a letter: ").lower()

    if hangman(guessWord, letter):
        if letter in guesses:
            pass
        else:
            correctAnswers += 1
        guesses += letter
        state_of_things(guessWord, guesses)
    else:
        state_of_things(guessWord, guesses)

    guessLimit += -1

    if correctAnswers < correctLetters:
        if guessLimit != 1:
            print(f"You have {guessLimit} guesses left.")
        else:
            print(f"You have 1 guess left.")
    else:
        pass

    print("")


if correctAnswers == correctLetters:
    print("You won!")
elif guessLimit == 0:
    print(f"The word was '{guessWord}'.")
    print("Better luck next time!")
