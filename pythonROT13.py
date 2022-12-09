import string

def rot13_encrypt_decrypt(message):
    encrypted_decrypted_message = ""

    for char in message:
        if char in string.ascii_uppercase:
            encrypted_decrypted_message += string.ascii_uppercase[(string.ascii_uppercase.index(char) + 13) % 26]
        elif char in string.ascii_lowercase:
            encrypted_decrypted_message += string.ascii_lowercase[(string.ascii_lowercase.index(char) + 13) % 26]
        else:
            encrypted_decrypted_message += char

    return encrypted_decrypted_message

message = input("Enter the message to encrypt/decrypt: ")

print(rot13_encrypt_decrypt(message))