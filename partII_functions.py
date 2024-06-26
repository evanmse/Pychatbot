"""

pychatbot-MASSE-LOESCH_Int2, Evan MASSE, Thomas LOESCH.

This file contains all the functions asked in part II.

"""

from tf_idf_function import *
from base_function import *
from math import *


def question_tokenization(question):
    """
    Function that takes the text of the question and returns the list of words that make up the question.

    :param question: Question asked by the user
    :return: A list of each word of the question
    """

    content = question.lower()
    content = cleanText(content)
    mylist = content.split(" ")  # Transformation into a list

    for i in range(mylist.count("")):  # Removing all the ""
        mylist.remove("")

    return mylist


def question_words_corpus(question):
    """
    Function that looks for terms that form the intersection between the set of words in the corpus and the
    set of words in the question.

    :param question: Question asked by the user
    :return: a list of terms that form the intersection between the set of words in the corpus and the
    set of words in the question.
    """

    words_corpus = list(score_IDF('./speeches').keys())

    words_in_question = list(set(question_tokenization(question)))

    return list(set(words_corpus) & set(words_in_question))  # Returning the intersection between the two sets


def question_TF_IDF(question):
    """
    Function that returns the TF-IDF vector of the question

    :param question: Question asked by the user
    :return: the TF-IDF vector of the question

    """
    TF = score_TF(question)
    list_word_question = list(TF.keys())
    IDF = score_IDF("./cleaned")
    TF_IDF = {}

    for value in list_word_question:  # Suppression of the words that are not in the corpus
        if value not in list(IDF.keys()):
            del TF[value]

    for value1, item1 in TF.items():  # Calculating the TF-IDF score of each word
        TF_IDF[value1] = item1 * IDF[value1]

    return TF_IDF


def scalar(vectA, vectB):
    """
    Function that calculates the scalar product of two vectors

    :param vectA: First vector
    :param vectB: Second vector

    :return: the scalar product of these two vectors

    """
    n = len(vectA)
    scal = 0
    for i in range(n):
        scal += (vectA[i] * vectB[i])  # Calculating the scalar product
    return scal


def norm(vectA: list):
    """
    Function that calculates the norm of a vector

    :param vectA: A vector
    :return: Its norm

    """
    n = len(vectA)
    norm = 0
    for i in range(n):
        norm += vectA[i] ** 2  # Calculating the norm
    return sqrt(norm)


def similarity(vectA, vectB):
    """

    Function that calculates the similarity between two vectors

    :param vectA: First vector
    :param vectB: Second Vector
    :return: The similarity score

    """
    try:
        simi = scalar(vectA, vectB) / (norm(vectA) * norm(vectB))
    except:
        simi = 0  # In the case where there is a division by zero
    return simi


def most_relevant_doc(matrix_TD_IDF, question_TF_IDF, files_name):
    """

    Function that returns the most similar document in relation to a question

    :param matrix_TD_IDF: The matrix TD_IDF of the corpus
    :param question_TF_IDF: The TF-IDF vector of the question
    :param files_name: the list of the files' name
    :return: the most similar document in relation to a question


    """

    IDF = score_IDF('./cleaned')
    index = 0
    similar_quantity = -1

    for file in files_name:
        index += 1
        document_vector = []

        with open(path_cleaned_file(file), 'r', encoding='utf-8') as f:
            content = cleanText(f.read().lower())
            TF = score_TF(content)
            list_of_word_document = list(TF.keys())

            for word in list(question_TF_IDF.keys()):  # Calculating the document vector
                if word in list_of_word_document:
                    document_vector.append(TF[word] * IDF[word])
                else:
                    document_vector.append(0)

            if similar_quantity < similarity(list(question_TF_IDF.values()),
                                             document_vector):  # Finding the most relevant document
                similar_quantity = similarity(list(question_TF_IDF.values()), document_vector)
                name_document = file

    return name_document


def word_highest_TF_IDF_question(question):
    """
    Function that returns the word with the highest score TF-IDF in the question

    :param question: Question asked by the user
    :return: If the TF-IDF vector of the question is empty, then it returns None. Otherwise, it returns
    the word with the highest score TF-IDF in the question
    """

    dict_TF_IDF_question = question_TF_IDF(question)
    if dict_TF_IDF_question != {}:
        max_value_word = max(dict_TF_IDF_question,
                             key=dict_TF_IDF_question.get)  # Allows us to get the key with the highest value
        return max_value_word
    else:
        return None


def sentence_word_highest_TF_IDF(question):
    """
    Function that locates the first occurrence of the word with the highest score in the most relevant document
    and returns the sentence containing it as the answer

    :param question: Question asked by the user
    :return: the sentence in which there is the word with the highest TF-IDF in the question in the most relevant document

    """

    word_highest_TF_IDF = word_highest_TF_IDF_question(question)

    if word_highest_TF_IDF is None:
        return "There are no words in the question that are in the corpus."
    else:

        relevant_document = most_relevant_doc(matrix_TD_IDF('./cleaned'),
                                              question_TF_IDF(question), list_of_files('./cleaned', 'txt'))

        question_formulation = {
            "Comment": "Après analyse, ",
            "Pourquoi": "Car, ",
            "Peux-tu": "Oui, bien sûr! ",
            "Pouvez-vous": "Oui, bien sûr! "
        }

        in_the_text = False

        with open(path_speeches_file(relevant_document), 'r', encoding="utf-8") as f:
            index = -1
            content = f.read()

            phrases = cleanText_with_dot(content).lower().split('.')

            for phrase in phrases:
                index += 1  # Locate the index of the sentence
                if word_highest_TF_IDF in phrase.split():
                    in_the_text = True
                    break

            phrase_containing_word = content.split(".")[index]  # Get the sentence

            phrase_containing_word = phrase_containing_word.replace('-', '')
            phrase_containing_word = phrase_containing_word.replace('\n', '')

            if in_the_text:
                if question.split(" ")[0] in list(
                        question_formulation.keys()):  # If the question begins with one of the keys of the dictionary question_formulation
                    return question_formulation[question.split(" ")[0]] + phrase_containing_word.lstrip("- \t\n") + "."
                else:
                    return phrase_containing_word.lstrip("- \t\n") + "."
            else:
                return "The word with the highest TF-IDF score is not in the most relevant document."
