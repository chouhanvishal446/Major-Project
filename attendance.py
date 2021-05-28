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

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ===== Variables =============================
        self.var_att_id = StringVar()
        self.var_att_roll = StringVar()
        self.var_att_name = StringVar()
        self.var_att_dep = StringVar()
        self.var_att_time = StringVar()
        self.var_att_date = StringVar()
        self.var_att_attendance = StringVar()

        #first Image
        img = Image.open(r"Images\smart-attendance.jpg")
        img = img.resize((800,200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=0,y=0,width=800, height=200)

        #Second Image
        img1 = Image.open(r"Images\student.jpg")
        img1 = img1.resize((800,200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=800,y=0,width=800, height=200)

        #Background Image
        img3 = Image.open(r"Images\att.png")
        img3 = img3.resize((1573,710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x=0,y=200,width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, height=600, width=1500)

        #Left Frame
        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"Images\facialrecognition.png")
        img_left = img_left.resize((720,130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_Frame, image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720, height=130)

        left_inside_frame = Frame(Left_Frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, height=370, width=720)

        # Label and Entry

        #Attendance ID
        attendanceID_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_att_id, font=("times new roman", 13, "bold"), width=20)
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=4, pady=8)

        roll_entry = ttk.Entry(left_inside_frame, textvariable=self.var_att_roll, font=("times new roman", 13, "bold"), width=22)
        roll_entry.grid(row=0, column=3, pady=8)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        name_label.grid(row=1, column=0)

        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_att_name, font=("times new roman", 13, "bold"), width=22)
        name_entry.grid(row=1, column=1, pady=8)

        # Department
        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=1, column=2)

        dep_entry = ttk.Entry(left_inside_frame, textvariable=self.var_att_dep, font=("times new roman", 13, "bold"), width=22)
        dep_entry.grid(row=1, column=3, pady=8)

        # time
        dep_label = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=2, column=0)

        dep_entry = ttk.Entry(left_inside_frame, textvariable=self.var_att_time, font=("times new roman", 13, "bold"), width=22)
        dep_entry.grid(row=2, column=1, pady=8)

        # date
        dep_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=2, column=2)

        dep_entry = ttk.Entry(left_inside_frame, textvariable=self.var_att_date, font=("times new roman", 13, "bold"), width=22)
        dep_entry.grid(row=2, column=3, pady=8)

        # attendance
        dep_label = Label(left_inside_frame, text="Attendance:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=3, column=0)

        self.att_status = ttk.Combobox(left_inside_frame, textvariable=self.var_att_attendance, font=("times new roman", 13, "bold"), state="readonly", width=20)
        self.att_status["values"] = ("Status", "Present", "Absent")
        self.att_status.current(0)
        self.att_status.grid(row=3, column=1, pady=8)

        #Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        import_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export", command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=17, command=self.action, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)



        #Right Frame
        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_Frame.place(x=750, y=10, width=720, height=580)

        # img_right = Image.open(r"Images\facialrecognition.png")
        # img_right = img_right.resize((720,130), Image.ANTIALIAS)
        # self.photoimg_right = ImageTk.PhotoImage(img_right)

        # f_lbl = Label(Right_Frame, image = self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=720, height=130)

        table_frame = Frame(Right_Frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455) 

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column = ("ID", "Roll", "Name", "Department", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID", text="AttendanceID")
        self.AttendanceReportTable.heading("Roll", text="Roll No")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        

        self.AttendanceReportTable.column("ID", width=100)
        self.AttendanceReportTable.column("Roll", width=100)
        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Department", width=100)
        self.AttendanceReportTable.column("Time", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("Attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)




    # ================== fetch data ================
    def fetchdata(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # Import csv
    def importCsv(self):
        global mydata
        mydata=[]
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Open CSV", filetypes = (("CSV File", "*.csv"),("ALL File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
                self.fetchdata(mydata)


    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data Found to Export", parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV File", "*.csv"),("ALL File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)

                messagebox.showinfo("Data Export", "Your data exported to"+os.path.basename(fln)+"successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_att_id.set(rows[0])
        self.var_att_roll.set(rows[1])
        self.var_att_name.set(rows[2])
        self.var_att_dep.set(rows[3])
        self.var_att_time.set(rows[4])
        self.var_att_date.set(rows[5])
        self.var_att_attendance.set(rows[6])


    def reset_data(self):
        self.var_att_id.set("")
        self.var_att_roll.set("")
        self.var_att_name.set("")
        self.var_att_dep.set("")
        self.var_att_time.set("")
        self.var_att_date.set("")
        self.var_att_attendance.set("")


    def action(self):
        id=self.var_att_id.get()
        roll=self.var_att_roll.get()
        name=self.var_att_name.get()
        dep=self.var_att_dep.get()
        time=self.var_att_time.get()
        date=self.var_att_date.get()
        attendn=self.var_att_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        







if __name__ == "__main__":
     root = Tk()
     obj = Attendance(root)
     root.mainloop()