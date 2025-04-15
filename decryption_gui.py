# Import necessary modules for GUI, threading, file handling, and time control
import tkinter as tk  # For GUI elements (buttons, labels, etc.)
import threading  # To run background tasks, like the auto-close timer
import os  # File operations (not used here, but can be helpful in the future)
import subprocess  # To open the folder via the system's default file explorer
import time  # To implement sleep delay (for auto-closing the GUI)

# Function to show a successful decryption GUI
def show_decryption_success_gui(decrypted_files):
    
    # Function to open the demo_files folder in the file explorer
    def open_folder():
        subprocess.Popen(["xdg-open", "demo_files"])  # Linux command to open the directory

    # Function to close the GUI window
    def close():
        window.destroy()  # Close the Tkinter window

    # Create the main Tkinter window
    window = tk.Tk()
    window.title("Decryption Complete")  # Set window title
    window.geometry("350x180")  # Set window size
    window.resizable(False, False)  # Make the window size fixed (not resizable)

    # Label that informs the user the decryption was successful
    label = tk.Label(window, text="Your files have been successfully decrypted!", font=("Arial", 11), wraplength=300)
    label.pack(pady=10)  # Add the label to the window and add padding

    # Text box to display the list of decrypted files
    text_box = tk.Text(window, height=5, width=40, wrap="none")  # Define text box for file list
    for f in decrypted_files:  # Loop through the list of decrypted files
        text_box.insert("end", f"{f}\n")  # Insert each file into the text box
    text_box.config(state="disabled")  # Make the text box read-only (disabled)
    text_box.pack(pady=5)  # Pack the text box into the window with padding

    # Create a frame to hold the buttons (Open Folder and Close)
    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=5)  # Pack the frame to the window with padding

    # Button to open the folder where decrypted files are stored
    open_btn = tk.Button(btn_frame, text="Open Folder", command=open_folder, width=12)  # Create button
    open_btn.pack(side="left", padx=10)  # Pack button on the left side of the frame with padding

    # Button to close the window
    close_btn = tk.Button(btn_frame, text="Close", command=close, width=12)  # Create button
    close_btn.pack(side="right", padx=10)  # Pack button on the right side of the frame with padding

    # Run a background thread to close the window after a delay of 5 seconds
    threading.Thread(target=lambda: time.sleep(5) or close(), daemon=True).start()  # Wait for 5 seconds and close

    # Start the Tkinter event loop to display the window
    window.mainloop()