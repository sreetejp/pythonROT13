import codecs

text = input("Enter some text to encrypt or decrypt: ")

if text == codecs.encode(text, "rot13"):
    decrypted_text = codecs.decode(text, "rot13")
    print(f"Decrypted text: {decrypted_text}")
else:
    encrypted_text = codecs.encode(text, "rot13")
    print(f"Encrypted text: {encrypted_text}")

input("Press enter to exit.")
