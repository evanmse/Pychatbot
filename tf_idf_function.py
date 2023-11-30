import math
from base_function import *



def score_TF(strings_chain):  # Function that associates to each word how many times it appeared in a string chain
    content = strings_chain.lower()
    content = cleanText(content)
    dictionary = {}
    mylist = content.split(" ")

    for i in range(mylist.count("")):  # Remove all the "" in the list
        mylist.remove("")

    list_unique_word = list(set(mylist))

    for word in list_unique_word:
        dictionary[word] = mylist.count(word)

    return dictionary


def score_IDF(directory):   #Function that computes the IDF score of each word in the entire corpus
    files_name = list_of_files(directory, 'txt')
    mylist = []
    mydict = {}
    dictionnary_IDF = {}

    for file in files_name:  # Go through each file in the directory
        full_path = path_speeches_file(file)  # Put in a variable the path of the file

        with open(full_path, 'r', encoding='utf-8') as f:
            content = cleanText(f.read())
            dictionnary_file = score_TF(content)
            mylist = list(set(mylist + list(dictionnary_file.keys())))  # List containing all the words of all the files

    for element in mylist:  # Creation of the dictionnary containing all the elements of mylist as keys
        mydict[element] = 0

    for document in files_name:
        full_path2 = path_speeches_file(document)

        with open(full_path2, 'r', encoding='utf-8') as f2:
            content2 = cleanText(f2.read().lower())
            content_dictionnary = score_TF(content2)

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
    word = cleanText(word.lower())
    dictionnary_scoreIDF_word = score_IDF('./speeches') #Dictionary that contains the score_IDF of each word

    with open(full_path, 'r', encoding='utf-8') as f:
        content = cleanText(f.read().lower())
        dictionnary_scoreTF_word = score_TF(content)

    return dictionnary_scoreTF_word[word] * dictionnary_scoreIDF_word[word]


def matrix_TD_IDF(directory):       #Calculate the matrix TF-IDF
    list_final = []
    rest = score_IDF('./cleaned')

    for keys, value in rest.items():     #Creation of the sub-lists in the matrix
        temp = []
        for file in list_of_files(directory, "txt"):

            with open(path_cleaned_file(file), 'r', encoding="utf-8") as f:
                content = cleanText(f.read())
                dictionnary_scoreTF_word = score_TF(content)

                if keys in set(dictionnary_scoreTF_word.keys()):
                    temp.append(dictionnary_scoreTF_word[keys] * rest[keys])
                else:
                    temp.append(0)
        temp.append(keys)

        list_final.append(temp)

    for file in list_of_files("./cleaned", "txt"):
        print(file, "|", end=" ")

    for word in range(len(list_final)):                         #Creation of the visual of the matrix
        for space in range(23 - len(list_final[word][-1])):
            print(end=" ")
        print(list_final[word][-1], '|', end=" ")
        for item in range(len(list_final[word][:-1])):
            for space in range(21 - len(str(list_final[word][item]))):
                print(end=" ")
            print(list_final[word][item], "|", end=" ")
        print()

    return