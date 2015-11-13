__author__ = 'Ryan Shean'

#TODO: Try to fix the arbitary assignment of synsets and hypernyms
#TODO: Make better graphs
#TODO: Make the analysis a function that writes a new file
#TODO: update the variable names to not have typing or be named the same as default types


#Honestly this code is black magic right now
#Anaconda broke my file reading and this fixes the problem so don't ask
import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.corpus import wordnet

#function that tokenizes a file given a path and returns a list of all tokens
#as lemmatized strings
def read_lemmas(path):
    tokens = []
    for word in open(path).read().split():
        tokens.append(word)

    lemmas = [nltk.WordNetLemmatizer().lemmatize(t) for t in tokens]
    return lemmas

#Takes a list of text strings and returns a list of snyset object coresponding to
#the strings, duplicates are allowed and strings that do not have synsets are
#put in another list and returned as a tuple(?) that needs to be indexed to grab
def make_synset(all_lemmas):
    syn_list = []
    unknown_words = []
    for word in all_lemmas:
        try:
            syn_list.append(wordnet.synsets(word)[0])
        except IndexError:
            unknown_words.append(word)
    return syn_list,unknown_words

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

#takes a list of words and returns a map containing parts of speech and their counts
#Had to be hardcoded because POS tagging output tuples(?) and I didn't want to have to deal
#with generalizing the other function
def tag_pos(list):
    pos_tagged = nltk.pos_tag(list)
    pos_map = {}
    for item in pos_tagged:
        pos = item[1]
        if pos in pos_map:
            pos_map[pos] += 1
        else:
            pos_map[pos] = 1
    return pos_map

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

#Takes a map of Synset Objects and values representing their counts as well as integer tolerance
#and prints the name of the sysnset objects that appear more than the tolerance in decending order
def sort_print(map, tolerance):
    for w in sorted(map, key=map.get, reverse=True):
        if map[w] > tolerance:
            print(w, map[w])
    print("\n\n")

#Takes a map of wordnet Sysnset objects and counts and an interger tolerance and displays a bar
#graph of the names of the synset objects with their frequencies on the y-axis. Only prints words
#that appear in the map more times than the passed tolerance
def graph_frequencies(map, tolerance):
        x_label = []
        y_data = []
        number_of_entries = 0
        for w in sorted(map, key=map.get, reverse=True):
            if map[w] > tolerance:
                number_of_entries += 1
                x_label.append(w.name().partition('.')[0])
                y_data.append(map[w])
        x_pos = np.arange(number_of_entries)
        plt.bar(x_pos,y_data)
        plt.xticks(x_pos, x_label)
        plt.show()




#I think this allows this code to be imported as a module
if __name__ == '__main__':
    #Open file and tokenize into strings
    path = 'ffbs.txt'
    lemmas = read_lemmas(path)

    #match all the words to a (somewhat arbitrary) wordnet definition
    #and then count them grab the known words and unknowns with
    #AUTOMATIC UNPACKING HOLY SHIT THATS COOL
    synset,unknowns = make_synset(lemmas)
    synset_counts = create_counts(synset)

    #Create a list of hypernyms off the "found" words in the file
    hypers_1 = make_hyper_list(synset)
    hypers_counts_1 = create_counts(hypers_1)

    #Create two lists of hypernyms one "level" up each
    hypers_2 = make_hyper_list(hypers_1)
    hypers_counts_2 = create_counts(hypers_2)

    hypers_3 = make_hyper_list(hypers_2)
    hypers_counts_3 = create_counts(hypers_3)

    hypers_4 = make_hyper_list(hypers_3)
    hypers_counts_4 = create_counts(hypers_4)





    graph_frequencies(hypers_counts_2, 10)



    print(path)
    print("\n")
    print("Parts of Speech:\n")
    sort_print(tag_pos(lemmas), 10)
    print("\n\n\n")
    print("Words Detected:\n")
    sort_print(synset_counts, 10)
    print("First Level of Hypernyms:\n")
    sort_print(hypers_counts_1, 10)
    print("Second Level of Hypernyms:\n")
    sort_print(hypers_counts_2, 10)
    print("Third Level of Hypernyms:\n")
    sort_print(hypers_counts_3, 10)
    print("Fourth Level of Hypernyms:\n")
    sort_print(hypers_counts_4, 10)

