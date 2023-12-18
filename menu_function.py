"""

pychatbot-MASSE-LOESCH_Int2, Evan MASSE, Thomas LOESCH.

This file allows the user to test the functions asked in the instructions in a menu.

"""



import time
from func_function import *
from test_function import *
from tf_idf_function import *
from partII_functions import *

def launcher():
    """
    Displays EFREI PYCHATBOT

    :return: No return since this function is used only to display the thing below.

    """
    print(r"""
    #################################################################
    #    ______  __          _                                      #
    #   |  ____|/ _|        (_)                                     #
    #   | |__  | |_ _ __ ___ _                                      #
    #   |  __| |  _| '__/ _ \ |                                     #
    #   | |____| | | | |  __/ |                                     #
    #   |______|_| |_|__\___|_|         _   ____        _           #
    #   |  __ \      / ____| |         | | |  _ \      | |          #
    #   | |__) |   _| |    | |__   __ _| |_| |_) | ___ | |_         #
    #   |  ___/ | | | |    | '_ \ / _` | __|  _ < / _ \| __|        #
    #   | |   | |_| | |____| | | | (_| | |_| |_) | (_) | |_         #
    #   |_|    \__, |\_____|_| |_|\__,_|\__|____/ \___/ \__|        #
    #           __/ |                                               #
    #          |___/                                                #
    #################################################################
    #            Welcome to Evan and Thomas's Pychatbot             #
    #################################################################""")
    return

def section():

    """
    Displays the different sections


    :return: No return since this function is used only to display the thing below.

    """
    print("""
    ##################################################################
    #                           Sections                             #      
    #   1 - Documentation of all the functions (Recommended to see   #
    #       this section first before testing the functions)         #    
    #                                                                #
    #   2 - Terminal where you can test the functions you asked      #    
    #       us to develop by calling them (they are the functions in #
    #       the documentation).                                      #
    #                                                                #
    #   3 - Mode chatbot                                             #
    #                                                                #
    #   4 - Exit                                                     #
    #                                                                #
    ##################################################################
          """)
    return

def displayStart():

    """
    Displays the different sections and EFREI PYCHATBOT

    :return: No return since this function is only used to display the two prints above

    """

    launcher()          #Print the 2 messages above
    section()
    return

def menu():

    """
    Function that asks the user in which section does he want to go to.

    :return: The choice of the user

    """
    setAnswer = ("1", "2", "3", "4", "documentation", "terminal", "chatbot", "exit")

    dir = str(input("Enter a number between 1 and 4 included in order to go in a section : "))      #Ask the user to enter a number between 1 and 4

    while dir not in setAnswer:
        dir = str(input("Enter a number between 1 and 4 included in order to go in a section : "))

    return dir

def searchFunctionality(search):

    """

    Functions that prints all the documentation

    :param search: Parameter used only if the user wants to go in the documentation. In this case, we print all the
    elements of the variable dic.
    :return: Nothing since this function is only used for displaying

    """
    dic = {
    "Basic functions" : {
        "extractNameFile" : "Function that extracts the name of the president in the name of a certain file",
        "assocNamePres" : "Function that associates to a president name, its first name",
        "listNamePres" : "Function that displays the list of the names of the presidents without duplications",
        "lowerClean" : "Function used to convert the texts in the 8 files to lower case and store the contents in new files",
        "cleanText" : "Function used to remove any punctuation characters of each file of the cleaned directory",
        },
    "The method TF-IDF" : {
        "score_TF" : "Function that associates to each word how many times it appeared in a string chain",
        "score_IDF" : "Function that computes the IDF score of each word in the entire corpus",
        "score_TF_IDF" : "Function that returns the score TF-IDF of a certain word in a certain document",
        "matrix_TD_IDF" : "Functions that calculates the matrix TF-IDF",
    },
    "Functionalities part 1" : {
        "min_word_TD_IDF" : "Function that gives the word(s) with TF-IDF = 0 in all the texts",
        "max_word_TD_IDF" : "Function that gives the word(s) with the highest score TF-IDF in all the texts",
        "word_most_repeated_Chirac": "Function that finds and prints the most repeated word(s) by Chirac",
        "talking_nation": "Function that determines which president(s) mentioned the word 'Nation' and identifies the president who repeated it the most times",
        "talking_climate": "Function that identifies the first president who talked about climate or ecology",
        "all_word_president": "Function that gives the words said by all the presidents, excluding unimportant words"
    },
    "Functionalities part 2" : {
        "question_tokenization" : "Tokenizes the input question, returning a list of words",
        "question_words_corpus" : "Finds terms that intersect between the set of words in the corpus and the set of words in the question",
        "question_TF_IDF" : "Returns the TF-IDF vector of the input question",
        "most_relevant_doc" : "Identifies the most similar document in relation to a given question.",
        "word_highest_TF_IDF_question" : "Returns the word with the highest TF-IDF score in the question",
        "sentence_word_highest_TF_IDF":"Retrieves a sentence containing the word with the highest TF-IDF score from the most relevant document"
        }
    }

    if search == "all":
                                #Print the documentation
        for key in dic:
            print()
            print(key, ":")
            print()

            for sub_key in dic[key]:
                print("Function : {}".format(sub_key))
                print("What it does : {}".format(dic[key][sub_key]))
        return

def documentation():
    """
    Function called in order to display the documentation

    :return: Nothing since it is only used for displaying.

    """
    searchFunctionality("all")
    time.sleep(1)           #Print the documentation, wait 1 sec and then go back to the menu where we can see the different sections

    section()
    return

def terminal():

    """
    Function that calls the functions desired by the user

    :return: Nothing since it only calls the different functions

    """

    state = False
    while True:
                if state is False:              #Message that appears only once
                    print()
                    print("(If you want to call the function \"talking_nation()\" for instance, type \"talking_nation\")")
                    print()

                    state = True

                dir = input("# Terminal (you can exit the terminal by typing \'exit\') : ")

                if dir == "min_word_TD_IDF":                #Call of a function depending on the user's demand
                    print()
                    print(min_word_TD_IDF())
                    print()
                elif dir == "max_word_TD_IDF":
                    print()
                    print(max_word_TD_IDF())
                    print()
                elif dir == "word_most_repeated_Chirac":
                    print()
                    print(word_most_repeated_Chirac())
                    print()
                elif dir == "talking_climate":
                    print()
                    print(talking_climate())
                    print()
                elif dir == "talking_nation":
                    print()
                    talking_nation()
                    print()
                elif dir == "all_word_president":
                    print()
                    print(all_word_president())
                    print()
                elif dir == "score_IDF":
                    print()
                    print(score_IDF("./cleaned"))
                    print()
                elif dir == "score_TF_IDF":
                    print()
                    doc = input("Select a document : ")
                    word = input("Select a word : ")
                    try:
                        print(score_TF_IDF(doc, word))
                    except:
                        print("The name of the document is wrong")
                    print()
                elif dir == "score_TF":
                    print()
                    doc = input("Select a document : ")
                    try:
                        full_path = path_speeches_file(doc)

                        with open(full_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            dictionary_scoreTF_word = score_TF(content.lower())

                        print(dictionary_scoreTF_word)
                    except:
                        print("The name of the document is wrong")
                    print()
                elif dir == "matrix_TD_IDF":
                    print()
                    visual_matrix_TD_IDF(matrix_TD_IDF('./cleaned'))
                    print()
                elif dir == "extractNameFile":
                    print()
                    file = input("Give me the name of a file : ")
                    try:
                        print(extractNameFile(file))
                    except:
                        print("The name of the file is wrong")
                    print()
                elif dir == "assocNamePres":
                    print()
                    president_name = input("Give me the name of a president from the corpus : ")
                    try:
                        print(assocNamePres(president_name))
                    except:
                        print("The name of the president is not correctly written or there is no such name in the corpus")
                    print()
                elif dir == "listNamePres":
                    print()
                    print(listNamePres('./speeches', '.txt'))
                    print()
                elif dir == "lowerClean":
                    print()
                    for name in list_of_files('./speeches', "txt"):
                        lowerClean(name)
                    print("All the files are now in lower case and are stored in the cleaned folder")
                    print()
                elif dir == "cleanText":
                    print()
                    for file in list_of_files('./cleaned', '.txt'):
                        clearFile(file)
                    print("All the files in the folder cleaned do not have any punctuations anymore")
                    print()
                elif dir == "question_tokenization":
                    print()
                    question = input("Enter a question : ")
                    print("This is your tokenization : ", question_tokenization(question))
                    print()
                elif dir == "question_words_corpus":
                    print()
                    question = input("Enter a question : ")
                    print("This is the terms that intersect : ",question_words_corpus(question))
                    print()
                elif dir == "question_TF_IDF":
                    print()
                    question = input("Enter a question : ")
                    print("This is the TF IDF of the question :")
                    print(question_TF_IDF(question))
                    print()
                elif dir == "most_relevant_doc":
                    print()
                    question = input("Enter a question : ")
                    print("This is the most similar document with the question :", most_relevant_doc(matrix_TD_IDF('./cleaned'),
                                              question_TF_IDF(question), list_of_files('./cleaned', 'txt')))
                    print()
                elif dir == "word_highest_TF_IDF_question":
                    print()
                    question = input("Enter a question : ")

                    if word_highest_TF_IDF_question(question) is None:
                        print("There are no words in the question that are in the corpus.")
                    else:
                        print("This is the word with the highest TF-IDF score in the question :", word_highest_TF_IDF_question(question))

                    print()
                elif dir == "sentence_word_highest_TF_IDF":
                    print()
                    question = input("Enter a question : ")
                    print(sentence_word_highest_TF_IDF(question))
                    print()
                elif dir == "exit":
                        print()
                        print("Exiting the Terminal. Goodbye!")
                        section()
                        break
                else:
                        print("!! Invalid choice !!")
    return

def chatbot():

    """
    Function that runs the Chatbot Mode.

    :return: Nothing since the function only displays

    """
    print("""
    ##################################################################
    #                           Chatbot                              #
    #       Enter the question you want to ask ?                     #
    #       To exit, enter : exit                                    #  
    ################################################################## 
""")
    while True:
        question = str(input("Question : "))            #Input from the user
        if question == "exit":
            section()
            break
        else:
            print("Chatbot :", sentence_word_highest_TF_IDF(question))      #Answer of the chatbot
    return