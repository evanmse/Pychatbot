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
    dic = {"list_of_files()":"# Function that gives the list of files in a directory, Example : /speeches",
    "extractNameFile()":"# Function that extracts the name of the president in the name of a certain file",
    "listNamePres()":"# Function that displays the list of the names of the presidents without duplications",
    "assocNamePres()":"# Function that associates to a president name, its first name",
    "lowerClean()":"# Function that transforms the content of a file into lowercase",
    "clearFile()":"# Main function in order to clean a certain file",
    "cleanText()":"# Sub-Function that cleans a text by removing the punctuations and the accents",
    "path_cleaned_file()":"# Function that gives to a cleaned file its path",
    "path_speeches_file()":"# Function that gives to a speeches file its path",
    "min_word_file_TD_IDF":"# Functionality that gives the word(s) that are not important in a file, TF-IDF = 0",
    "max_word_file_TD_IDF":"# Functionality that gives the most important words in a file",
    "min_word_TD_IDF":"# Functionality that gives the word(s) with the lowest TF-IDF in all text (TF-IDF = 0)",
    "max_word_TD_IDF":"# Functionality that gives the word(s) with the highest TF-IDF in all text",
    "word_most_repeated_Chirac":"# Functionality that gives the most repeated word(s) by Chirac",
    "talking_climate:":"# Functionality that gives the first president who talked about climate",
    "talking_nation":"# Functionality that gives which president(s) said the word \"Nation\" and the one who repeated it the most time",
    "all_word_president":"# Functionality that gives the words all presidents have said except the unimportant words",
    "test_extractNameFile()":"# Test for function extractNameFile ",
    "test_assocNamePres()":"# Test for assocNamePres, for Sarkozy",
    "test_listNamePres()":" # Test for listNamePres ",
    "test_score_TF()":"# Test for score_TF",
    "path_cleaned_file":"# Function that gives to a cleaned file its path",
    "path_speeches_file":"# Function that gives to a speeches file its path",
    }
    if search == "all":
        for keys, value in dic.items():
            print("Function : {}".format(keys))
            print("Function : {}".format(value)) 
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

                if dir == "min_word_file_TD_IDF":
                    file = input("Give a name of file :")
                    min_word_file_TD_IDF(file)
                elif dir == "min_word_file_TD_IDF":
                    file = input("Give a name of file")
                    min_word_file_TD_IDF(file)
                elif dir == "min_word_TD_IDF":
                    min_word_TD_IDF()
                elif dir == "max_word_TD_IDF":
                    max_word_TD_IDF()
                elif dir == "word_most_repeated_Chirac":
                    word_most_repeated_Chirac()
                elif dir == "talking_climate":
                    talking_climate()
                elif dir == "talking_nation":
                    talking_nation()
                elif dir == "all_word_president":
                    all_word_president()
                elif dir == "test_extractNameFile":
                    test_extractNameFile()
                elif dir == "test_assocNamePres":
                    test_assocNamePres()
                elif dir == "test_listNamePres":
                    test_listNamePres()
                elif dir == "test_score_TF":
                    test_score_TF()
                elif dir == "test_lowerClean":
                    test_lowerClean()
                elif dir == "test_clearFile":
                    test_clearFile()
                elif dir == "min_word_file_TD_IDF":
                    file = input("Give a name of file")
                    min_word_file_TD_IDF(file)
                elif dir == "max_word_file_TD_IDF":
                    file = input("Give a name of file")
                    max_word_file_TD_IDF(file)
                elif dir == "min_word_TD_IDF":
                    min_word_TD_IDF()
                elif dir == "max_word_TD_IDF":
                    max_word_TD_IDF()
                elif dir == "word_most_repeated_Chirac":
                    word_most_repeated_Chirac()
                elif dir == "talking_climate":
                    talking_climate()
                elif dir == "talking_nation":
                    talking_nation()
                elif dir == "all_word_president":
                    all_word_president()
                elif dir == ":exit":
                        print("Exiting the Terminal. Goodbye!")
                        section()
                        break
                else:
                        print("!! Invalid choice !!")
    return




     

