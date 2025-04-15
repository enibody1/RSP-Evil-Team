import os
import time
import hashlib
from collections import defaultdict

WATCH_DIR = "demo_files"  # Folder to monitor
SCAN_INTERVAL = 5         # seconds
THRESHOLD = 10            # suspicious file changes per interval

# File extensions typically seen in ransomware
SUSPICIOUS_EXTENSIONS = [".enc", ".locked", " .txt" ".crypt"]
RANSOM_NOTE_KEYWORDS = ["ransom", "decrypt", "btc", "bitcoin"]

# Store file hashes to detect changes
file_hashes = {}

def hash_file(filepath):
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        return None

def scan_directory():
    current_files = {}
    suspicious_count = 0
    ransom_note_count = 0

    for root, dirs, files in os.walk(WATCH_DIR):
        for file in files:
            filepath = os.path.join(root, file)
            current_files[filepath] = True

            # Count suspicious extensions
            if any(file.endswith(ext) for ext in SUSPICIOUS_EXTENSIONS):
                suspicious_count += 1

            # Check ransom note contents
            if "note" in file.lower() or any(keyword in file.lower() for keyword in RANSOM_NOTE_KEYWORDS):
                try:
                    with open(filepath, "r", errors="ignore") as f:
                        content = f.read().lower()
                        if any(keyword in content for keyword in RANSOM_NOTE_KEYWORDS):
                            ransom_note_count += 1
                except Exception:
                    pass

            # Check if the file has been modified
            file_hash = hash_file(filepath)
            if file_hash:
                if filepath not in file_hashes:
                    file_hashes[filepath] = file_hash
                elif file_hashes[filepath] != file_hash:
                    suspicious_count += 1
                    file_hashes[filepath] = file_hash

    # Detect deleted files
    deleted_files = set(file_hashes.keys()) - set(current_files.keys())
    suspicious_count += len(deleted_files)
    for df in deleted_files:
        del file_hashes[df]

    return suspicious_count, ransom_note_count

def monitor():
    print(f"[*] Monitoring '{WATCH_DIR}' for suspicious activity...")
    while True:
        suspicious_count, ransom_note_count = scan_directory()

        if suspicious_count >= THRESHOLD or ransom_note_count > 0:
            print(f"[!] ALERT: Suspicious activity detected!")
            print(f"    - File changes: {suspicious_count}")
            print(f"    - Ransom notes: {ransom_note_count}")
            # You can add alert/logging/email logic here

        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    monitor()