import math

import test_function
from base_function import *
from test_function import *

directory = "./speeches"


def score_TF(strings_chain):  # Function that associates to each word how many times it appeared in a string chain
    content = strings_chain.lower()
    content = cleanText(content)
    dictionary = {}
    mylist = content.split(" ")
    print(mylist)

    for i in range(mylist.count("")):  # Remove all the "" in the list
        mylist.remove("")

    list_unique_word = list(set(mylist))

    for word in list_unique_word:
        dictionary[word] = mylist.count(word)

    return dictionary


def score_IDF(directory):
    files_name = os.listdir(directory)
    mylist = []
    mydict = {}
    dictionnary_IDF = {}

    for file in files_name:  # Go through each file in the directory
        full_path = path_speeches_file(file)  # Put in a variable the path of the file

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            dictionnary_file = score_TF(content)
            mylist = list(set(mylist + list(dictionnary_file.keys())))  # List containing all the words of all the files

    for element in mylist:  # Creation of the dictionnary containing all the elements of mylist as keys
        mydict[element] = 0

    for document in files_name:
        full_path2 = path_speeches_file(document)

        with open(full_path2, 'r', encoding='utf-8') as f2:
            content = f2.read().lower()
            content_dictionnary = score_TF(content)

            for word in mylist:  # Add 1 to mydict[word] if the word is in the .txt file
                if word in list(content_dictionnary.keys()):
                    mydict[word] += 1

    for key in list(
            mydict.keys()):  # Calculate the log of the inversed of the proportion of documents containing a certain word
        number_document = len(list_of_files('./speeches', '.txt'))
        proportion_document_containing_word = mydict[key] / number_document
        inversed_proportion_document_containing_word = 1 / proportion_document_containing_word
        dictionnary_IDF[key] = math.log(inversed_proportion_document_containing_word)

    return dictionnary_IDF


def score_TF_IDF(document, word):  # Return the score TF-IDF of a certain word in a certain document
    full_path = os.path.join('./speeches', document)
    word = word.lower()

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read().lower()
        dictionnary_scoreTF_word = score_TF(content)
        dictionnary_scoreIDF_word = score_IDF('./speeches')

        return dictionnary_scoreTF_word[word] * dictionnary_scoreIDF_word[word]
