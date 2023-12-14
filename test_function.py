from base_function import *
from tf_idf_function import *
from menu_function import *
from partII_functions import *

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

def test_assocNamePres_Sarkozy(): # Test for assocNamePres, for "Sarkozy" 
    print("### Test for assocNamePres ### ")
    print(assocNamePres("Sarkozy"))
    return

def test_listNamePres():   # Test for listNamePres :
    print("### Test for listNamePres ### ")
    print(listNamePres(directory, "txt"))
    return

def test_score_TF(): # Test for score_TF
    print("### Test for score_TF for Nomination_Chirac1.txt ### ")
    with open('./speeches/Nomination_Chirac1.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
            print(score_TF(file_content))
    return

def test_lowerClean(): # Test for lowerClean :        
    print("### Test for function lowerClean ### ")
    for name in list_of_files(directory, "txt"):
        lowerClean(name)
    print("Text is now in lowercase")
    return

def test_clearFile():  # Test for clearFile :
    print("### Test for function clearFile ### ")
    for name in list_of_files("./cleaned", "txt"):
        clearFile(name)
    print("Text is now clear")
    return

def test_Similarity(question):
    print("#### Test similarity ####")
    x = question_TF_IDF(question)

    list_value_question_TD_IDF = []
    list_word_question = []

    for item, val in x.items():
        list_value_question_TD_IDF.append(val)
        list_word_question.append(item)

    matrix = []  #List containing the values of the score TF-IDF of the words of the question

    for document in list_of_files("./cleaned", "txt"):
        temp = []
        for word in list_word_question:
            try:
                temp.append(score_TF_IDF(document,word))
            except:
                 temp.append(0)
        matrix.append(temp)
    print("This is the matrix of similarity of word of the question: ", matrix)

    result = []
    for i in range(len(list_of_files("./cleaned", "txt"))):
            result.append(similarity(matrix[i],list_value_question_TD_IDF))
            print(result[i:])
    return result
