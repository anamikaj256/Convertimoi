import tkinter as tk
from tkinter import messagebox
import random
import time

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Practice makes a man perfect.",
    "Coding is fun and rewarding.",
    "Artificial intelligence is the future of technology.",
]

# Global variables
start_time = 0
selected_sentence = ""

# Functions
def start_game():
    """Start the game by displaying a random sentence."""
    global start_time, selected_sentence
    selected_sentence = random.choice(sentences)
    start_time = time.time()
    sentence_label.config(text=selected_sentence)
    input_box.delete(0, tk.END)
    input_box.config(state=tk.NORMAL)
    input_box.focus()
    result_label.config(text="")

def check_result():
    """Check typing speed and accuracy."""
    global start_time, selected_sentence
    if not start_time:
        messagebox.showerror("Error", "Click 'Start' to begin the game!")
        return

    end_time = time.time()
    time_taken = end_time - start_time

    user_input = input_box.get()
    input_box.config(state=tk.DISABLED)

    # Calculate Words Per Minute (WPM)
    word_count = len(selected_sentence.split())
    wpm = (word_count / (time_taken / 60))

    # Calculate Accuracy
    correct_chars = sum(1 for a, b in zip(user_input, selected_sentence) if a == b)
    accuracy = (correct_chars / len(selected_sentence)) * 100

    # Display Results
    result_label.config(
        text=(
            f"Time Taken: {time_taken:.2f} seconds\n"
            f"Words Per Minute (WPM): {wpm:.2f}\n"
            f"Accuracy: {accuracy:.2f}%"
        )
    )

def reset_game():
    """Reset the game for a new round."""
    global start_time, selected_sentence
    start_time = 0
    selected_sentence = ""
    sentence_label.config(text="Click 'Start' to begin.")
    input_box.delete(0, tk.END)
    input_box.config(state=tk.DISABLED)
    result_label.config(text="")

# UI Setup
root = tk.Tk()
root.title("Typing Speed Tester")
root.geometry("600x400")
root.resizable(False, False)

# Fonts and colors
font_title = ("Helvetica", 16, "bold")
font_normal = ("Helvetica", 14)
bg_color = "#f5f5f5"

root.configure(bg=bg_color)

# Title Label
title_label = tk.Label(root, text="Typing Speed Tester", font=font_title, bg=bg_color)
title_label.pack(pady=10)

# Sentence Label
sentence_label = tk.Label(
    root, text="Click 'Start' to begin.", font=font_normal, wraplength=500, bg=bg_color
)
sentence_label.pack(pady=20)

# Input Box
input_box = tk.Entry(root, font=font_normal, width=50, state=tk.DISABLED)
input_box.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", font=font_normal, command=start_game)
start_button.grid(row=0, column=0, padx=10)

check_button = tk.Button(button_frame, text="Submit", font=font_normal, command=check_result)
check_button.grid(row=0, column=1, padx=10)

reset_button = tk.Button(button_frame, text="Reset", font=font_normal, command=reset_game)
reset_button.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=font_normal, bg=bg_color)
result_label.pack(pady=20)

# Run the application
root.mainloop()
