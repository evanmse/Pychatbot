"""

pychatbot-MASSE-LOESCH_Int2, Evan MASSE, Thomas LOESCH.

This file contains the basic functions asked in the instructions. The functions allow to clean a file, extract the
name of a president, have the name of the files and so on.

"""



import os

def list_of_files(directory, extension):  # Function that gives the list of files in a directory, Example : /speeches

    """

    :param directory: the parameter directory is the directory within which the function is going to return a list of all the files present in the directory.
    :param extension: the parameter extension is the type of the files that we are going to put in the list. (txt, jpg, ...)
    :return: a list containing all the names' files of a certain directory of a certain type.

    """

    files_names = []

    for filename in os.listdir(directory):                  #Creation of the list of files
        if filename.endswith(extension):
            files_names.append(filename)

    return files_names

def extractNameFile(nameFile):  # Function that extracts the name of the president in the name of a certain file

    """

    :param nameFile: It is the name of the file
    :return: The name of the president in the name's file

    """
    namePres = "" # Variable for the result

    nameSplit = nameFile.split("_")[1]  # Split the name of the file and keep group 1 [Nomination_][[nom d’un president][numéro].txt]
    nameSplit = nameSplit.split(".")[0]  # Split the name of group 1 and keep before the dot group [[nom d’un president][numéro]][.txt]

    for char in nameSplit: # Function that test in nameSplit if he has a number
        if char.isspace():
            namePres += " "
        elif char.isalpha():
            namePres += char

    return namePres

def listNamePres(inputFile, extension):  #Function that displays the list of the names of the presidents without duplications(doublons)
    """

    :param inputFile: Directory within which we are going to extract the name of the presidents
    :param extension: Extension of the files with which we are going to extract the name of the presidents
    :return: The list with the names of the presidents in the directory.

    """


    list_name_pres = []

    for name_file in list_of_files(inputFile, extension):
        list_name_pres.append(extractNameFile(name_file))      #Add to the list the name of the president in the name's file

    return list(set(list_name_pres))

def assocNamePres(namePresident): # Function that associates to a president name, its first name
    """

    :param namePresident: The name of a president
    :return: The first name of a president whose name was the parameter

    """

    dictPres = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François', 'Macron': 'Emmanuel', 'Mitterrand': 'François','Sarkozy': 'Nicolas' }
    return dictPres[namePresident]

def lowerClean(inputFile):    # Function that converts the text into lowercase in a new folder
    """

    :param inputFile: A file
    :return: Nothing because the function just rewrites in lowercase the content of a file in a new folder.

    """
    # Test if the file exists
    path_cleaned_dir = "./cleaned" 
    if not os.path.exists(path_cleaned_dir):
        os.mkdir(path_cleaned_dir)

    # Copy the content from speeches to cleaned with change letter in lowercase
    with open(path_speeches_file(inputFile), 'r', encoding='utf-8') as file, open(path_cleaned_file(inputFile), 'w', encoding='utf-8') as output_file:
        content = file.read()
        output_file.write(content.lower()) # Writes the contents of a file in speeches to a file in cleaned in lowercase


    file.close()
    output_file.close()

    return

def clearFile(inputFile): # Function that moves a text removed from accents and punctuations to a file in the cleaned folder

    """

    :param inputFile: A file
    :return: Nothing because the function just moves a text removed from accents and
    punctuations to a file in the cleaned folder

    """
    path_file = path_cleaned_file(inputFile)

    with open(path_file, 'r', encoding='utf-8') as file:
        text = file.read()

    clearText = cleanText(text)  #Cleans the text

    with open(path_file, 'w', encoding='utf-8') as file:
        file.write(clearText) # Write the clean text

    return 

def cleanText(text): # Function that removes from a text any accents and punctuations

    """

    :param text: A string
    :return: The functions returns the string but without accents, punctuations

    """
    dicReplace = {'é':'e', 'à':'a', 'è':'e', 'ç':'c', 'ê': 'e', 'ë': 'e', 'ù':'u', 'â':'a', '\n' : ' ', 'ô': 'o', 'î' : 'i', 'û' : 'u'}
    punctuation = [',',';','-','!','?','\'','.',':','"','`']

    for character in punctuation: # Replace of ponctuation
        text = text.replace(character,' ')

    for keys, value in dicReplace.items(): #Replace with dicReplace
        text = text.replace(keys, value)

    return text

def cleanText_with_dot(text): # Function that removes from a text any accents and punctuations except the dot.

    """

    :param text: A string
    :return: The functions returns the string but without accents, punctuations, except the dot.

    """

    dicReplace = {'é': 'e', 'à': 'a', 'è': 'e', 'ç': 'c', 'ê': 'e', 'ë': 'e', 'ù': 'u', 'â': 'a', '\n': ' ', 'ô': 'o',
                  'î': 'i', 'û': 'u'}
    punctuation = [',', ';', '-', '!', '?', '\'', ':', '"', '`']

    for character in punctuation:  # Replace of ponctuation
        text = text.replace(character, ' ')

    for keys, value in dicReplace.items():  # Replace with dicReplace
        text = text.replace(keys, value)

    return text

def path_cleaned_file(inputFile): # Function that gives to a cleaned file its path

    """

    :param inputFile: A file
    :return: the functions returns the path of a file in the folder cleaned.

    """
    path_cleaned_file = "./cleaned/{}".format(inputFile)            #Create the path in the cleaned folder
    return path_cleaned_file

def path_speeches_file(inputFile): # Function that gives to a speeches file its path

    """

    :param inputFile: A file
    :return: the function returns the path of a file in the folder speeches.

    """
    path_input_file = "./speeches/{}".format(inputFile)     #Create the path in the speeches folder
    return path_input_file
