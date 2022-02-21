# One-Time Pad Cipher
## overview
This program primarily serves to decipher encrypted messages via a single-use "pad" of letters, shifting each letter of a message to a letter elsewhere in the alphabet as determined by a value, represented by a letter in the pad.

It is also capable of generating such a pad of an specified length, and of enciphering messages given a pad. To encipher or decipher a message, the pad must be of equal or greater length to the number of letters in the message.

Largely, my program accomplishes these functions through use of ASCII characters and values, via the ord() and chr() functions, and basic arithmetic. It is not quite elegant; rather its intent was to mimic in code the process of decrypting and encrypting such messages by hand.

## functions
The program has three main functions. The first is generatePad, which, taking an integer "length" as an argument, appends for each increment of that length a random, capital letter (pads, by convention, are made up of capital letters). The result is a string of random letters of the specified length.

The remaining two, encipher and decipher, operate much the same. They each take as an argument a message and a pad, then iterate over the characters in the message, indexing characters from the pad as necessary to encipher or decipher letters. The encipher function adds together the numerical values 0-25 representing the character from the message and respective character from the pad; the decipher method subtracts the value of the pad character from that of the message character. Each function appends each character as it encrypts/decrypts it to a string that begins empty; the string is then returned once the function has run.

Lastly, there is the main function; this calls upon the others.

## usage
currently, the main function is coded to read into the program an encrypted message and its pad, and calls on the decipher function to print the decrypted message.

If one were to desire the program handle other data, or perform differently when run, it would require going into the main function and altering what is written there.