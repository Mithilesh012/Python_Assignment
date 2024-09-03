import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to speech")
root.geometry("900*450")
root.resizable(False,False)

#icon
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,image_icon)

root.mainloop()
