from cryptography.fernet import Fernet
import os
from decryption_gui import show_decryption_success_gui  # Import the GUI function from the renamed helper file

decrypted_files = []  # List to store successfully decrypted files

# Load the encryption key from file
with open("key.key", "rb") as key_file:
    key = key_file.read()

# Initialize Fernet object using the key
fernet = Fernet(key)

# Traverse all files in the target directory
for root, dirs, files in os.walk("demo_files"):
    for file in files:
        filepath = os.path.join(root, file)  # Full path of the current file

        # Skip files that are not encrypted (i.e., disguised as .txt)
        if not file.endswith(".txt"):
            continue

        # Try to restore the original filename (remove .txt extension)
        restored_name = filepath.replace(".txt", "")  # Remove .txt suffix from the file name

        try:
            # Read the encrypted file content
            with open(filepath, "rb") as f:
                encrypted_data = f.read()

            # Decrypt the content
            decrypted_data = fernet.decrypt(encrypted_data)

            # Write decrypted content to the restored filename
            with open(restored_name, "wb") as f:
                f.write(decrypted_data)

            # Remove the encrypted file after decryption
            os.remove(filepath)

            # Add to list of successfully decrypted files (relative to demo_files)
            decrypted_files.append(os.path.relpath(restored_name, "demo_files"))

            # Debugging: Print the decrypted file path
            print(f"Decrypted: {restored_name}")

        except Exception as e:
            # Log files that couldn't be decrypted
            print(f"[!] Skipped file: {file} ({e})")

# Delete ransom notes after decryption
for root, dirs, files in os.walk("demo_files"):
    for file in files:
        if "ransom_note" in file.lower():
            os.remove(os.path.join(root, file))

# Write decrypted files log
with open("decryption_log.txt", "w") as log:
    for f in decrypted_files:
        log.write(f"{f}\n")

# Debugging: Print all decrypted files in the log
print("Decrypted Files List:")
for file in decrypted_files:
    print(file)

# Launch GUI confirmation window showing decrypted files
show_decryption_success_gui(decrypted_files)