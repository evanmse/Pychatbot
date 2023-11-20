from base_function import *
from tf_idf_function import *

if __name__ == "__main__":
        # Main variables
        directory = "./speeches"
        files_names = list_of_files(directory, "txt")

        # Test for function extractNameFile :
        print("\n### Test for function extractNameFile ### ")
        president_names = []
        for filename in files_names:
                president_names.append(extractNameFile(filename))  #List of president
        print("Président names:", president_names) #Print of the list


        # Test for assocNamePres :
        print("\n### Test for assocNamePres ### ")
        print(assocNamePres(president_names[3]))

        #Test for listNamePres :
        print("\n### Test for listNamePres ### ")
        print(listNamePres(directory, "txt"))

        #Test for score_TF
        print("\n### Test for score_TF ### ")
        with open('./speeches/Nomination_Chirac1.txt', 'r', encoding='utf-8') as file:
              file_content = file.read()
              print(score_TF(file_content))

        # Test for lowerClean :
        print("\n### Test for function lowerClean ### ")
        for name in list_of_files(directory, "txt"):
                lowerClean(name)

        # Test for clearFile :
        print("\n### Test for function clearFile ### ")
        for name in list_of_files("./cleaned", "txt"):
                clearFile(name)

        # Test for score_IDF :
        print("\n### Test for function score_IDF ### ")
        print(score_IDF('./speeches'))
