import math
from base_function import *

directory = "./speeches"


def score_TF(strings_chain):  # Function that associates to each word how many times it appeared in a string chain

    dictionnary = {}
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"  # A string that contains all the punctuations
    mylist_words = []

    for caracter in strings_chain:
        if caracter not in punctuations:
            mylist_words.append(caracter)  # Append to mylist_words all the caracters that are not punctuations
        else:
            mylist_words.append(' ')  # Replace all the punctuations by space

    str_chain_no_punctuations = ''.join(mylist_words)
    list_chain_no_punctuations = str_chain_no_punctuations.split(" ")

    for i in range(list_chain_no_punctuations.count("")):  # Remove all the "" in the list
        list_chain_no_punctuations.remove("")

    for k in range(list_chain_no_punctuations.count("\n")):  # Remove all the "\n" in the list
        list_chain_no_punctuations.remove("\n")

    for j in range(len(list_chain_no_punctuations)):  # Remove "\n" in each word of the list

        if "\n" in list_chain_no_punctuations[j][:2] or "\n" in list_chain_no_punctuations[j][-2:]:
            list_chain_no_punctuations[j] = list_chain_no_punctuations[j].replace("\n", "")

        elif "\n" in list_chain_no_punctuations[j][2:-2]:
            word_space = list_chain_no_punctuations[j].split("\n")
            list_chain_no_punctuations.remove(list_chain_no_punctuations[j])
            for x in range(len(word_space)):
                list_chain_no_punctuations.append(word_space[x])

    list_unique_word = list(set(list_chain_no_punctuations))

    for word in list_unique_word:
        dictionnary[word] = list_chain_no_punctuations.count(word)  # Create the dictionnary

    return dictionnary


def score_IDF(directory):
    files_name = os.listdir(directory)
    mylist = []
    mydict = {}
    dictionnary_IDF = {}

    for file in files_name:  # Go through each file in the directory
        full_path = os.path.join('./speeches', file)  # Put in a variable the path of the file

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            dictionnary_file = score_TF(content)
            mylist = list(set(mylist + list(dictionnary_file.keys())))  # List containing all the words of all the files

    for element in mylist:  # Creation of the dictionnary containing all the elements of mylist as keys
        mydict[element] = 0

    for document in files_name:
        full_path2 = os.path.join('./speeches', document)

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
