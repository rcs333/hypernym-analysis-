__author__ = 'Ryan Shean'

#TODO: POS Tagging
import nltk
from nltk.corpus import wordnet

#function that tokenizes a file given a path and returns a list of all tokens
#as strings
def read_lemmas(path):
    lemmas = []
    for word in open(path).read().split():
        lemmas.append(word)
    return lemmas

#Takes a list of synsnet objects and creates and returns a list of all hypernyms
#inside of the list, duplicates are allowed and the list is completely unsorted
def make_hyper_list(list):
    hyper_list = []
    for token in list:
        try:
            hyper_list.append(token.hypernyms()[0])
        except IndexError:
            pass
    return hyper_list

#Takes a list of text strings and returns a list of snyset object coresponding to
#the strings, duplicates are allowed and strings that do not have synsets are dropped
def make_synset(list):
    syn_list = []
    for word in list:
        try:
            syn_list.append(wordnet.synsets(word)[0])
        except IndexError:
            pass
    return syn_list

#Takes a map of keys and values and prints them in decending orderd
def sort_print(map):
    for w in sorted(map, key=map.get, reverse=True):
        print(w, map[w])


lemmas = read_lemmas("allwords.txt")
synset = make_synset(lemmas)
hypernet = make_hyper_list(synset)
hypernet_2 = make_hyper_list(hypernet)
print(hypernet_2)