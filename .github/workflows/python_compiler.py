import tkinter as tk
import tkinter as ttk
from tkinter import scrolledtext
import subprocess

def run_code():
    code = editor.get(1.0, tk.END)
    try:
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, universal_newlines=True)
        output.delete(1.0, tk.END)
        output.insert(tk.END, result)
    except subprocess.CalledProcessError as e:
        output.delete(1.0, tk.END)
        output.insert(tk.END, e.output)

# Create the main window
window = tk.Tk()
overview_label = tk.Label(window, text="Welcome to the Python Compiler!\n\nThis is a simple compiler that can be used to compile and run Python code.\n\nHappy coding!")
overview_label.pack(side="top", fill="both", expand=True)

window.title("Simple Python Compiler")

# Create an editor
editor = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
editor.pack()

# Create a "Run" button
run_button = tk.Button(window, text="Run", command=run_code)
run_button.pack()

# Create an output console
output = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
output.pack()

# Start the GUI loop
window.mainloop()