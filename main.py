##CodeNames
#Autumn Kinchen and Kate Bond

import gensim
import operator
import random


# filename = '/Users/autumnkinchen/data/GoogleNews-vectors-negative300.bin.gz'
# model = gensim.models.KeyedVectors.load_word2vec_format(filename, binary=True)
lines = open('wordlist.txt').read().splitlines()
# red = []
# blue = []
# chosen = []

red = random.sample(lines, 8)
blue = random.sample(lines, 9)
assassin = random.sample(lines, 1)


# red = ['watch', 'star', 'mole', 'Berlin', 'limousine', 'day', 'wind', 'cap', 'thumb']
# blue = ['smuggler', 'crown', 'cotton', 'palm', 'pumpkin', 'giant', 'link', 'puppy']
# assassin = 'tie'
# def verify(candidate, word_list):
#     if '_' in candidate:
#         return False
#     for word in word_list:
#         if word in candidate or candidate in word:
#             return False
#     return True
#
# def verify2(inp, clue):
#     if inp in clue or clue in inp:
#         return False
#     return True
#
#
# inp = input("Enter a clue: ")
# similar = [(c.lower(), s) for c,s in model.most_similar(positive=[inp], topn=50)]
# clue = [(c, s) for c, s in similar if verify2(inp, c)][:1]
#
# print("My guess is:", clue[0][0])
#
# if clue[0][0] in blue:
#     print("Good work")
# else:
#     print("Bad work")
#


