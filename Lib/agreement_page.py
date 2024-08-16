# agreement_page.py
"""
August 16, 2024
@Author: Shivam Shukla
@Description: This package facilitates the execution or invocation of the application

This code is provided solely for educational purposes.
As the developer, I explicitly disclaim any responsibility for any unexpected or adverse effects on your system resulting from its use.
While I encourage learning and experimentation, I recommend exercising caution and using this code wisely.
Ultimately, you, the user, are entirely responsible for how you utilize this code in any scenario or context.

The code is unencumbered by copyright; feel free to share, modify, or adapt it as you see fit.
"""

from os.path import abspath
from os.path import dirname
import tkinter as tk
from tkinter import messagebox

def on_accept():
    messagebox.showinfo("Accepted", "You have accepted the license agreement.")
    root.destroy()
    quit(0)

def on_decline():
    messagebox.showinfo("Declined", "You have declined the license agreement.")
    root.destroy()
    quit(1)

print(dirname(abspath(__file__)))

root = tk.Tk()
root.title("License Agreement")
root.geometry("650x500")
root.resizable(False, False)

text_frame = tk.Frame(root)
text_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

license_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)


with open('LICENSE', 'r') as file:
    content = file.read()

license_text.insert(tk.END, content)
license_text.config(state=tk.DISABLED)
license_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

scrollbar.config(command=license_text.yview)

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10, anchor='se')

accept_button = tk.Button(button_frame, text="Accept", command=on_accept)
accept_button.pack(side=tk.LEFT, padx=5)

decline_button = tk.Button(button_frame, text="Decline", command=on_decline)
decline_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
