def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Contoh
plaintext = input()
ciphertext = caesar_cipher(plaintext, 3)  # Geser 3 huruf
print(ciphertext)
