#very basic cypher test
#do not use for anything sensetive

import random
import string

characters = " " + string.punctuation + string.ascii_letters + string.digits
characters = list(characters)
key = characters.copy()

random.shuffle(key)

#print(f"characters: {characters}")
#print(f"key: {key}")

#encrpytion stage
plain_text = input("Enter plain text: ")
cipher_text = ""

for letter in plain_text:
    index = characters.index(letter)
    cipher_text += key[index]

print(f"Original Message : {plain_text}")
print(f"Encrypted Message: {cipher_text}")

#decryption stage
cipher_text = input("Enter a message to decrypt ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += characters[index]

print(f"Encrypted Message : {cipher_text}")
print(f"Original Message: {plain_text}")
