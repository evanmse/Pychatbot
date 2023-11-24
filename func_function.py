from tf_idf_function import score_TF, score_IDF
from base_function import path_speeches_file
import os

def max_score_TF_IDF(): #Function that calculates the highest TF-IDF score
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


def min_word_file_TD_IDF():  # Functionality that give the non-important word, TD-IDF = 0
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


def max_word_file_TD_IDF():  # Functionality that give the word(s) with the highest score TD_IDF
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


def min_word_TD_IDF(value):  # Functionality that give the word with min TD-IDF in all text
    print("In development")
    return


def max_word_TD_IDF(value):  # Functionality that give the word with max TD-IDF in all text
    print("In development")
    return


def repeat_word_pres(president):  # Functionality that give the most word repeat by a president
    print("In development")
    return


def talking_climate():  # Functionality that give who talks about climate
    print("In development")
    return


def talking_nation():  # Functionality that give who talks about climate
    print("In development")
    return


def all_word_president():  # Functionality words all presidents have spoken without the unimportant words
    print("In development")
    return


