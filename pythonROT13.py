import codecs  # Import the codecs module

# Ask the user for some text to encrypt or decrypt
text = input("Enter some text to encrypt or decrypt: ")

# Check if the text is already encrypted
if text == codecs.encode(text, "rot13"):
    # The text is encrypted, so decrypt it
    decrypted_text = codecs.decode(text, "rot13")
    print(f"Decrypted text: {decrypted_text}")
else:
    # The text is not encrypted, so encrypt it
    encrypted_text = codecs.encode(text, "rot13")
    print(f"Encrypted text: {encrypted_text}")

# Keep the script running until the user is ready to exit
input("Press enter to exit.")
