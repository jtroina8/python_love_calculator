import time
import random

print('''
LOVE CALCULATOR

In love? We’ve all been there. Have you tried asking them? Of course not!
You’ve come to the right place.
I’ll tell you how compatible you two are!
''')
resultsDic = [
    "%: Absolutely no chance. Like ever... ever ever. I'm literally mad you asked about this and I'm a bot.\n",
    "%: Yeeeeeaaaaaahhhhhhhhh—nnnnnooooo.\n",
    "%: I’d be surprised if you even to the friend zone.\n",
    "%: I mean, if this was a school grade, it’d only be like a F minus minus... minus?\n",
    "%: I mean… not TERRIBLE... definitely not good though.\n",
    "%: I don't know if I absolutely hate this, or just like it a little bit?\n",
    "%: At least you’re on the positive side! I’ll give it a Potential2Grow sticker.\n",
    "%: I definitely see sparks. ;)\n",
    "%: You’re either on the first date, or in the Best-Friend stage. Keep at it.\n",
    "%: Yaaaaassssssss!!! This. Just. This.\n",
    "%: RED ALERT! RED ALERT! THESE TWO ARE FIRE TOGETHER!!\n",
    "%: < 3 Always + Forver < 3\n"
]

range_score = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99, 100]


play_again = True

while play_again:

    user1 = input("What is your name? ").lower()
    user2 = input("What is the name of the person you love? ").lower()

    score = 0
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = ["b", "c", "d", "f", "g", 'h', 'j', 'k', 'l', 'm',
                  'n', 'l', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vowels_in_user1 = 0
    vowels_in_user2 = 0

    user1_letters = []
    user2_letters = []

    for letter in user1:
        user1_letters.append(letter)
    for letter in user2:
        user2_letters.append(letter)

    # both names have the same amount of consonants/vowels

    def letters(user1, user2, the_letters):
        user1_consonants = {}
        user2_consonants = {}
        global score
        for character in user1:
            if character in the_letters:
                try:
                    user1_consonants[user1] += 3
                except KeyError:
                    user1_consonants[user1] = 3
        for character in user2:
            if character in the_letters:
                try:
                    user2_consonants[user2] += 3
                except KeyError:
                    user2_consonants[user2] = 3
        for key in user1_consonants:
            if key in user2_consonants:
                score += min([user1_consonants[key], user2_consonants[key]])

        user1_vowels = {}
        user2_vowels = {}
        for character in user1:
            if character in the_letters:
                try:
                    user1_vowels[user1] += 3
                except KeyError:
                    user1_vowels[user1] = 3
        for character in user2:
            if character in the_letters:
                try:
                    user2_vowels[user2] += 3
                except KeyError:
                    user2_vowels[user2] = 3
        for key in user1_vowels:
            if key in user2_vowels:
                score += min([user1_vowels[key], user2_vowels[key]])

    letters(user1, user2, consonants)
    letters(user1, user2, vowels)

    # if both names start with the same letter
    if user1[0] == user2[0]:
        score = score + 10

    # if first letter in user 2 is in user1 name
    if user2_letters[0] in user1_letters:
        score = score + 8

    # if the names have the same amount of characters
    if len(user1) == len(user2):
        score = score + 15

    # if both users name has an L O V or E in it
    for letter in user1:
        if letter in "love":
            score += 3
            break

    for letter in user2:
        if letter in "love":
            score += 3
            break

    # gives a random amount of points to make result different every time
    final_score = random.randint(0, 50) + score

    # cap the score to 100
    if final_score > 100:
        final_score = 100

    print("\nCalculating...\n")
    time.sleep(3)

    def findIndex(flist, func):
        for i, v in enumerate(flist):
            if func(v):
                return i
        return -1

    def response_result(score, response_text):
        print("\n" + str(score) + response_text)

    def result():
        index_of_result = findIndex(range_score, lambda i: i <= final_score)

        result_text = resultsDic[index_of_result]
        response_result(final_score, result_text)

    result()

    # "play again" feature
    again = str(input(
        "The stars have shifted! Your fate could have changed! Would you like to try again? "))
    if again not in ("yes", "Y", "y"):
        play_again = False
