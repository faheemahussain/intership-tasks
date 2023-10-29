

import tkinter as tk


# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the input and results
entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Define buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons on the GUI
row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 20),
              command=lambda b=button: on_button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

def on_button_click(button):
    if button == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button)

root.mainloop()
