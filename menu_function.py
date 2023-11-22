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
    
    dir = str(input("Enter a number to go in section or a shortcut :"))
    while not dir in setAnswer:
        dir = input("!! Please retry to enter a correct number or shortcut : ")         
    return dir

def searchFunc(search):
    dic = {"list_of_files()":"# Function that gives the list of files, Example : /speeches",
    "extractNameFile()":"# Function that extracts the name of the president in the name of a certain file",
    "listNamePres()":"# Function that displays the list of the names of the presidents without duplications(doublons)",
    "assocNamePres()":"# Function that associate to a president name, its first name",
    "lowerClean()":"# Input file to go lowercase",
    "clearFile()":"# Main function for clean File",
    "cleanText()":"# Sub-Function that clean a text",
    "path_cleaned_file()":"# Function that give to a cleaned file its path",
    "path_speeches_file()":"# Function that give to a speeches file its path"
    }
    if search == "all":
        for keys, value in dic.items():
            print("Function : {}".format(keys))
            print("Function : {}".format(value)) 
        return
    else:
        for keys, value in dic.items():
            if (keys.find(search) != -1) and (value.find(search) != -1) :
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
        else:
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
    #   2 - How to us ?                                             #
    #   3 - Definition of function                                  #
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
    #                  How to us the documentation                  #
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
    dic = {"min_word_file_TD_IDF":"# Functionality that give the word that not important in file, TD-IDF = 0",
    "min_word_file_TD_IDF":"# Functionality that give the word that most important in file, TD-IDF near of 1",
    "min_word_TD_IDF":"# Functionality that give the word with min TD-IDF in all text",
    " max_word_TD_IDF":"# Functionality that give the word with max TD-IDF in all text",
    "repeat_word_pres":"# Functionality that give the most word repeat by a president",
    "talking_climate:":"# Functionality that give who talks about climate",
    "talking_nation":"# Functionality that give who talks about climate",
    "all_word_president":"# Functionality words all presidents have spoken without the unimportant words",
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
    #   Please enter a number ?                                     #
    #   1 - Search for functionality                                #
    #   2 - How to us ?                                             #
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
    #                  How to us functionality                      #
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
    #                        All functionality                      #
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
                elif dir == "repeat_word_pres":
                    president = input("What prsident do you want :")
                    repeat_word_pres(president)
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
    "path_cleaned_file":"# Function that give to a cleaned file its path",
    "path_speeches_file":"# Function that give to a speeches file its path"
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

def sectionTest():
        print("""
    #################################################################
    #                            Test                               #
    #   Please enter a number ?                                     #
    #   1 - Search for test                                         #
    #   2 - How to us ?                                             #
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
    else:
        searchTest(search)
        time.sleep(5)
        section()
        return
    return
    

def sectionTestHow():
    print("""
    #################################################################
    #                         How to us test                        #
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

                if dir == "min_word_file_TD_IDF":
                    test_extractNameFile()
                elif dir == "min_word_file_TD_IDF":
                    file = input("Give a name of file")
                    min_word_file_TD_IDF(file)
                elif dir == "min_word_TD_IDF":
                    value = input("Input the number of value that you want :")
                    min_word_TD_IDF(value)
                elif dir == "max_word_TD_IDF":
                    value = input("Input the number of value that you want :") 
                    max_word_TD_IDF(value)
                elif dir == "repeat_word_pres":
                    president = input("What prsident do you want :")
                    repeat_word_pres(president)
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
    