import string

directory = "./speeches"

def score_TF(strings_chain):  # Function that associates to each word how many times it appeared in a strings_chain



    dictionnary = {}
    punctuations = string.punctuation #A string that contains all the punctuations
    mylist_words = []

    for caracter in strings_chain:
        if caracter not in punctuations:
            mylist_words.append(caracter)       #Append to mylist_words all the caracters that are not punctuations
        else:
            mylist_words.append(' ')            #Replace all the punctuations by space

    str_chain_no_punctuations = ''.join(mylist_words)
    list_chain_no_punctuations = str_chain_no_punctuations.split(" ")

    for i in range(list_chain_no_punctuations.count("")):   #Remove all the "" in the list
        list_chain_no_punctuations.remove("")

    for k in range(list_chain_no_punctuations.count("\n")):  #Remove all the elements \n in the list
        list_chain_no_punctuations.remove("\n")

    for element in range(len(list_chain_no_punctuations)):  #Remove all the \n in words
        if "\n" in list_chain_no_punctuations[element]:
            list_chain_no_punctuations[element] = list_chain_no_punctuations[element].replace("\n", '')

    list_unique_word = list(set(list_chain_no_punctuations))  #Remove all the duplications

    for word in list_unique_word:
        dictionnary[word] = list_chain_no_punctuations.count(word)   #Create the dictionnary

    return dictionnary