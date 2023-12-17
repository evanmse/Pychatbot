import time
from func_function import *
from test_function import *
from tf_idf_function import *
from partII_functions import *

def launcher():
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
    launcher()
    section()
    return

def menu():
    setAnswer = ("1", "2", "3", "4", "documentation", "terminal", "chatbot", "exit")
    
    dir = str(input("Enter a number between 1 and 4 included in order to go in a section : "))

    while dir not in setAnswer:
        dir = str(input("Enter a number between 1 and 4 included in order to go in a section : "))

    return dir

def searchFunctionality(search):
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

        for key in dic:
            print()
            print(key, ":")
            print()

            for sub_key in dic[key]:
                print("Function : {}".format(sub_key))
                print("What it does : {}".format(dic[key][sub_key]))
        return

def documentation():
    searchFunctionality("all")
    time.sleep(1)
    section()
    return

def terminal():

    state = False
    while True:
                if state is False:
                    print()
                    print("(If you want to call the function \"talking_nation()\" for instance, type \"talking_nation\")")
                    print()

                    state = True

                dir = input("# Terminal (you can exit the terminal by typing \'exit\') : ")

                if dir == "min_word_TD_IDF":
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
                elif dir == "question_words_corpus":
                    print()
                    question = input("Enter a question : ")
                    print("This is the terms that intersect : ",question_words_corpus(question))
                elif dir == "question_TF_IDF":
                    print()
                    question = input("Enter a question : ")
                    print("This is the TF IDF of the question :", question_TF_IDF(question))
                elif dir == "most_relevant_doc":
                    print()
                    question = input("Enter a question : ")
                    print("This is the most similar document with the question :", most_relevant_doc(matrix_TD_IDF('./cleaned'),
                                              question_TF_IDF(question), list_of_files('./cleaned', 'txt')))
                elif dir == "word_highest_TF_IDF_question":
                    print()
                    question = input("Enter a question : ")
                    print("This is the word with the highest TF-IDF score in the question :", word_highest_TF_IDF_question(question))
                elif dir == "sentence_word_highest_TF_IDF":
                    print()
                    question = input("Enter a question : ")
                    print("This is sentence containing the word with the highest TF-IDF score :", sentence_word_highest_TF_IDF(question)) 
                elif dir == "exit":
                        print("Exiting the Terminal. Goodbye!")
                        section()
                        break
                else:
                        print("!! Invalid choice !!")
    return

def chatbot():
    print("""
    ##################################################################
    #                           Chatbot                              #
    #       Enter the question you want to ask ?                     #
    #       To exit, enter : exit                                    #  
    ################################################################## 
""")
    while True:
        question = str(input("Chatbot : "))
        if question == "exit":
            section()
            break
        else:
            print(sentence_word_highest_TF_IDF(question))
    return