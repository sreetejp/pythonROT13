def encrypt(message):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    encrypted_message = ""

    for char in message:
        if char in characters:
            char_index = characters.index(char)

            shifted_index = (char_index + 13) % len(characters)

            encrypted_char = characters[shifted_index]
        else:
            encrypted_char = char

        encrypted_message += encrypted_char

    return encrypted_message

def decrypt(encrypted_message):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    decrypted_message = ""

    for char in encrypted_message:
        if char in characters:
            char_index = characters.index(char)

            shifted_index = (char_index - 13) % len(characters)

            decrypted_char = characters[shifted_index]
        else:
            decrypted_char = char

        decrypted_message += decrypted_char

    return decrypted_message

message = input("Enter the message you want to encrypt/decrypt: ")

encrypted_message = encrypt(message)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)