##CodeNames
#Autumn Kinchen and Kate Bond

import gensim
import operator
import random

#modeling
filename = '/Users/autumnkinchen/data/GoogleNews-vectors-negative300.bin.gz'
model = gensim.models.KeyedVectors.load_word2vec_format(filename, binary=True)
lines = open('wordlist.txt').read().splitlines()

#generating words for the board
red = random.sample(lines, 8)
blue = random.sample([i for i in lines if i not in red], 9)
filler = random.sample([i for i in lines if i not in red and i not in blue], 7)
assassin = random.sample([i for i in lines if i not in red and i not in blue and i not in filler], 1)

inpu = input("Welcome to Codenames. Type '1' to play the codemaster or type '2' to play the agent. ")


def verify(inp, clue):
    if '_' in clue:
        return False
    if inp in clue or clue in inp:
        return False
    return True

if inpu == '1':
    redboard = red.copy()
    blueboard = blue.copy()
    assassinb = assassin.copy()
    fillerboard = filler.copy()

    # readying the display board for codemaster
    for i, word in enumerate(redboard):
        word2 = word.replace(word, "RED: " + word)
        redboard[i] = word2
    for i, word in enumerate(blueboard):
        word2 = word.replace(word, "BLUE: " + word)
        blueboard[i] = word2
    for i, word in enumerate(fillerboard):
        word2 = word.replace(word, "BYSTANDER: " + word)
        fillerboard[i] = word2
    for i, word in enumerate(assassinb):
        word2 = word.replace(word, "ASSASSIN: " + word)
        assassinb[i] = word2
    board = redboard + blueboard + assassinb + fillerboard
    wordlist = red + blue + assassin + filler
    random.shuffle(board)

    while True:
        if len(blue) == 0:
            print("Congrats! You've won!")
            break
        if len(red) == 0:
            print("GAME OVER: YOU LOST.")
            break
        #display for codemaster
        grouped = [board[i:i + 5] for i in range(0, len(board), 5)]
        for l in grouped:
            print("".join("{:<26}".format(x) for x in l))

        #gameplay
        inp = input("Enter a clue: ")
        guess = model.most_similar_to_given(inp, wordlist)

        print("My guess is:", guess)

        if guess in blue:
            print("I got it right!")
            blue.remove(guess)
            wordlist.remove(guess)
            # removing word from the board
            for w in board:
                if guess in w:
                    board.remove(w)
                else:
                    continue

        elif guess in red:

            print("Oh no! I gave two points to the other team by guessing their word.")
            red.remove(guess)
            wordlist.remove(guess)

            rand = random.choice(red)
            red.remove(rand)

            # wordlist.remove(guess)
            # wordlist.remove(rand)

            # removing word from the board
            for w in board:
                if guess in w:
                    board.remove(w)
                else:
                    continue

        elif guess in assassin:
            print("GAME OVER: YOU LOST")
            break

        else:
            print("I chose a bystander word. A point for the other team :(")
            filler.remove(guess)
            wordlist.remove(guess)

            rand = random.choice(red)
            red.remove(rand)
            # removing word from the board
            for w in board:
                if guess in w:
                    board.remove(w)
                elif rand in w:
                    board.remove(w)
                else:
                    continue



if inpu == '2':
    words = red + blue + assassin + filler
    random.shuffle(words)

    #gameplay
    while True:
        if len(blue) == 0:
            print("Congrats! You've won!")
            break
        if len(red) == 0:
            print("GAME OVER: YOU LOST.")
            break

        # board display
        grouped = [words[i:i + 5] for i in range(0, len(words), 5)]
        for l in grouped:
            print("".join("{:<26}".format(x) for x in l))

        #generate a random clue
        word = random.choice(blue)
        similar = [(c.lower(), s) for c,s in model.most_similar(positive=[word], topn=50, restrict_vocab = 60000)]
        clue = [(c, s) for c, s in similar if verify(word, c)][:1]

        #giving clue, asking for guess
        inp = input("My clue is: " + clue[0][0] + "...have a guess? ")

        #evaluating the guesses, updating the lists of words and the board
        if inp in blue:
            print("Correct! A point for your team!")
            blue.remove(inp)
            words.remove(inp)
        elif inp in red:
            print("Correct!....for the wrong team. Two points to the opposing team.")
            red.remove(inp)
            words.remove(inp)

            #intermediary check to prevent out of range error
            if len(red) == 0:
                print("GAME OVER: YOU LOST.")
                break

            rand = random.choice(red)
            red.remove(rand)
            words.remove(rand)

        elif inp in filler:
            print("You chose a bystander. A point for the opposing team.")
            filler.remove(inp)
            words.remove(inp)

            rand = random.choice(red)
            red.remove(rand)
            words.remove(rand)
        else:
            print("GAME OVER: YOU LOST")
            break





