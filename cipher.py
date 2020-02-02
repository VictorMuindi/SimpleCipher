# A simple substitution cipher is the most commonly used cipher
# The algorithm substitutes every plain text character for every cipher text character

# example
# plaintext: defend the east wall
# ciphertext: giuifg cei iprc tpnn

import random, sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def checkValidKey(key):
    # we turn the letter set and "key" into a list
    keyList = list(key)
    letterList = list(LETTERS)

    # then we sort them
    keyList.sort()
    letterList.sort()

    # then we compare them if they don't match we have a problem
    if keyList != letterList:
        exit("The key doesn't check out...exiting")

def encryptMessage(key, message):
    message = 'defend the wall'
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    print(ord(message))

    # return translateMessage(key, message, 'encrypt')



def decryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def main():
    message = 'defend the wall'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt'

    checkValidKey(myKey)

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, message)
    elif myMode == 'decrypt':
        print("Using the key" + myKey)
        print("The encrypted" + translated)

def translateMessage(key, message, mode):
    translated = ""
    # turn the message and key into a character set
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':
        charsA, charsB = charsB, charsA 

        # loop through each symbol in the message
        for symbol in message:
            if symbol.upper() in charsA:
                symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
                # else:
                #     translated += symbol

    return translated
        
