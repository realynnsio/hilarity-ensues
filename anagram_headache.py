import random
import re

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def find_non_letters(x):
    res1 = re.findall("\W", x)
    return res1

def index_that_shit(someString):
    res1 = find_non_letters(someString)
    full_index_list = []

    for thing in res1:
        listIndexes = find(someString, thing)
        full_index_list.extend(listIndexes)

    full_index = list(set(full_index_list))
    full_index.sort(key=int)
    return full_index

def randomize_letters(x):
    x_list = list(x)
    randomized = ""
    z = len(x)
    for i in range(z):
        randomized += x_list[random.randrange(0, len(x_list))]
        x_list.pop(x_list.index(randomized[-1]))

    return randomized

sentence = input("Throw me a sentence baybee: ")
sentence_divided = re.split("\W", sentence)
anagram_list = []

for word in sentence_divided:
    anagram_list.append(randomize_letters(word))

anagram = "".join(list(filter(None, anagram_list))).capitalize()
final_anagram = list(anagram)
nonLetters = find_non_letters(sentence)
indexNonLetters = index_that_shit(sentence)

for i in range(len(nonLetters)):
    final_anagram.insert(indexNonLetters[i], nonLetters[i])

final_final_anagram = "".join(final_anagram).capitalize()

print(final_final_anagram)
