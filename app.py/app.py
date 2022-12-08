import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

def addApp():
     filename = filedialog.askopenfilename(initialdir="/", title="Select File",
     filetypes=(("excutables","*.exe"),("all files", "*.*")))

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openfile = tk.Button(root, text="open file", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openfile.pack()
runApps =  tk.Button(root, text="Runapps", padx=10, pady=5, fg="white", bg="black")

root.mainloop();