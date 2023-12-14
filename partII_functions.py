from tf_idf_function import *
from base_function import *
from math import *

def question_tokenization(question):
    """
    Function that takes the text of the question and returns the list of words that make up the question.
    """

    content = question.lower()
    content = cleanText(content)
    mylist = content.split(" ")

    for i in range(mylist.count("")):  # Remove all the "" in the list
        mylist.remove("")

    return mylist

def question_words_corpus(question):
    """
    Function that looks for terms that form the intersection between the set of words in the corpus and the
    set of words in the question.

    """

    words_corpus = list(score_IDF('./speeches').keys())

    words_in_question = list(set(question_tokenization(question)))

    return list(set(words_corpus) & set(words_in_question))

def question_TF_IDF(question): #Function that returns the TF-IDF vector of the question
    TF =  score_TF(question)
    IDF = score_IDF("./cleaned")
    TF_IDF = {}
    for value1, item1 in TF.items():
        for value2, item2 in IDF.items():
            if value1 == value2:
                TF_IDF[value1] = TF[value2]*IDF[value1]
            elif value1 not in IDF:
                TF_IDF[value1] = 0
    return TF_IDF

def scalar(vectA, vectB):       #Function that calculates the scalar product of two vectors
    n = len(vectA)
    scal = 0
    for i in range(n):
        scal += (vectA[i]*vectB[i])
    return scal

def norm(vectA:list):       #Function that calculates the norm of a vector
    n =len(vectA)
    norm = 0
    for i in range(n):
        norm += vectA[i]**2
    return sqrt(norm)

def similarity(vectA, vectB):   #Function that calculates the similarity between two vectors
    try:
        simi = scalar(vectA, vectB)/(norm(vectA)*norm(vectB))
    except:
        simi = 0
    return simi

def most_relevant_doc(matrix_TF_IDF, question_TF_IDF, files_name):
    """
    Function that returns the most similar document in relation to a question
    """

    IDF = score_IDF('./cleaned')
    index = 0
    similar_quantity = -1

    visual_matrix_TD_IDF(matrix_TF_IDF)

    for file in files_name:
        index += 1
        document_vector = []


        for j in range(len(list(IDF.keys()))):
            document_vector.append(matrix_TF_IDF[j][index])

        print(document_vector)
        print()

        if similar_quantity < similarity(list(question_TF_IDF.values()), document_vector):
            similar_quantity = similarity(list(question_TF_IDF.values()), document_vector)
            name_document = file


    return name_document

print(most_relevant_doc(matrix_TD_IDF('./cleaned'), question_TF_IDF('"Peux-tu me dire comment une nation peut-elle prendre soin du climat ?'), list_of_files('./cleaned', 'txt')))
