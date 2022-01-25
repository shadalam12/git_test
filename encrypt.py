import string

def encrypted(message, offset):
    alphabet = string.ascii_lowercase
    punctuation = ",.?!' "
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else: 
            translated_message += letter
    return translated_message

if __name__ == "__main__":
    print(encrypted("shad alam", 10))
