from tf_idf_function import score_TF, score_IDF
from base_function import path_speeches_file
import os


def max_score_TF_IDF():  # Function that calculates the highest TF-IDF score
    dictionnary_scoreIDF_word = score_IDF('./speeches')
    maxi = 0
    files_name = os.listdir('./speeches')

    for file in files_name:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            dictionnary_scoreTF_word = score_TF(content)

        for i in dictionnary_scoreTF_word:  # Calculate the maximum TF-IDF score
            if (dictionnary_scoreTF_word[i] * dictionnary_scoreIDF_word[i]) > maxi:
                maxi = dictionnary_scoreTF_word[i] * dictionnary_scoreIDF_word[i]

    return maxi


def min_word_file_TD_IDF(file):  # Functionality that gives the word(s) that are not important in file, TD-IDF = 0
    print("In development")
    return


def max_word_file_TD_IDF(file):  # Functionality that gives the most important words in file
    print("In development")
    return


def min_word_TD_IDF():  # Functionality that gives the word(s) with min TD-IDF in all text
    mylist = []
    dictionnary_scoreIDF_word = score_IDF('./speeches')

    files_name = os.listdir('./speeches')

    for file in files_name:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            list_of_word = list(score_TF(content).keys())
            dictionnary_scoreTF_word = score_TF(content)

        for i in list_of_word:
            if (dictionnary_scoreTF_word[i] * dictionnary_scoreIDF_word[i]) == 0:  # If score TF-IDF is 0
                mylist.append(i)

    return list(set(mylist))


def max_word_TD_IDF():  # Functionality that gives the word(s) with max TD-IDF in all text

    dictionnary_scoreIDF_word = score_IDF('./speeches')
    maxi = max_score_TF_IDF()
    files_name = os.listdir('./speeches')
    mylist = []

    for file in files_name:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            dictionnary_scoreTF_word = score_TF(content)

        for i in dictionnary_scoreTF_word:  # Calculate the maximum TF-IDF score
            if (dictionnary_scoreTF_word[i] * dictionnary_scoreIDF_word[i]) == maxi:
                mylist.append(i)

    return list(set(mylist))


def word_most_repeated_Chirac():  # Functionality that gives the most repeated word by Chirac

    content = ''
    files_name = os.listdir('./speeches')
    mylist_Chirac = [text for text in files_name if 'Chirac' in text]
    mylist = []

    for file in mylist_Chirac:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = content + f.read()

    dictionnary_scoreTF_word = score_TF(content)

    maxi = max(list(dictionnary_scoreTF_word.values()))

    for key in list(dictionnary_scoreTF_word.keys()):
        if dictionnary_scoreTF_word[key] == maxi:
            mylist.append(key)

    return mylist


def talking_climate():  # Functionality that gives the first president who talked about climate
    print("In development")
    return


def talking_nation():  # Functionality that gives which president(s) said the word "Nation" and the one who repeated it the most time
    print("In development")
    return


def all_word_president():  # Functionality that gives the words all presidents have said except the unimportant words
    print("In development")
    return