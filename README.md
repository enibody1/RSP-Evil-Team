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

## Files

- ```encryptor.py```: Main script that encrypts files and generates ransom note.

- ```decryptor.py```: Script to decrypt the files if the correct key is available.

- ```README.md```: This file.

- ```key.key```: Generated encryption key.

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

## Author

Uchendu, Favour Eni & 
