import random

def word_game(words):
    random.shuffle(words)
    for i in words:
        game=[words[0],words[1],words[2],words[4],words[3]]
    x = 0
    for i in game:
        b = list(i)
        random.shuffle(b)
        b = ''.join(b)
        print(b)
        c = input("Correct Spell of word is : ")
        if c.lower() == i:
            x = x+1
        elif c!=i:
            x = x-1
    print("your score is :",x)
    if x ==5:
        print("You are a winner")
    else:
        print("you are a looser")

words = ["father", "mother", "student", "teacher", "guide", "country", "india", "america"]
word_game(words)