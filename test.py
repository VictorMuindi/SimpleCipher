import string
import re

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = "Its not a story the Jedi would tell"
key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'

def encrypt(key, message):
    # this function removes the whitespaces from the message
    def remove(string): 
        pattern = re.compile(r'\s+')
        return re.sub(pattern, '', string)

    # it is importany to remember the string operations are case sensitive 
    # hence the lower function

    keyList = list(key)
    messageLength = len(remove(message.lower()))
    messageList = list(remove(message.lower()))
    messageArray = [] 
    messageNum = []
    encrypted_mess = " "
    d = 0
    x = 0

    for d in range(messageLength):
        # push the letters into an array
        messageArray.append(messageList[d])
        # push their numerical value  into another array
        messageNum.append(string.ascii_lowercase.index(messageArray[d]))
    
    for x in range(messageLength):
        #with each iteration in the for loop
        # the corresponding letter to the number
        # is added to the encrypted message
        encrypted_mess += keyList[messageNum[x]]
    
    # print(encrypted_mess)
    return encrypted_mess

print("The message: ", message)
print("The encrypted cipher", encrypt(key, message))