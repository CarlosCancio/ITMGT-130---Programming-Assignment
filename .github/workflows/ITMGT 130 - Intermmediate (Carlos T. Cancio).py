'''Python: Intermediate

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    if letter == " ":
        return " "
    letter_ascii = ord(letter)
    shifted_ascii = letter_ascii + shift
    if shifted_ascii > 90:
        shifted_ascii = (shifted_ascii - 65) % 26 + 65
    shifted_letter = chr(shifted_ascii)
    return shifted_letter

def caesar_cipher(message, shift):
    shifted_message = ""  
    for char in message:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            shifted_message += shifted_char
        else:
            shifted_message += char
    return shifted_message

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " " 
    letter = letter.upper()
    letter_shift = letter_shift.upper()
    shift_amount = ord(letter_shift) - ord('A')
    shifted_letter = chr((ord(letter) - ord('A') + shift_amount) % 26 + ord('A'))
    return shifted_letter

def vigenere_cipher(message, key):
    key = key.upper()
    message = message.upper()
    key_length = len(key)
    encrypted_message = ""
    extended_key = (key * (len(message) // key_length)) + key[:len(message) % key_length]
    for i in range(len(message)):
        if message[i] == " ":
            encrypted_message += " "
        else:
            shift_amount = ord(extended_key[i]) - ord('A')
            shifted_letter = chr(((ord(message[i]) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_message += shifted_letter
    return encrypted_message

def scytale_cipher(message, shift):
    remainder = len(message) % shift
    if remainder != 0:
        message += "_" * (shift - remainder)
    encoded_message = ""
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        encoded_message += message[index]
    return encoded_message

def scytale_decipher(message, shift):
    deciphered_message = ""
    num_rows = len(message) // shift
    for col in range(shift):
        for row in range(num_rows):
            index = row * shift + col
            deciphered_message += message[index]
    return deciphered_message
