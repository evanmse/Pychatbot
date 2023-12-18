"""

pychatbot-MASSE-LOESCH_Int2, Evan MASSE, Thomas LOESCH.

This file contains all the features asked in the instructions.

"""




from tf_idf_function import score_TF, score_IDF
from base_function import path_speeches_file, cleanText, listNamePres, extractNameFile, list_of_files

def max_score_TF_IDF():  # Function that calculates the highest TF-IDF score
    dictionnary_scoreIDF_word = score_IDF('./speeches')
    maxi = 0
    files_name = list_of_files('./speeches', 'txt')

    for file in files_name:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            dictionnary_scoreTF_word = score_TF(content)

        for i in dictionnary_scoreTF_word:  # Calculate the maximum TF-IDF score
            if (dictionnary_scoreTF_word[i] * dictionnary_scoreIDF_word[i]) > maxi:
                maxi = dictionnary_scoreTF_word[i] * dictionnary_scoreIDF_word[i]

    return maxi


def min_word_TD_IDF():  # Functionality that gives the word(s) with TF-IDF = 0 in all text
    mylist = []
    dictionnary_scoreIDF_word = score_IDF('./speeches')

    files_name = list_of_files('./speeches','txt')

    for file in files_name:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            list_of_word = list(score_TF(content).keys())
            dictionnary_scoreTF_word = score_TF(content)

        for i in list_of_word:
            if (dictionnary_scoreTF_word[i] * dictionnary_scoreIDF_word[i]) == 0:  # If score TF-IDF is 0
                mylist.append(i)

    return list(set(mylist))


def max_word_TD_IDF():  # Functionality that gives the word(s) with max TD-IDF in all text

    dictionnary_scoreIDF_word = score_IDF('./speeches')
    maxi = max_score_TF_IDF()
    files_name = list_of_files('./speeches', 'txt')
    mylist = []

    for file in files_name:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            dictionnary_scoreTF_word = score_TF(content)

        for i in dictionnary_scoreTF_word:  # Calculate the maximum TF-IDF score
            if (dictionnary_scoreTF_word[i] * dictionnary_scoreIDF_word[i]) == maxi:
                mylist.append(i)

    return list(set(mylist))


def word_most_repeated_Chirac():  # Functionality that gives the most repeated word by Chirac

    content = ''
    files_name = list_of_files('./speeches', 'txt')
    mylist_Chirac = [text for text in files_name if 'Chirac' in text]
    mylist = []

    for file in mylist_Chirac:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = content + f.read()

    dictionnary_scoreTF_word = score_TF(content)

    unimportant_words = min_word_TD_IDF()

    for word in list(dictionnary_scoreTF_word.keys()):
        if word in unimportant_words:
            del dictionnary_scoreTF_word[word]

    maxi = max(list(dictionnary_scoreTF_word.values()))

    for key in list(dictionnary_scoreTF_word.keys()):
        if dictionnary_scoreTF_word[key] == maxi:
            mylist.append(key)

    return mylist


def talking_climate():  # Functionality that gives the first president who talked about climate
    files_name = list_of_files('./speeches', 'txt')

    index_min = float('inf')  # index_min equals to infinity

    for file in files_name:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            content = cleanText(content)
            mylist = content.split(" ")

            for i in range(mylist.count("")):
                mylist.remove("")

            for j in range(
                    len(mylist)):  # If the index is inferior to the previous files, index is update and the president too
                if ("climat" in mylist[j] or "écologie" in mylist[j]) and (j < index_min):
                    index_min = j
                    president_climate_ecology = extractNameFile(file)
                    break

    return president_climate_ecology


def talking_nation():  # Functionality that gives which president(s) said the word "Nation" and the one who repeated it the most time

    files_name = list_of_files('./speeches', 'txt')
    maxi = 0
    mylist = []

    for file in files_name:
        full_path = path_speeches_file(file)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            dictionary_scoreTF_word = score_TF(content)
            list_words_content = list(dictionary_scoreTF_word.keys())

        if "nation" in list_words_content:  # Verify if nation is a word in the file
            mylist.append(extractNameFile(file))  # If yes, the name of the president is added to mylist
            if dictionary_scoreTF_word["nation"] > maxi:  # Calculate how many times a certain president said the word
                maxi = dictionary_scoreTF_word["nation"]
                president_talked_most_nation = extractNameFile(file)

    print("Presidents that talked about the nation : ", list(set(mylist)))
    print("The president who said the most time the word nation :", president_talked_most_nation)
    return


def all_word_president():  # Functionality that gives the words all presidents have said except the unimportant words

    list_name_pres = listNamePres("./speeches", "txt")
    files_name = list_of_files('./speeches', 'txt')
    word_TF_IDF_zero = min_word_TD_IDF()
    mylist = []

    for president in list_name_pres:
        content = ''

        for file in files_name:  # Regroup in a list all the words that presidents have said in common
            full_path = path_speeches_file(file)
            if president in file:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = content + f.read()
                    list_word = list(score_TF(content).keys())

        mylist.append(set(list_word))

    word_in_common = list(set.intersection(*mylist))  # Find the intersection between all the sets in my list
    word_in_common = [word for word in word_in_common if word not in word_TF_IDF_zero]

    return word_in_common
