import codecs

def rot13(text):
    return codecs.encode(text, 'rot_13')

# Contoh
plaintext = input()
ciphertext = rot13(plaintext)
print(ciphertext)
