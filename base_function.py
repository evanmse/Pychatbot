import os
import re
import string

directory = "./speeches"


def list_of_files(directory, extension):  # Function that gives the list of files, Example : /speeches
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extractNameFile(nameFile):  # Function that extracts the name of the president in the name of a certain file
    match = re.match(r"Nomination_([a-zA-Z\s]+)\d*.txt", nameFile)  # Pattern to find in the name of files
    if match:
        return match.group(1)  # We just want to keep the groupe [Name of president]
    else:
        return None  # If he doesn't find the group with the pattern


def assocNamePres(namePresident):  # Function that associate to a president name, its first name
    dictPres = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François', 'Macron': 'Emmanuel',
                'Mitterrand': 'François', 'Sarkozy': 'Nicolas'}
    return dictPres[namePresident]


def lowerClean():
    return


def clearFile():
    return


def list_namePres():  # Function that displays the list of the names of the presidents without duplications(doublons)
    list_file = list_of_files(directory, "txt")
    president_names = [extractNameFile(filename) for filename in list_file]
    return list(set(president_names))