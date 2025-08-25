'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.'''
    if letter == " ":
        return " "
    base = ord("A")
    new_pos = (ord(letter) - base + shift) % 26
    return chr(base + new_pos)

def caesar_cipher(message, shift):
    '''Caesar Cipher.'''
    return "".join(shift_letter(ch, shift) for ch in message)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.'''
    if letter == " ":
        return " "
    base = ord("A")
    shift_val = ord(letter_shift) - base
    new_pos = (ord(letter) - base + shift_val) % 26
    return chr(base + new_pos)

def vigenere_cipher(message, key):
    '''Vigenere Cipher.'''
    result = []
    base = ord("A")
    # Extend key to match the full message length (including spaces)
    extended_key = (key * ((len(message) // len(key)) + 1))[:len(message)]

    for m_char, k_char in zip(message, extended_key):
        if m_char == " ":
            result.append(" ")
        else:
            shift_val = ord(k_char) - base
            new_pos = (ord(m_char) - base + shift_val) % 26
            result.append(chr(base + new_pos))
    return "".join(result)

def scytale_cipher(message, shift):
    '''Scytale Cipher.'''
    while len(message) % shift != 0:
        message += "_"
    n = len(message)
    encoded = []
    for i in range(n):
        index = (i // shift) + (n // shift) * (i % shift)
        encoded.append(message[index])
    return "".join(encoded)

def scytale_decipher(message, shift):
    '''Scytale De-cipher.'''
    n = len(message)
    decoded = [""] * n
    for i in range(n):
        index = (i // shift) + (n // shift) * (i % shift)
        decoded[index] = message[i]
    return "".join(decoded)
