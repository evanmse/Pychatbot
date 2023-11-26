import time
from func_function import *
from test_function import *
from tf_idf_function import *

def launcher():
    print("""
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
    #################################################################
    #                         Section                               #
    #   1 - documentation                                           #
    #   2 - terminal                                                #
    #   3 - exit                                                    #
    #################################################################""")
    return

def displayStart():
    launcher()
    section()
    return

def menu():
    setAnswer = ("1", "2", "3","documentation", "terminal", "exit")
    
    dir = str(input("Enter a number in order to go in a section or a shortcut : "))
    if not dir in setAnswer:
        dir = input("!! Please retry to enter a correct number or shortcut : ")         
    return dir

def searchFunctionality(search):
    dic = {
    "max_score_TF_IDF": "Computes and prints the word with the highest TF-IDF score in the entire corpus.",
    "min_word_TF_IDF": "Identifies and prints the word(s) with the lowest TF-IDF score in all text (TF-IDF = 0).",
    "max_word_TD_IDF": "Determines and prints the word(s) with the highest TF-IDF score in all text.",
    "word_most_repeated_Chirac": "Finds and prints the most repeated word(s) by Chirac.",
    "talking_climate": "Identifies the first president who talked about climate.",
    "talking_nation": "Determines which president(s) mentioned the word 'Nation' and identifies the president who repeated it the most times.",
    "all_word_president": "Prints the words spoken by all presidents, excluding unimportant words.",
    "test_extractNameFile": "Executes a test for the `extractNameFile` functionality.",
    "test_assocNamePres_Sarkozy": "Executes a test for the `assocNamePres` functionality, specifically for Sarkozy.",
    "test_listNamePres": "Executes a test for the `listNamePres` functionality.",
    "test_score_TF": "Executes a test for the `score_TF` functionality.",
    "test_lowerClean": "Executes a test for the `lowerClean` functionality.",
    "test_clearFile": "Executes a test for the `clearFile` functionality.",
    "score_IDF": "Computes and prints the IDF score for a given directory of cleaned files.",
    "score_TF_IDF": "Computes and prints the TF-IDF score for a given document and word selected by the user.",
    "matrix_TD_IDF": "Generates and prints the TF-IDF matrix.",
    "searchFunctionality": "A dictionary (`dic`) maps search terms to their respective functionality descriptions.",
    "exit": "To exit the terminal, use the command `exit`."}

    if search == "all":
        for keys, value in dic.items():
            print("Function : {}".format(keys))
            print("Definition : {}".format(value)) 
        return
    else:
        for keys, value in dic.items():
            if (keys.find(search) != -1) or (value.find(search) != -1) :
                print("Function : {}".format(keys))
                print("Function : {}".format(value))
        return

def documentation():
    searchFunctionality("all")
    time.sleep(5)
    section()
    return

def terminal():
    while True:
                dir = input("# Terminal # : ")

                if dir == "max_score_TF_IDF":
                    print(max_score_TF_IDF())
                elif dir == "min_word_TF_IDF":
                    print(min_word_TD_IDF())
                elif dir == "max_word_TD_IDF":
                    print(max_word_TD_IDF())
                elif dir == "word_most_repeated_Chirac":
                    print(word_most_repeated_Chirac())
                elif dir == "talking_climate":
                    print(talking_climate())
                elif dir == "talking_nation":
                    talking_nation()
                elif dir == "all_word_president":
                    print(all_word_president())
                elif dir == "test_extractNameFile":
                    test_extractNameFile()
                elif dir == "test_assocNamePres_Sarkozy":
                    test_assocNamePres_Sarkozy()
                elif dir == "test_listNamePres":
                    test_listNamePres()
                elif dir == "test_score_TF":
                    test_score_TF()
                elif dir == "test_lowerClean":
                    test_lowerClean()
                elif dir == "test_clearFile":
                    test_clearFile()
                elif dir == "score_IDF":
                    print(score_IDF("./cleaned"))
                elif dir == "score_TF_IDF":
                    doc = input("Select a document :")
                    word = input("Select a word :")
                    print(score_TF_IDF(doc, word))
                elif dir == "matrix_TD_IDF":
                    file = input("Select a directory :")
                    matrix_TD_IDF(file)
                elif dir == "exit":
                        print("Exiting the Terminal. Goodbye!")
                        section()
                        break
                else:
                        print("!! Invalid choice !!")
    return




     

