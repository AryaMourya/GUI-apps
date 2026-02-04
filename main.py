import tkinter as tk
from tkinter import messagebox,filedialog

from matplotlib import text

main = tk.Tk()
main.title("Simple Text Editor")
main.geometry("600x400")

text_area = tk.Text(
    main,
    wrap=tk.WORD,
    font=("Arial", 12))

text_area.pack(expand=True, fill=tk.BOTH)

def new_file():
    text_area.delete(1.0, tk.END)

main.mainloop()