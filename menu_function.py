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
    #   1 - Documentation                                           #
    #   2 - Functionality                                           #
    #   3 - Test                                                    #
    #################################################################""")
    return

def displayStart():
    launcher()
    section()
    return

def menu():
    setAnswer = ("1", "2", "3", "4", "5", ":doc", ":doc search", ":doc how", ":doc func",
                ":func", ":func search",":func how", ":func func",
                ":test", ":test search",":test how", ":test func", ":section",":terminal", ":exit")
    
    dir = str(input("Enter a number in order to go in a section or a shortcut : "))
    while not dir in setAnswer:
        dir = input("!! Please retry to enter a correct number or shortcut : ")         
    return dir

def searchFunc(search):
    dic = {"list_of_files()":"# Function that gives the list of files in a directory, Example : /speeches",
    "extractNameFile()":"# Function that extracts the name of the president in the name of a certain file",
    "listNamePres()":"# Function that displays the list of the names of the presidents without duplications",
    "assocNamePres()":"# Function that associates to a president name, its first name",
    "lowerClean()":"# Function that transforms the content of a file into lowercase",
    "clearFile()":"# Main function in order to clean a certain file",
    "cleanText()":"# Sub-Function that cleans a text by removing the punctuations and the accents",
    "path_cleaned_file()":"# Function that gives to a cleaned file its path",
    "path_speeches_file()":"# Function that gives to a speeches file its path"
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



def sectionDocSearch():
        print("""
    #################################################################
    #                  Documentation Search                         #
    #################################################################
            """)     
        search = input("# Please enter 3 letter to search in documentation :")
        if len(search) < 3:
            search = input("# !! Please enter 3 letter to search in documentation :")
        searchFunc(search)
        time.sleep(5)
        section()
        return

def allFunction():
     searchFunc("all")
     return

def sectionDoc():
        print("""
    #################################################################
    #                    Documentation                              #
    #   Please enter a number ?                                     #
    #   1 - Search                                                  #
    #   2 - How to use ?                                            #
    #   3 - List of all the functions and what they do              #
    #   4 - Exit                                                    #
    #################################################################
    """)
        sub = menu()

        if sub == "1":
            sectionDocSearch()
        elif sub == "2":
            sectionDocHow()
        elif sub == "3":
            sectionDocFunc()
        elif sub == "4":
            print("!! Returning to the main menu !!")
            time.sleep(2)
            section()
        else:
            print("!! Invalid choice !!")
            time.sleep(2)
            section()
        return 
    
def sectionDocHow():
        print("""
    #################################################################
    #                  How to use the documentation                 #
    #################################################################
    #                                                               #
    # - You can search with search or command " :doc search"        #
    # - Or you can see the documentation of all function            #
    #                                                               #
    #################################################################
                """)
        time.sleep(5)
        section()
        return

def sectionDocFunc():
        print("""
    #################################################################
    #                        All function                           #
    #################################################################""")
        searchFunc("all")
        time.sleep(5)
        section()
        return
     
##################################### Part Functionality #####################################################

def searchFunctionality(search):
    dic = {"min_word_file_TD_IDF":"# Functionality that gives the word(s) that are not important in a file, TD-IDF = 0",
    "max_word_file_TD_IDF":"# Functionality that gives the most important words in a file",
    "min_word_TD_IDF":"# Functionality that gives the word(s) with min TD-IDF in all text",
    "max_word_TD_IDF":"# Functionality that gives the word(s) with max TD-IDF in all text",
    "word_most_repeated_Chirac":"# Functionality that gives the most repeated word(s) by Chirac",
    "talking_climate:":"# Functionality that gives the first president who talked about climate",
    "talking_nation":"# Functionality that gives which president(s) said the word \"Nation\" and the one who repeated it the most time",
    "all_word_president":"# Functionality that gives the words all presidents have said except the unimportant words",
    }
    if search == "all":
        for keys, value in dic.items():
            print("Test : {}".format(keys))
            print("Function : {}".format(value)) 
        return
    else:
        for keys, value in dic.items():
            if (keys.find(search) != -1) and (value.find(search) != -1) :
                print("Test : {}".format(keys))
                print("Function : {}".format(value))
        return

def sectionFunc():
        print("""
    #################################################################
    #                    Functionality                              #
    #   Please enter a number                                       #
    #   1 - Search for functionality                                #
    #   2 - How to use ?                                            #
    #   3 - Definition of function                                  #
    #   4 - Terminal                                                #
    #   5 - Exit                                                    #
    #################################################################
    """) 
        sub = menu()

        if sub == "1":
            sectionFuncSearch()
        elif sub == "2":
            sectionFuncHow()
        elif sub == "3":
            sectionFuncFunc()
        elif sub == "4":
            terminal()
        elif sub == "5":
            print("!! Returning to the main menu !!")
            time.sleep(2)
            section()
        else:
            print("!! Invalid choice !!")
            time.sleep(2)
            section()
        return 

def sectionFuncSearch():
    print("""
    #################################################################
    #                  Functionality Search                         #
    #################################################################
    """)     
    search = input("# Please enter 3 letter to search in documentation :")
    if len(search) < 3:
            search = input("# !! Please enter 3 letter to search in documentation :")
    else:
        searchFunctionality(search)
        time.sleep(5)
        section()
        return
    return

def sectionFuncHow():
    print("""
    #################################################################
    #                  How to use functionality                     #
    #################################################################
    #                                                               #
    # - You can search with search or command " :func search"       #
    # - Or you can see the documentation of all function with       #
    # ":func func"                                                  #
    # - The best, is to use functionality in the terminal or with   #
    #   ":terminal"                                                 #
    #################################################################
                """)
    time.sleep(5)
    section()
    return
    

def sectionFuncFunc():
    print("""
    #################################################################
    #                        All functionalities                    #
    #################################################################""")
    searchFunctionality("all")
    time.sleep(5)
    section()
    return
    

def terminal():
    while True:
                dir = input("# Terminal # :")

                if dir == "min_word_file_TD_IDF":
                    file = input("Give a name of file :")
                    min_word_file_TD_IDF(file)
                elif dir == "min_word_file_TD_IDF":
                    file = input("Give a name of file")
                    min_word_file_TD_IDF(file)
                elif dir == "min_word_TD_IDF":
                    value = input("Input the number of value that you want :")
                    min_word_TD_IDF(value)
                elif dir == "max_word_TD_IDF":
                    value = input("Input the number of value that you want :") 
                    max_word_TD_IDF(value)
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
     


##################################### Part Test #####################################################

def searchTest(search):
    dic = {"test_extractNameFile()":"# Test for function extractNameFile ",
    "test_assocNamePres()":"# Test for assocNamePres, for Sarkozy",
    "test_listNamePres()":" # Test for listNamePres ",
    "test_score_TF()":"# Test for score_TF",
    "path_cleaned_file":"# Function that gives to a cleaned file its path",
    "path_speeches_file":"# Function that gives to a speeches file its path",
    "min_word_file_TD_IDF":"# Functionality that gives the word(s) that are not important in a file, TD-IDF = 0",
    "max_word_file_TD_IDF":"# Functionality that gives the most important words in a file",
    "min_word_TD_IDF":"# Functionality that gives the word(s) with min TD-IDF in all text",
    "max_word_TD_IDF":"# Functionality that gives the word(s) with max TD-IDF in all text",
    "word_most_repeated_Chirac":"# Functionality that gives the most repeated word(s) by Chirac",
    "talking_climate:":"# Functionality that gives the first president who talked about climate",
    "talking_nation":"# Functionality that gives which president(s) said the word \"Nation\" and the one who repeated it the most time",
    "all_word_president":"# Functionality that gives the words all presidents have said except the unimportant words"
    }
    if search == "all":
        for keys, value in dic.items():
            print("Test : {}".format(keys))
            print("Function : {}".format(value)) 
        return
    else:
        for keys, value in dic.items():
            if (keys.find(search) != -1) or (value.find(search) != -1) :
                print("Test : {}".format(keys))
                print("Function : {}".format(value))
        return

def sectionTest():
        print("""
    #################################################################
    #                            Test                               #
    #   Please enter a number ?                                     #
    #   1 - Search for test                                         #
    #   2 - How to use ?                                            #
    #   3 - Definition of  all test                                 #
    #   4 - Test                                                    #
    #   5 - Exit                                                    #
    #################################################################
    """)
        sub = menu()

        if sub == "1":
            sectionTestSearch()
        elif sub == "2":
            sectionTestHow()
        elif sub == "3":
            sectionTestFunc()
        elif sub == "4":
            test()
        elif sub == "5":
            print("!! Returning to the main menu !!")
            time.sleep(2)
            section()
        else:
            print("!! Invalid choice !!")
            time.sleep(2)
            section()
        return 

def sectionTestSearch():
    print("""
    #################################################################
    #                       Test Search                             #
    #################################################################
    """)     
    search = input("# Please enter 3 letter to search in documentation :")
    if len(search) < 3:
            search = input("# !! Please enter 3 letter to search in documentation :")
    
    searchTest(search)
    time.sleep(5)
    section()
    return

def sectionTestHow():
    print("""
    #################################################################
    #                         How to use test                       #
    #################################################################
    #                                                               #
    # - You can search with search or command " :test search"       #
    # - Or you can see the documentation of all test with           #
    # ":test func"                                                  #
    # - The best, is to use functionality in the terminal or with   #
    #   ":test"                                                     #
    #################################################################
                """)
    time.sleep(5)
    section()
    return

def sectionTestFunc():
    print("""
    #################################################################
    #                        All test                               #
    #################################################################""")
    searchTest("all")
    time.sleep(5)
    section()
    return

def test():
    while True:
                dir = input("# Test # :")


                if dir == "test_extractNameFile":
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
    