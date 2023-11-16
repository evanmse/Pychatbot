import os
import re

def list_of_files(directory, extension):  #Function that give the list of files, Example : /speeches
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extractNameFile(nameFile):
    match = re.match(r"Nomination_([a-zA-Z\s]+)\d*.txt", nameFile) #Pattern to find in the name of files
    if match:
        return match.group(1) #We just want to keep the groupe [Name of president]
    else:
        return None #If he don't find the group with the pattern

def assocNamePres(namePresident):
    dictPres = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François', 'Macron': 'Emmanuel', 'Mitterrand': 'François','Sarkozy': 'Nicolas' }
    return dictPres[namePresident]

def lowerClean():
    return

def clearFile():
    return