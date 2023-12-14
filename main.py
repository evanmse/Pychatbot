from base_function import *
from tf_idf_function import *
from menu_function import *
from partII_functions import *

if __name__ == "__main__":
        
        for name in list_of_files("./speeches", "txt"):  #Backbone of the menu
                lowerClean(name)
        for name in list_of_files("./cleaned", "txt"):
                clearFile(name)
        
        question = "Pain baguette jeu joue tout vous v"
        test_Similarity(question)

        displayStart()
        while True:
                dir = menu()

                if dir == "1" or dir == "documentation":
                        documentation()
                elif dir == "2" or dir == "terminal":
                        terminal()
                elif dir == "3" or dir == "exit":
                        print("Exiting the program. Goodbye!")
                        break
                else:
                        print("!!! Invalid choice !!!")
