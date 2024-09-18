# Function to decrypt the cryptogram using a shift key
def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_message = ''
    for char in cryptogram:
        if char.isalpha():
            if char.islower():
                decrypted_message += chr(((ord(char) - ord('a') - shift_key) % 26) + ord('a'))
            elif char.isupper():
                decrypted_message += chr(((ord(char) - ord('A') - shift_key) % 26) + ord('A'))
        else:
            decrypted_message += char
    return decrypted_message

# Input from the user
ciphered_quote = input("Enter the ciphered quote: ")
shift_key = int(input("Enter the shift key: "))

# Decrypting the ciphered quote
decrypted_quote = decrypt_cryptogram(ciphered_quote, shift_key)

# Output
print(f"\nDecrypted Quote: {decrypted_quote}")
