"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Step 1 : input secret number
    Step 2 : input cipher words
    Step 3 : find new alphabet
    Step 4 : start to decipher
    Step 5 : change lower case into upper case, avoid case-sensitive condition
    Step 6 : find sequence in new alphabet, and find correspond sequence in original alphabet
    Step 7 : if the cipher is not alphabet, copy it and put in deciphered sentence.
    Step 8 : print the deciphered sentence
    """
    secret = int(input('Secret number: '))
    cipher = input('What\'s the ciphered string? ')
    new_alphabet = ALPHABET[26-secret:] + ALPHABET[:26-secret]
    ans = ''
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            cipher = cipher.upper()
            sequence = new_alphabet.find(cipher[i])
            ans = ans + ALPHABET[sequence]
        else:
            ans = ans + cipher[i]
    print('The deciphered string is: ' + str(ans))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
