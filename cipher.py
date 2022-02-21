# Allison Adams one-time pad cipher program
# February 2022 for CSC 151

import random

# function that generates a 'pad'
# returns a random sequence of capital letters, of a specified length, as a string.

def generatePad(length):
    new_pad = ''
    for a in range(0, length):
        new_pad += chr(random.randint(65, 90))

    return new_pad


# function that decrypts a message using a pad

def decipher(coded_message, pad):

    # the 'message' variable will store the output message letter by letter as it decrypts
    # 'offset' increments each time the loop encounters a non-letter in the encrypted message, ensuring letters of the pad will not be used up
    
    message = ''
    offset = 0

    for b in range(len(coded_message)):

        # a boolean that stores whether the character being iterated over is a letter
        # and the same that store whether it is uppercase

        letter = True
        uppercase = True

        # an if/elif/else loop that accomplishes three things:
        # determines if the character being iterated over is in the alphabet by way of ASCII values,
        # and if it is, storing in the variable 'character' as a value from 0-25 indicating which letter it is,

        # setting the bool 'uppercase' to False if a lowercase letter is found,

        # and if the character is not a letter, setting 'letter' to false

        if ord(coded_message[b]) in range(65, 91):
            character = ord(coded_message[b]) - 65
        elif ord(coded_message[b]) in range(97, 123):
            character = ord(coded_message[b]) - 97
            uppercase = False
        else:
            letter = False

        # this stores the pad character aligning with the message character as a value from 0-25
        
        pad_character = ord(pad[b - offset]) - 65

        # a couple things happen in this if/else:
        # if letter is true, the code then decrypts the character. If not, 'decoded_charater' simply stores the character being iterated over as is

        # if the character was uppercase going in, a second if/else ensures it will be uppercase going out
        
        if letter:
            if character < pad_character:
                character += 26
            
            decoded_character = character - pad_character

            if uppercase:
                decoded_character += 65
            else:
                decoded_character += 97
            
            decoded_character = chr(decoded_character)
        else:
            decoded_character = coded_message[b]
            offset += 1
        
        message += decoded_character
    
    return message


# function that encrypts a message using a pad

def encipher(message, pad):

    # 'coded_message' and 'offset' serve the same purposes as 'message' and 'offset' for the decipher function

    coded_message = ''
    offset = 0

    # the following is almost identical to the decipher function above
    # the major difference being it adds the values of character and pad_character rather than subtracts

    for c in range(len(message)):
        letter = True
        uppercase = True

        if ord(message[c]) in range(65, 91):
            character = ord(message[c]) - 65
        elif ord(message[c]) in range(97, 123):
            character = ord(message[c]) - 97
            uppercase = False
        else:
            letter = False

        pad_character = ord(pad[c - offset]) - 65

        if letter:
            coded_character = (character + pad_character) % 26

            if uppercase:
                coded_character += 65
            else:
                coded_character += 97
            
            coded_character = chr(coded_character)
        else:
            coded_character = message[c]
            offset += 1
        
        coded_message += coded_character
    
    return coded_message



def main():

    # stores the content of pad.txt and ecrypted-message.txt as strings

    with open('pad.txt') as pad_text:
        pad = pad_text.read()
    with open('encrypted-message.txt') as message_text:
        message = message_text.read()

    # calls the decipher function with the message and pad as its arguments
    # then prints the returned decrypted string

    print(decipher(message, pad))



main()