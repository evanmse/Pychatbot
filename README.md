# 🐍 Pychatbot MASSE LOESCH Int2

# Terminal Command Interface for Text Analysis

This repository contains a Python script that provides a terminal-based interface for various text analysis functionalities. The script allows users to analyze text data related to presidential speeches. Below are the available functionalities and their corresponding commands that can be used by running the main.py file:

### Functionalities:

1. **min_word_TD_IDF**
   - Command: `min_word_TD_IDF`
   - Description: Function that gives the word(s) with TF-IDF = 0 in all the texts.

2. **max_word_TD_IDF**
   - Command: `max_word_TD_IDF`
   - Description: Function that gives the word(s) with the highest score TF-IDF in all the texts.

3. **word_most_repeated_Chirac**
   - Command: `word_most_repeated_Chirac`
   - Description: Function that finds and prints the most repeated word(s) by Chirac.

4. **talking_climate**
   - Command: `talking_climate`
   - Description: Function that identifies the first president who talks about climate or ecology.

5. **talking_nation**
   - Command: `talking_nation`
   - Description: Function that determines which president(s) mentioned the word 'Nation' and identifies the president who repeated it the most times.

6. **all_word_president**
   - Command: `all_word_president`
   - Description: Function that gives the words said by all the presidents, excluding unimportant words.

7. **score_IDF**
    - Command: `score_IDF`
    - Description: Function that computes the IDF score of each word in the entire corpus.

8. **score_TF_IDF**
    - Command: `score_TF_IDF`
    - Description: Function that returns the score TF-IDF of a certain word in a certain document.

9. **matrix_TD_IDF**
    - Command: `matrix_TD_IDF`
    - Description: Functions that computes and generates the matrix TF-IDF.
      
10. **score_TF**
    - Command: `score_TF`
    - Description: Function that associates to each word how many times it appeared in a string chain
      
11. **extractNameFile**
    - Command: `extractNameFile`
    - Description: Function that extracts the name of the president in the name of a certain file.

12. **assocNamePres**
    - Command: `assocNamePres`
    - Description: Function that associates to a president name, its first name.
      
13. **listNamePres**
    - Command: `lowerClean`
    - Description: Function used to convert the texts in the 8 files to lower case and store the contents in new files.

14. **cleanText**
    - Command: `cleanText`
    - Description: Function used to remove any punctuation characters of each file of the cleaned directory.
    
15. **question_tokenization**
    - Command: `question_tokenization`
    - Description: Tokenizes the input question, returning a list of words.

16. **question_words_corpus**
    - Command: `question_words_corpus`
    - Description: Finds terms that intersect between the set of words in the corpus and the set of words in the question.

17. **question_TF_IDF**
    - Command: `question_TF_IDF`
    - Description: Returns the TF-IDF vector of the input question

18. **most_relevant_doc**
    - Command: `most_relevant_doc`
    - Description: Identifies the most similar document in relation to a given question.

19. **word_highest_TF_IDF_question**
    - Command: `word_highest_TF_IDF_question`
    - Description: Returns the word with the highest TF-IDF score in the question.

20. **sentence_word_highest_TF_IDF**
    - Command: `sentence_word_highest_TF_IDF`
    - Description: Retrieves a sentence containing the word with the highest TF-IDF score from the most relevant document.

### Additional Functions:

- ** Search Functionality in the terminal**
  -You can call for a function listed in the documentation in order to test it in the terminal.

Feel free to explore and analyze text data using this versatile terminal interface!

To exit the terminal, use the command `exit`. Enjoy exploring the functionalities!
