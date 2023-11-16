from base_function import *

if __name__ == "__main__":
        directory = "./speeches"
        files_names = list_of_files(directory, "txt")

        # Test for function extractNameFile :
        president_names = [extractNameFile(filename) for filename in files_names] #List of president
        print("Président names:", president_names) #Print of the list


        # Test for assocNamePres :
        print(assocNamePres(president_names[3]))

        #Test for list_namePres :
        print(list_namePres())