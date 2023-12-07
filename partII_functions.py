from tf_idf_function import *
from base_function import *

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
    print(TF)
    IDF = score_IDF("./cleaned")
    TF_IDF = {}
    for value1, item1 in TF.items():
            for value2, item2 in IDF.items():
                if value1 == value2:
                    TF_IDF[value1] = TF[value2]*IDF[value1]
                if value1 not in IDF:
                    TF_IDF[value1] = 0
    return TF_IDF