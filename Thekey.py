from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import scrolledtext

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import tkinter
import tkinter.filedialog
import base64
from tkinter.ttk import *
import webbrowser





key = Tk()
key.title("The key")
cesar_key = "Your Key"
key_canvas = Canvas(key, width=320, height=80)
key_text = Text(key, height=1, width=30)
key_text.insert(INSERT, cesar_key)
key_canvas.create_window(150, 20, window=key_text)
button_key = Button(key, text='   Enter  ', command=key_text.get("1.0", END))
key_canvas.create_window(200, 60, window=button_key)
button_key1 = Button(key, text='   Annuler  ', command=key_text.get("1.0", END))
key_canvas.create_window(100, 60, window=button_key1)



thekey1 = key_text.get("1.0", END)
print(thekey1)


key_canvas.pack()

