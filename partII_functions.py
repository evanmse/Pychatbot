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

def question_TF_IDF(question): #TD_IDF Question
    TF =  score_TF(question)
    IDF = score_IDF("./cleaned")
    TF_IDF = {}
    for value1, item1 in TF.items():
            for value2, item2 in IDF.items():
                if value1 == value2:
                    TF_IDF[value1] = TF[value2]*IDF[value1]
                if value1 not in IDF:
                    TF_IDF[value1] = 0
    return TF_IDF

def scalar(vectA, vectB):
    n = len(vectA)
    scal = 0
    for i in range(n):
        scal += (vectA[i]*vectB[i])
    return scal

def norm(vectA):
    n =len(vectA)
    norm = 0
    for i in range(n):
        norm += vectA[i]**2
    return sqrt(norm)

def similarity(vectA, vectB):
    try:
        simi = scalar(vectA, vectB)/(norm(vectA)*norm(vectB))
    except:
        simi = 0
    return simi

def most_relevant_doc(matrix_TD_IDF, question_TF_IDF,listNamePres):
    

    return