import hashlib

# SHA256
str1 = "Network Security"
result = hashlib.sha256(str1.encode())
print("The hexadecimal equivalent of SHA256 is :")
print(result.hexdigest())
print("\r")

# SHA384
str2 = "Cryptography"
result = hashlib.sha384(str2.encode())
print("The hexadecimal equivalent of SHA384 is :")
print(result.hexdigest())
print("\r")

# SHA224
str3 = "Cybersecurity"
result = hashlib.sha224(str3.encode())
print("The hexadecimal equivalent of SHA224 is :")
print(result.hexdigest())
print("\r")

# SHA512
str4 = "Hello World"
result = hashlib.sha512(str4.encode())
print("The hexadecimal equivalent of SHA512 is :")
print(result.hexdigest())
print("\r")
