import os
from Crypto.Cipher import AES
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Symmetric Encryption (AES)
def symmetric_encryption():
    key = os.urandom(32)  # 256-bit key
    plaintext = b'This is a secret message'
    
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Decrypting
    cipher_decrypt = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    decrypted_message = cipher_decrypt.decrypt(ciphertext)

    print("\n[Symmetric AES Encryption]")
    print("Original Message:", plaintext.decode())
    print("Encrypted Message:", ciphertext)
    print("Decrypted Message:", decrypted_message.decode())

# Asymmetric Encryption (RSA)
def asymmetric_encryption():
    # Generate RSA private and public keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Encrypting
    message = b"This is an RSA encrypted message"
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None)
    )

    # Decrypting
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None)
    )

    print("\n[Asymmetric RSA Encryption]")
    print("Original Message:", message.decode())
    print("Encrypted Message:", ciphertext)
    print("Decrypted Message:", decrypted_message.decode())

if __name__ == "__main__":
    symmetric_encryption()
    asymmetric_encryption()
