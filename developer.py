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

class Developer:
    def __init__(self,root):
        pass
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman",35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"Images\dev_person.jpg")
        img_top = img_top.resize((1530,720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530, height=720) 

        # Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, height=400, width=500)


        # Developer Information
        dev_label = Label(main_frame, text = "This Project is developed by: ", font=("times new roman", 30, "bold"), fg="red", bg="white")
        dev_label.place(x=0, y=5)
        dev_label = Label(main_frame, text = "Name : Vishal Chauhan", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        dev_label.place(x=0, y=60)
        dev_label = Label(main_frame, text = "Enrollment No. 0108CS171123", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        dev_label.place(x=0, y=100)
        dev_label = Label(main_frame, text = "Name : Utkarsh Talreja", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.place(x=0, y=140)
        dev_label = Label(main_frame, text = "Enrollment No. 0108CS171116", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.place(x=0, y=180)
        dev_label = Label(main_frame, text = "Name : Damodar Dhakad", font=("times new roman", 20, "bold"), fg="brown", bg="white")
        dev_label.place(x=0, y=220)
        dev_label = Label(main_frame, text = "Enrollment No. 0108CS183D04", font=("times new roman", 20, "bold"), fg="brown", bg="white")
        dev_label.place(x=0, y=260)
        dev_label = Label(main_frame, text = "Project Guide: Prof. Satish Pawar", font=("times new roman", 25, "bold"), fg="red", bg="white")
        dev_label.place(x=0, y=350)





if __name__ == "__main__":
     root = Tk()
     obj = Developer(root)
     root.mainloop()