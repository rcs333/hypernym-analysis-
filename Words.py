__author__ = 'Ryan Shean'


import nltk
from nltk.corpus import wordnet



#A class that stores information about text data in a list
class WordBin(object):
    #creates a new WordBin object and sets the list and creates the mapping
    def __init__(self, words):
        self.all_words = words
        self.list_synset = []
        self.unknown_words = []
        for word in self.all_words:
            try:
                self.list_synset.append(wordnet.synsets(word)[0])
            except IndexError:
                    self.unknown_words.append(word)


        self.synset_map = {}
        for word in self.list_synset:
            if word in self.synset_map:
                self.synset_map[word] += 1
            else:
                self.synset_map[word] = 1


        self.hyper_list = []
        self.words_with_no_hypers = []

        for w in self.list_synset:
            try:
                self.hyper_list.append(w.hypernyms()[0])
            except IndexError:
                self.words_with_no_hypers.append(w)

    #prints a decending list of words and number of occurences
    def show_sorted(self):
        for w in sorted(self.synset_map, key=self.synset_map, reverse=True):
            print(w, self.synset_map[w])


    #just run over the raw lists don't bother with counting them all up
    #keeping them in a big fat list then count later

    def create_hypers(self, list):
        hypers = []
        for w in list:
            try:
                hypers.append(w.hypernyms()[0])
            except IndexError:
                pass
        return hypers

#open function
templist = []
for word in open("allwords.txt").read().split():
    templist.append(word)
cbinl = WordBin(templist)


#make hypernym function
hyper_dictionary = {}
for thing in cbinl.hyper_list:
    if thing in hyper_dictionary:
        hyper_dictionary[thing] += 1
    else:
        hyper_dictionary[thing] = 1


for w in sorted(hyper_dictionary, key=hyper_dictionary.get, reverse=True):
    print(w, hyper_dictionary[w])

#let's get another list


hyper_list_2 = []
no_hyper_2 = []
for w in cbinl.hyper_list:
    try:
        hyper_list_2.append(w.hypernyms()[0])
    except IndexError:
        no_hyper_2.append(w)

hyper_dictionary_2 = {}
for thing in hyper_list_2:
    if thing in hyper_dictionary_2:
        hyper_dictionary_2[thing] += 1
    else:
        hyper_dictionary_2[thing] = 1
print("\n\n\n\n")

#for w in sorted(hyper_dictionary_2, key=hyper_dictionary_2.get, reverse=True):
   # print(w, hyper_dictionary_2)
print(len(cbinl.hyper_list))
print(len(hyper_list_2))
print(len(hyper_dictionary_2))
for w in sorted(hyper_dictionary_2, key=hyper_dictionary_2.get, reverse=True):
    print(hyper_dictionary_2[w], w.definition())
