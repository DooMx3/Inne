def encrypt(message, key):
    encrypted = ""
    for letter in message:
        if ord(letter) < ord('a') or ord(letter) > ord('z'):
            encrypted += letter
        elif ord(letter) + key > ord('z'):
            encrypted += chr(ord(letter) + key - 26)
        else:
            encrypted += chr(ord(letter) + key)
    return encrypted


def decrypt(message, key):
    encrypted = ""
    for letter in message:
        if ord(letter) < ord('a') or ord(letter) > ord('z'):
            encrypted += letter
        elif ord(letter) - key < ord('a'):
            encrypted += chr(ord(letter) - key + 26)
        else:
            encrypted += chr(ord(letter) - key)
    return encrypted


print(decrypt("Sxevnubexm ndqdł!", 3))
