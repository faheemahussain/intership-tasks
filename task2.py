import random
import string
import tkinter as tk

root = tk.Tk()
root.title("Random Password Generator")

# Label for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

# Entry widget for password length
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for character types
use_letters = tk.IntVar()
use_numbers = tk.IntVar()
use_special = tk.IntVar()

tk.Checkbutton(root, text="Include Letters", variable=use_letters).pack()
tk.Checkbutton(root, text="Include Numbers", variable=use_numbers).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=use_special).pack()

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Display generated password
password_label = tk.Label(root, text="")
password_label.pack()

def generate_password():
    password_length = int(length_entry.get())
    characters = ""

    if use_letters.get():
        characters += string.ascii_letters
    if use_numbers.get():
        characters += string.digits
    if use_special.get():
        characters += string.punctuation

    if characters:
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        password_label.config(text=generated_password)
    else:
        password_label.config(text="Please select at least one character type.")

root.mainloop()
