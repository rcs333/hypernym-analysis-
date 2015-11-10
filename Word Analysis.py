__author__ = 'Ryan Shean'

#TODO: Examine the efficeincy and complexity of what i'm doing here, im pretty sure its O(N) but idk
#TODO: Try to fix the arbitary assignment of synsets and hypernyms
#TODO: Maybe work on nicer output, graphs w/ matlabplot lib ?

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
    print("\n\n\n")

#Takes a list of any object and counts them and creates a map
#probobly inefficient but I'm not working with an extremly large data set
def create_counts(list):
    counts = {}
    for item in list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

#Open file and tokenize into strings
lemmas = read_lemmas("allwords.txt")

#match all the words to a (somewhat arbitrary) wordnet definition
#and then count them
synset = make_synset(lemmas)
synset_counts = create_counts(synset)

#Create a list of hypernyms off the "found" words in the file
hypers_1 = make_hyper_list(synset)
hypers_counts_1 = create_counts(hypers_1)

#Create two lists of hypernyms one "level" up each
hypers_2 = make_hyper_list(hypers_1)
hypers_counts_2 = create_counts(hypers_2)

hypers_3 = make_hyper_list(hypers_2)
hypers_counts_3 = create_counts(hypers_3)

#Tag all of the words and then count each occurance of each part of speech
pos_tagged = nltk.pos_tag(lemmas)
pos_map = {}
for item in pos_tagged:
    pos = item[1]
    if pos in pos_map:
        pos_map[pos] += 1
    else:
        pos_map[pos] = 1

#Print all dat shit
sort_print(pos_map)
print("\n\n\n")
sort_print(synset_counts)
sort_print(hypers_counts_1)
sort_print(hypers_counts_2)
sort_print(hypers_counts_3)
