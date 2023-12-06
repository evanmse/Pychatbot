from tf_idf_function import score_IDF
from base_function import cleanText

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

