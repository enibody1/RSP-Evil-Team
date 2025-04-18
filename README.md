# Ransomware Simulation Project

This project is a simulated ransomware script designed for educational and research purposes only. It demonstrates how ransomware operates in a controlled environment to help learners understand the underlying mechanics of malicious file encryption, as well as to aid in developing defenses against such attacks.

## Disclaimer

This project is for educational purposes only. Do NOT use it on any system without explicit permission. I do not condone or support the use of ransomware for malicious purposes.

## Features

- Simulates ransomware behavior by encrypting files in a specified directory.

- Uses the cryptography library for symmetric key encryption (Fernet).

- Generates an encryption key and stores it separately.

- Displays a ransom note with instructions.

- Includes functionality to decrypt files if the correct key is provided.

## Technologies Used

- Python 3

- ```cryptography``` library

## Project Structure

RSP-Evil-Team/

│

├── encryptor.py              # Main script to encrypt files and write ransom notes

├── decryptor.py              # Main script to decrypt files and restore original filenames

├── ransomware_gui.py         # GUI for the ransomware attack (e.g., countdown, warnings)

├── decryption_gui.py         # GUI for showing decryption success and displaying decrypted files

├── persistence.py            # Persistence setup for simulating autostart on system boot

├── decryption_log.txt        # Log of decrypted files (generated after decryption)

├── demo_files/               # Directory containing demo files for encryption/decryption

├── key.key                   # Encryption key file used during encryption and decryption

├── ransom_note.txt           # Simulated ransom instructions

└── README.md                 # Project README file (this file)

ransomware_simulator/
│
├── encryptor.py            # Script to encrypt files and drop ransom note
├── decryptor.py            # Script to decrypt files with a key
├── key.key                 # Generated encryption key
├── ransom_note.txt         # Template ransom message (used in script)
├── demo_files/             # Test files that will be encrypted
└── README.md   

## Files

- ```encryptor.py```: This script is responsible for encrypting files in a specified directory (demo_files). It generates a unique encryption key, encrypts the files, and saves them with a .txt extension. It also writes a ransom note in each folder containing encrypted files.

- ```decryptor.py```: This script is used to decrypt files that have been encrypted by the encryptor.py. It reads the key from the key.key file, decrypts the .txt files (which were originally encrypted), and restores the original filenames. It also launches a GUI showing a list of decrypted files.

- ```ransomware_gui.py```: This script contains the graphical user interface (GUI) for the ransomware simulation. It includes a countdown timer that is shown to the user before the attack is initiated. This script manages the window that alerts the user of the encryption process.

- ```decryption_gui.py```: This file is responsible for the GUI displayed after the decryption is complete. It shows the user a list of successfully decrypted files and provides options like "Open Folder" to view the restored files or "Close" to exit the GUI.

- ```persistence.py```: This script simulates the persistence mechanism for the ransomware, ensuring it runs automatically at startup (to mimic the persistence of ransomware on a system). It sets up a cron job to run the ransomware each time the system reboots, simulating a real-world ransomware persistence mechanism.

- ```decryption_log.txt```: This file is created by decryptor.py after successfully decrypting files. It logs all the decrypted file paths for reference. The log helps the user verify which files were decrypted during the recovery process.

- ```ransom_note.txt```: Simulated ransom instructions.

## How It Works

1. The ransomware script searches for files in a given directory.

2. It encrypts the files using a randomly generated key.

3. It saves the key to a file and deletes the original versions.

4. A ransom note is created, mimicking real-world ransomware tactics.

5. The decrypt.py script can be used with the key to reverse the encryption.

## Setup and Usage

### Requirements

- Python 3.9
- Install dependencies:
```pip install cryptography```

### Running the Ransomware Simulation
```python encryptor.py```

### Decryption (after getting the key)
```python decryptor.py```

Ensure the key.key file is present in the same directory before running the decrypt script.

## Educational Use Cases

- Demonstrating the risk and behavior of ransomware.

- Teaching about cybersecurity and ethical hacking.

- Practicing threat detection and incident response in a lab environment.

## Authors

Uchendu, Favour Eni & Oladimeji, Richard
