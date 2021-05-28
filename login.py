from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from time import strftime
import cv2
import os
import csv
import numpy as np
from tkinter import filedialog

class login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")

        self.bg = ImageTk.PhotoImage(file =(r"Images\login.png"))
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)






if __name__ == "__main__":
     root = Tk()
     obj = login_window(root)
     root.mainloop()