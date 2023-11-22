from base_function import *
from tf_idf_function import *
from menu_function import *


# Main variables
directory = "./speeches"
files_names = list_of_files(directory, "txt")

def test_extractNameFile():    # Test for function extractNameFile 
    print("### Test for function extractNameFile ### ")
    president_names = []
    for filename in files_names:
            president_names.append(extractNameFile(filename))  #List of president
    print("Président names:", president_names) #Print of the list
    return

def test_assocNamePres(): # Test for assocNamePres, for "Sarkozy" 
    print("### Test for assocNamePres ### ")
    print(assocNamePres("Sarkozy"))
    return

def test_listNamePres():   # Test for listNamePres :
    print("### Test for listNamePres ### ")
    print(listNamePres(directory, "txt"))
    return

def test_score_TF(): # Test for score_TF
    print("### Test for score_TF ### ")
    with open('./speeches/Nomination_Chirac1.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
            print(score_TF(file_content))
    return

def test_lowerClean(): # Test for lowerClean :        
    print("### Test for function lowerClean ### ")
    for name in list_of_files(directory, "txt"):
        lowerClean(name)
    return

def test_clearFile():  # Test for clearFile :
    print("### Test for function clearFile ### ")
    for name in list_of_files("./cleaned", "txt"):
        clearFile(name)
    return