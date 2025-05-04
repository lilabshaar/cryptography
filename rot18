def rot18(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 13) % 26 + base)
        elif char.isdigit():
            result += chr((ord(char) - ord('0') + 5) % 10 + ord('0'))
        else:
            result += char
    return result

# Contoh
plaintext = input()
ciphertext = rot18(plaintext)
print(ciphertext)
