import nltk

from nltk.corpus import words
#Import words list from above module
word_list = words.words()
import random, time


#Create list for alphabets and morse code symbols
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
morse_symbols = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']

dict_alphabet_to_morse = {alpha:morse_symbol for alpha,morse_symbol in zip(alphabet,morse_symbols)}

#Test by checking lengths of both lists and the dictionary comprehension formed
#print(len(alphabet))
#print(len(morse_symbols))
#print(dict_alphabet_to_morse)

def word_creator(l):
    #Create empty string and counter variable
    string = ""
    count = 0  
    #While the string is not in the word list, do not accept the string and reset to empty string
    while string not in word_list:
        string = ""
        #while string is less than no of letters chosen by user, continue to add a letter to the string at random
        while len(string) < int(l):
            string += alphabet[random.randint(0,len(alphabet)-1)]
        #Increment counter but break if taking too long as words in list incopmrehensibly long
        count += 1
        if count > 2000:
            break
    else:
        return string

#Define function to convert word into morse code
def convert_word_to_morse_code(word):
    morse_version_word_chosen = ""
    for letter in word:
        morse_version_word_chosen += dict_alphabet_to_morse[letter]
        morse_version_word_chosen += " "
    return morse_version_word_chosen

#Define function to test knowledge of morse code
def test_morse_code():
    #Require user input for length of word
    l = input('What length word would you like to play with? ')
    word_chosen = None
    #Use function to create word 
    while word_chosen is None:
        word_chosen = word_creator(l)
    else:
        #Allow for some time, then convert the word to morse code and display to the user
        time.sleep(5)
        morse_code_shown = convert_word_to_morse_code(word_chosen)
        print(morse_code_shown)
        #Ask for the user to convert it as part of the test
        user_guess = input('Please attempt to convert from morse code to the word (type in lowercase): ')
        #If it is correct, display the 'you are correct' message
        if (user_guess == word_chosen):
            print('You are correct')
        #Otherwise, display the 'you are incorrect' message and reveal the word
        else:
            print('You are incorrect. The word was ' + word_chosen)

def run():
    test_morse_code()

if __name__ == "__main__":
    run()
