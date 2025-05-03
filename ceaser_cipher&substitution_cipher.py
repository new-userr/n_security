# Caesar Cipher Technique
def caesar_encrypt(text, s):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char 

    return result


# Substitution Cipher Technique
def substitution_encrypt(text, key):
    result = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in text:
        if char.islower():
            index = alphabet.index(char)
            result += key[index]  
        elif char.isupper():
            index = alphabet.index(char.lower())
            result += key[index].upper()  
        else:
            result += char  
    return result


# Testing Caesar Cipher
caesar_text = "ATTACKATONCE"
caesar_shift = 4
print("Caesar Cipher")
print("Text  : " + caesar_text)
print("Shift : " + str(caesar_shift))
print("Cipher: " + caesar_encrypt(caesar_text, caesar_shift))
print("\r")

# Testing Substitution Cipher
substitution_text = "HELLO WORLD"
substitution_key = "qazwsxderfvctgbhnujmikolp"  # A random substitution key
print("Substitution Cipher")
print("Text  : " + substitution_text)
print("Key   : " + substitution_key)
print("Cipher: " + substitution_encrypt(substitution_text, substitution_key))
