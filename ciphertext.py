def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("Caesar Cipher Program")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_message = encrypt(message, shift)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted Message: {decrypted_message}")
