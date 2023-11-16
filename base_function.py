import os
import re

directory = "./speeches"

def list_of_files(directory, extension):  #Function that gives the list of files, Example : /speeches
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extractNameFile(nameFile):  #Function that extracts the name of the president in the name of a certain file
    match = re.match(r"Nomination_([a-zA-Z\s]+)\d*.txt", nameFile) #Pattern to find in the name of files
    if match:
        return match.group(1) #We just want to keep the groupe [Name of president]
    else:
        return None #If he doesn't find the group with the pattern

def assocNamePres(namePresident):
    dictPres = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François', 'Macron': 'Emmanuel', 'Mitterrand': 'François','Sarkozy': 'Nicolas' }
    return dictPres[namePresident]

def lowerClean(inputFile): # Input name of file to go upper
    # Path of the files and directory
    path_input_file = "./speeches/{}".format(inputFile)
    path_cleaned_dir = "./cleaned"
    path_cleaned_file = "./cleaned/{}".format(inputFile)
    # Test if the file exists 
    if not os.path.exists(path_cleaned_dir):
        os.mkdir(path_cleaned_dir)
    # Copy the content from speeches to cleaned with change letter lowercase
    with open(path_input_file, 'r', encoding='utf-8') as file, open(path_cleaned_file, 'w', encoding='utf-8') as output_file:
            content = file.read()
            content_lower = content.lower()
            output_file.write(content_lower)
    # Security close of file
    file.close()
    output_file.close()
    return

def clearFile():


    return

def list_namePres():  #Function that displays the list of the names of the presidents without duplications(doublons)
    list_file = list_of_files(directory, "txt")
    president_names = [extractNameFile(filename) for filename in list_file]
    return list(set(president_names))