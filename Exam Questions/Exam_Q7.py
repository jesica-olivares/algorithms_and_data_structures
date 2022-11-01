#Implement the Vigenere Cipher
#Although the idea of the Vigenere Cipher is very basic it took humanity over 300 years to break it. 
# Ultimately, frequency analysis broke it. Develop the class to encrypt and decrypt using the cipher developed by Vigenere.

import string
def vigenere_cipher(word,shift):
    abc=string.ascii_lowercase
    abc+=abc
    output=""
    for i in word:
        letter=abc[abc.find(i)+shift]
        output=output+letter

    print(output)

word="aaabbbccczzz"
shift=2

vigenere_cipher(word,shift)
