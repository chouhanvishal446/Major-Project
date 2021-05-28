from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student_class:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ======== Variables =====================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_rollno = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()


        #first Image
        img = Image.open(r"C:\Users\Vishal\Desktop\FR Project\Images\smart-attendance.jpg")
        img = img.resize((500,130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=0,y=0,width=500, height=130)

        #Second Image
        img1 = Image.open(r"C:\Users\Vishal\Desktop\FR Project\Images\facialrecognition.png")
        img1 = img1.resize((500,130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=500,y=0,width=500, height=130)

        #Third Image
        img2 = Image.open(r"C:\Users\Vishal\Desktop\FR Project\Images\student.jpg")
        img2 = img2.resize((500,130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550, height=130)

        #Background Image
        img3 = Image.open(r"C:\Users\Vishal\Desktop\FR Project\Images\clg.jpg")
        img3 = img3.resize((1573,710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530, height=710)

        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman",35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, height=600, width=1500)

        #Left Frame
        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Users\Vishal\Desktop\FR Project\Images\facialrecognition.png")
        img_left = img_left.resize((720,130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_Frame, image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720, height=130)

        #Current Course
        Current_course_frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        Current_course_frame.place(x=5, y=135, width=720, height=150)

        #Department
        dep_label = Label(Current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(Current_course_frame, textvariable = self.var_dep, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "CSE", "EC", "Electrical", "Mechanical", "Civil", "BME", "Petrochemical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Course
        course_label = Label(Current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(Current_course_frame, textvariable = self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "BE", "B.Tech", "ME", "M.Tech", "MBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Year
        year_label = Label(Current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(Current_course_frame, textvariable = self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "First Year", "Second Year", "Third Year", "Final Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Semester
        Semester_label = Label(Current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(Current_course_frame, textvariable = self.var_sem, font=("times new roman", 13, "bold"), state="readonly", width=20)
        Semester_combo["values"] = ("Select", "First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

       #Class Student Information
        Class_Student_frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        Class_Student_frame.place(x=5, y=250, width=720, height=300)

        #StudentID
        StudentID_label = Label(Class_Student_frame, text="StudentID:", font=("times new roman", 13, "bold"), bg="white")
        StudentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(Class_Student_frame, textvariable = self.var_id, font=("times new roman", 13, "bold"), width=20)
        StudentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #Student Name
        Student_Name_label = Label(Class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        Student_Name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Student_Name_entry = ttk.Entry(Class_Student_frame, textvariable = self.var_name, font=("times new roman", 13, "bold"), width=20)
        Student_Name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #Class Devision
        Class_Devision_label = Label(Class_Student_frame, text="Class Devision:", font=("times new roman", 13, "bold"), bg="white")
        Class_Devision_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Class_Devision_entry = ttk.Entry(Class_Student_frame, textvariable = self.var_div, font=("times new roman", 13, "bold"), width=20)
        Class_Devision_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #Roll No
        Roll_No_label = Label(Class_Student_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        Roll_No_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_No_entry = ttk.Entry(Class_Student_frame, textvariable = self.var_rollno, font=("times new roman", 13, "bold"), width=20)
        Roll_No_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #Phone Number
        Phone_No_label = Label(Class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        Phone_No_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        Phone_No_entry = ttk.Entry(Class_Student_frame, textvariable = self.var_phone, font=("times new roman", 13, "bold"), width=20)
        Phone_No_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #Email ID
        Email_ID_label = Label(Class_Student_frame, text="Email ID:", font=("times new roman", 13, "bold"), bg="white")
        Email_ID_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        Email_ID_entry = ttk.Entry(Class_Student_frame, textvariable = self.var_email, font=("times new roman", 13, "bold"), width=20)
        Email_ID_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Class_Student_frame,variable = self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(Class_Student_frame,variable = self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        #Button Frame
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame, command = self.add_data, text="Save", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=17, command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=17, command=self.delete_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, command = self.generate_dataset, text="Take Photo Sample", width=35,  font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35,  font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)
       
       
       
       
    
       
       
        #Right Frame
        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_Frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"C:\Users\Vishal\Desktop\FR Project\Images\facialrecognition.png")
        img_right = img_right.resize((720,130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_Frame, image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720, height=130)

        # # Search System
        # Search_Frame = LabelFrame(Right_Frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        # Search_Frame.place(x=5, y=135, width=710, height=70)

        # Search_label = Label(Search_Frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        # Search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # Search_combo = ttk.Combobox(Search_Frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        # Search_combo["values"] = ("Select", "Roll No.", "Phone No.")
        # Search_combo.current(0)
        # Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Search_entry = ttk.Entry(Search_Frame, font=("times new roman", 13, "bold"), width=15)
        # Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # search_btn = Button(Search_Frame, text="Search", width=12, command= self.search_data, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        # search_btn.grid(row=0, column=3, padx=4)

        # showall_btn = Button(Search_Frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        # showall_btn.grid(row=0, column=4, padx=4)

        # ================= Table Frame ==============================
        Table_Frame = LabelFrame(Right_Frame, bd=2, bg="white")
        Table_Frame.place(x=5, y=135, width=710, height=400)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_Frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "phone", "email", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("photo", width=100)


        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    # ========== Function Declaration ===============
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Zandubalm@987", database="face-recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                (self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_sem.get(),
                                self.var_id.get(),
                                self.var_name.get(),
                                self.var_div.get(),
                                self.var_rollno.get(),
                                self.var_phone.get(),
                                self.var_email.get(),
                                self.var_radio1.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details added Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # =========== Fetch Data =====================================================================================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Zandubalm@987", database="face-recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

            conn.commit()
        conn.close()

    # ===================== get cursor ====================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_email.set(data[9]),
        self.var_radio1.set(data[10])


    # def search_data(self):
    #     if self.serchTxt_var.get()=="" or self.serch_var.get()=="Select Option":
    #         messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
    #     else:
    #         try:
    #             conn=mysql.connector.connect(host='localhost',username='root',password='Zandubalm@987',database='face-recognition')
    #             my_cursor=conn.cursor()
    #             my_cursor.execute("select * from student where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
    #             rows=my_cursor.fetchall()         
    #             if len(rows)!=0:
    #                 self.student_table.delete(*self.student_table.get_children())
    #                 for i in rows:
    #                     self.student_table.insert("",END,values=i)
    #                 if rows==None:
    #                     messagebox.showerror("Error","Data Not Found",parent=self.root)
    #                     conn.commit()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # # Update Function

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Zandubalm@987", database="face-recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Phone=%s, Email=%s, Photo=%s where Student_id=%s",
                                            (
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_sem.get(),
                                                self.var_name.get(),
                                                self.var_div.get(),
                                                self.var_rollno.get(),
                                                self.var_phone.get(),
                                                self.var_email.get(),
                                                self.var_radio1.get(),
                                                self.var_id.get()
                                            ))

                else:
                    if not update:
                        return

                messagebox.showinfo("Success","Student details successfully updated")
                conn.commit()
                self.fetch_data()
                conn.close()   

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)    




    # ========== Delete Data ======================================================
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student delete page", "Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Zandubalm@987", database="face-recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()   
                messagebox.showinfo("Success", "Student data successfully deleted", parent=self.root)
                

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    #================ Reset Button ===============================================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_rollno.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_radio1.set("")

    # ================= Generate Dataset or Take Photos ============

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Zandubalm@987", database="face-recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Phone=%s, Email=%s, Photo=%s where Student_id=%s",
                                                (
                                                    self.var_dep.get(),
                                                    self.var_course.get(),
                                                    self.var_year.get(),
                                                    self.var_sem.get(),
                                                    self.var_name.get(),
                                                    self.var_div.get(),
                                                    self.var_rollno.get(),
                                                    self.var_phone.get(),
                                                    self.var_email.get(),
                                                    self.var_radio1.get(),
                                                    self.var_id.get() == id+1
                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                    # ========= Load harcascade classifier ===========================================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scaling factor = 1.3
                        # minimum neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                capture = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = capture.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1

                        face = cv2.resize(face_cropped(my_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)
                        file_name_path = "data/user." +str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed")

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


        

if __name__ == "__main__":
     root = Tk()
     obj = Student_class(root)
     root.mainloop()
