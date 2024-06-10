#01-Import is alpha to check if the input letter is alphabetic
from curses.ascii import isalpha

#02-Input the letter from the user
letter = input("Enter the letter: ")

#03-Case: if the input is validated
if (len(letter) == 1) and (isalpha(letter)):
        #04-Case if the letter is vowel
        if (letter.lower() == 'a') or (letter.lower() == 'e') or (letter.lower() == 'i') or (letter.lower() == 'o') or (letter.lower() == 'u'):
            print("The letter is vowel")
        #04-Case if the letter is not vowel
        else:
            print("The letter is not vowel")
#03-Case: if the input is not validated
else: 
    print("Error: Please Enter One Valid Letter Only")