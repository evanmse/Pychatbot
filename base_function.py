import os



def list_of_files(directory, extension):  # Function that gives the list of files, Example : /speeches
    files_names = []

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)

    return files_names

def extractNameFile(nameFile):  # Function that extracts the name of the president in the name of a certain file
    namePres = "" # Variable for the result

    nameSplit = nameFile.split("_")[1] # Split the name of the file and keep group 1 [Nomination_][[nom d’un president][numéro].txt]
    nameSplit = nameSplit.split(".")[0] # Split the name of group 1 and keep before the dot group [[nom d’un president][numéro]][.txt]

    for char in nameSplit: # Function that test in nameSplit if he has a number
        if char.isspace():
            namePres += " "
        elif char.isalpha():
            namePres += char

    return namePres

def listNamePres(inputFile, extension):  #Function that displays the list of the names of the presidents without duplications(doublons)
    list_name_pres = []

    for name_file in list_of_files(inputFile, extension):
        list_name_pres.append(extractNameFile(name_file))

    return list(set(list_name_pres))

def assocNamePres(namePresident): # Function that associate to a president name, its first name
    dictPres = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François', 'Macron': 'Emmanuel', 'Mitterrand': 'François','Sarkozy': 'Nicolas' }
    return dictPres[namePresident]

def lowerClean(inputFile): # Input name of file to go upper
    # Test if the file exists
    path_cleaned_dir = "./cleaned" 
    if not os.path.exists(path_cleaned_dir):
        os.mkdir(path_cleaned_dir)

    # Copy the content from speeches to cleaned with change letter in lowercase
    with open(path_speeches_file(inputFile), 'r', encoding='utf-8') as file, open(path_cleaned_file(inputFile), 'w', encoding='utf-8') as output_file:
        content = file.read()
        output_file.write(content.lower()) # Writes the contents of a file in speeches to a file in cleaned in lowercase

    # Security close of file
    file.close()
    output_file.close()

    return

def clearFile(inputFile): #Main function for clean File
    path_file = path_cleaned_file(inputFile)

    with open(path_file, 'r', encoding='utf-8') as file:
        text = file.read()

    clearText = cleanText(text) #Call the sub-function for clean the text

    with open(path_file, 'w', encoding='utf-8') as file:
        file.write(clearText) # Write the clean text

    return 

def cleanText(text): #Sub-Function that clean a text
    dicReplace = {'é':'e', 'à':'a', 'è':'e', 'ç':'c', 'ê': 'e', 'ë': 'e', 'ù':'u', 'â':'a'} # Dictionary of values to be changed
    punctuation = [',',';','-','!','?','\'','.',':','"','`'] # List of punctuation to be change

    for character in punctuation: # Replace of ponctuation
        text = text.replace(character,' ')

    for keys, value in dicReplace.items(): #Replace with dicReplace
        text = text.replace(keys, value)

    return text

def path_cleaned_file(inputFile): #Function that give to a cleaned file its path
    path_cleaned_file = "./cleaned/{}".format(inputFile)
    return path_cleaned_file

def path_speeches_file(inputFile): #Function that give to a speeches file its path
    path_input_file = "./speeches/{}".format(inputFile)
    return path_input_file

