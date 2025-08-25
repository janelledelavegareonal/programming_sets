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
    key_index = 0
    for ch in message:
        if ch == " ":
            result.append(" ")
        else:
            shift_val = ord(key[key_index % len(key)]) - base
            new_pos = (ord(ch) - base + shift_val) % 26
            result.append(chr(base + new_pos))
            key_index += 1
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


# ------------------ TEST BLOCK ------------------ #
if __name__ == "__main__":
    print("Testing shift_letter:")
    print(shift_letter("A", 0))  # A
    print(shift_letter("A", 2))  # C
    print(shift_letter("Z", 1))  # A
    print(shift_letter("X", 5))  # C
    print(shift_letter(" ", 5))  # " "

    print("\nTesting caesar_cipher:")
    print(caesar_cipher("HELLO WORLD", 3))  # KHOOR ZRUOG

    print("\nTesting shift_by_letter:")
    print(shift_by_letter("A", "A"))  # A
    print(shift_by_letter("A", "C"))  # C
    print(shift_by_letter("B", "K"))  # L
    print(shift_by_letter(" ", "D"))  # " "

    print("\nTesting vigenere_cipher:")
    print(vigenere_cipher("A C", "KEY"))        # K A
    print(vigenere_cipher("LONGTEXT", "KEY"))   # BQBKZQXB

    print("\nTesting scytale_cipher:")
    print(scytale_cipher("INFORMATION_AGE", 3))  # IMNNA_FTAOIGROE
    print(scytale_cipher("INFORMATION_AGE", 4))  # IRIANMOGFANEOT__
    print(scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8))  # AOTSRIOALRH_EMRNGIMA_PTT

    print("\nTesting scytale_decipher:")
    print(scytale_decipher("IMNNA_FTAOIGROE", 3))        # INFORMATION_AGE
    print(scytale_decipher("IRIANMOGFANEOT__", 4))       # INFORMATION_AGE_
    print(scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8))  # ALGORITHMS_ARE_IMPORTANT
