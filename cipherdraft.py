import random

def generatePad(length):
    new_pad = ''
    for a in range(0, length):
        new_pad += chr(random.randint(65, 90))

    return new_pad

##def shift(shift_len, character):
    ##if ord(character) in range(65, 91):
        ##character = ord(character) - 65

        ##character = (character + shift_len) % 26

        ##character += 65
        ##character = chr(character)

    ##elif ord(character) in range(97, 123):
        ##character = ord(character) - 97

        ##character = (character + shift_len) % 26

        ##character += 97
        ##character = chr(character)
    
    ##return character

##def encipher(message, pad):
    ##coded_message = ''

    ##pad_index = 0
    ##for b in message:
        ##pad_shift = pad[pad_index] - 97

        ##coded_message += shift(pad_shift, b)
        ##pad_index += 1
    ##return coded_message

##def decipher(coded_message, pad):
    ##message = ''

    ##pad_index = 0
    ##for b in coded_message:
        ##pad_shift = ord(pad[pad_index]) - 97

        ##message += shift(-pad_shift, b)
        ##pad_index += 1
    ##return message

def decipher(coded_message, pad):

    message = ''
    #letter = True
    #uppercase = True
    #pad_index = 0
    offset = 0

    for b in range(len(coded_message)):
    #for b in coded_message:
        letter = True
        uppercase = True

        if ord(coded_message[b]) in range(65, 91):
            character = ord(coded_message[b]) - 65
            #uppercase = True
            #letter = True
        elif ord(coded_message[b]) in range(97, 123):
            character = ord(coded_message[b]) - 97
            uppercase = False
            #letter = True
        else:
            letter = False

        #if ord(b) in range(65, 91):
            #character = ord(b) - 65
            #uppercase = True
            #letter = True
        #elif ord(b) in range(97, 123):
            #character = ord(b) - 97
            #uppercase = False
            #letter = True
        #else:
            #letter = False

        #pad_character = ord(pad[b]) - 65
        pad_character = ord(pad[b - offset]) - 65
        #pad_character = ord(pad[pad_index]) - 65

        if letter:
            if character < pad_character:
                character += 26
            
            decoded_character = character - pad_character

            if uppercase:
                decoded_character += 65
            else:
                decoded_character += 97
            
            decoded_character = chr(decoded_character)
            #pad_index += 1
        else:
            #decoded_character = b
            decoded_character = coded_message[b]
            offset += 1
        
        message += decoded_character
    
    return message

def encipher(message, pad):

    coded_message = ''
    offset = 0

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
    with open('pad.txt') as pad_text:
        pad = pad_text.read()
    with open('encrypted-message.txt') as message_text:
        message = message_text.read()

    print(decipher(message, pad))

    print("enciphering message: Happy Valentine's Day!")
    val_pad = generatePad(22)
    print('pad: ' + val_pad)
    print(encipher("Happy Valentine's Day!", val_pad))
    print(decipher(encipher("Happy Valentine's Day!", val_pad), val_pad))

    ##pad_length = int(input('pad for fun! what length would you like your pad to be? '))
    ##print(generatePad(pad_length))

main()