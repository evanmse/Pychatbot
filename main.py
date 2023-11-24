from base_function import *
from tf_idf_function import *
from menu_function import *

if __name__ == "__main__":
        displayStart()
        while True:
                dir = menu()
                
                if dir == "1":
                        sectionDoc()
                elif dir == "2":
                        sectionFunc()
                elif dir == "3":
                        sectionTest()
                elif dir == ":doc":
                        sectionDoc()
                elif  dir == ":doc search": 
                        sectionDocSearch()
                elif dir == ":doc how":
                        sectionDocHow()
                elif dir == ":doc func":
                        sectionDocFunc()
                elif dir == ":func":
                        sectionFunc()
                elif dir == ":func search":
                        sectionFuncSearch()
                elif dir == ":func how": 
                        sectionFuncHow()
                elif dir == ":func func":
                        sectionFuncFunc()
                elif dir == ":test":
                        sectionTest()
                elif dir == ":test search":
                        sectionTestSearch()
                elif dir == ":test how":
                        sectionTestHow()
                elif dir == ":test func":
                        sectionTestFunc()
                elif dir == ":section":
                        section()
                elif dir == ":terminal":
                        terminal()
                elif dir == ":test":
                        test()
                elif dir == ":exit":
                        print("Exiting the program. Goodbye!")
                        break
                else:
                        print("!! Invalid choice !!")
