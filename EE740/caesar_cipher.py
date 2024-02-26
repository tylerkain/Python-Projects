def caesar_cipher_encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # If it's not a letter, add it as it is (to handle spaces, punctuation)
        else:
            result += char

    return result


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


# Example usage
plaintext = "CONFIDENTIAL DATA"
shift = 3

encrypted_text = caesar_cipher_encrypt(plaintext, shift)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

(encrypted_text, decrypted_text)
