from cryptography.fernet import Fernet
message = "hello world"
key = Fernet.generate_key()
fernet = Fernet(key)
# Encrypt the message (convert to bytes first)
encMessage = fernet.encrypt(message.encode())
print("Original string:", message)
print("Encrypted string:", encMessage)
# Decrypt the encrypted message
decMessage = fernet.decrypt(encMessage).decode()
print("Decrypted string:", decMessage)
