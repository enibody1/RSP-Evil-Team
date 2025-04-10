from cryptography.fernet import Fernet
import os

# Load key
with open("key.key", "rb") as key_file:
    key = key_file.read()

# Create Fernet object
cipher = Fernet(key)

# Define the path to the encrypted file
filepath = "demo_files/zacchaeus.jpg.enc"
filepath = "demo_files/lazarus.txt.enc"
filepath = "demo_files/methuselah.docx.enc"

# Decrypt the file
with open(filepath, "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = cipher.decrypt(encrypted_data)

print("Decrypted message:")
print(decrypted_data.decode())