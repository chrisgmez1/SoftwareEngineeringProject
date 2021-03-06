import tkinter as tk
from tkinter import *
import json

def insert_verify():
    
    records = {"username":username1.get(),"studentFirst":firstName.get(),"studentLast":lastName.get(),
    "studentID":studentID.get(),"studentCourses":[],"studentExamScores":[],"studentPhoneNum":phoneNum.get(),"studentAddress":address.get()}
    j = json.dumps(records)
    with open('studentinfo.json','r') as f:
        data=json.load(f)
        f.close()
    data["users"].append(records)
    with open('studentinfo.json','w') as jfile:
        json.dump(data,jfile, indent = 6)
        jfile.close
    screen1.destroy()
    username_entry.delete(0, END)
    firstName_entry.delete(0, END)
    lastName_entry.delete(0, END)
    studentID_entry.delete(0, END)
    phoneNum_entry.delete(0, END)
    address_entry.delete(0, END)

def insert_records():
    global screen1 
    screen1 = tk.Toplevel()
    global username1
    global firstName
    global lastName
    global studentID
    global phoneNum
    global address

    username1 = StringVar()
    firstName = StringVar()
    lastName = StringVar()
    studentID = StringVar()
    phoneNum = StringVar()
    address = StringVar()

    global username_entry
    global firstName_entry 
    global lastName_entry 
    global studentID_entry
    global phoneNum_entry
    global address_entry

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text =  "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username1)
    username_entry.pack()
    Label(screen1,text = "First Name * ").pack()
    firstName_entry = Entry(screen1, textvariable = firstName)
    firstName_entry.pack()
    Label(screen1,text = "Last Name * ").pack()
    lastName_entry = Entry(screen1, textvariable = lastName)
    lastName_entry.pack()
    Label(screen1,text = "StudentID * ").pack()
    studentID_entry = Entry(screen1, textvariable = studentID)
    studentID_entry.pack()
    Label(screen1,text = "Phone Number * ").pack()
    phoneNum_entry = Entry(screen1, textvariable = phoneNum)
    phoneNum_entry.pack()
    Label(screen1,text = "Address * ").pack()
    address_entry = Entry(screen1, textvariable = address)
    address_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1,command=insert_verify).pack()
    

def delete_info():
    obj  = json.load(open("studentinfo.json"))
                          
    for i in range(0,len(obj["users"])):
        if obj["users"][i]["username"] == username2.get():
            obj["users"].pop(i)
            break
                                
    open("studentinfo.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))

    screen2.destroy()
def delete_records():
    global username2
    global screen2 
    screen2 = tk.Toplevel()
    username2 = StringVar()

    Label(screen2, text = "Enter the user whose record you wish to delete").pack()
    Label(screen2, text =  "Username * ").pack()
    username_entry = Entry(screen2, textvariable = username2)
    username_entry.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Enter", width = 10, height = 1,command=delete_info).pack()
def modify_grades():
    screen = tk.Toplevel()
    global exam1 
    global exam2 
    global exam3 
    global exam4 
    global exam5 
    exam1 = StringVar() 
    exam2 = StringVar() 
    exam3 = StringVar() 
    exam4 = StringVar() 
    exam5 = StringVar() 

    Label(screen, text =  "Exam 1 * ").pack()
    exam1_entry = Entry(screen, textvariable = exam1)
    exam1_entry.pack()
    Label(screen, text =  "Exam 2 * ").pack()
    exam2_entry = Entry(screen, textvariable = exam2)
    exam2_entry.pack()
    Label(screen, text =  "Exam 3 * ").pack()
    exam3_entry = Entry(screen, textvariable = exam3)
    exam3_entry.pack()
    Label(screen, text =  "Exam 4 * ").pack()
    exam4_entry = Entry(screen, textvariable = exam4)
    exam4_entry.pack()
    Label(screen, text =  "Exam 5 * ").pack()
    exam5_entry = Entry(screen, textvariable = exam5)
    exam5_entry.pack()
    enter_button = tk.Button(screen, text = "Enter", padx = 10, pady = 5
                                        ,fg="black",command=modify_info)
    enter_button.pack()
def modify_courses():
    screen = tk.Toplevel()
    global exam1 
    global exam2 
    global exam3 
    global exam4 
    global exam5 
    exam1 = StringVar() 
    exam2 = StringVar() 
    exam3 = StringVar() 
    exam4 = StringVar() 
    exam5 = StringVar() 

    Label(screen, text =  "Exam 1 * ").pack()
    exam1_entry = Entry(screen, textvariable = exam1)
    exam1_entry.pack()
    Label(screen, text =  "Exam 2 * ").pack()
    exam2_entry = Entry(screen, textvariable = exam2)
    exam2_entry.pack()
    Label(screen, text =  "Exam 3 * ").pack()
    exam3_entry = Entry(screen, textvariable = exam3)
    exam3_entry.pack()
    Label(screen, text =  "Exam 4 * ").pack()
    exam4_entry = Entry(screen, textvariable = exam4)
    exam4_entry.pack()
    Label(screen, text =  "Exam 5 * ").pack()
    exam5_entry = Entry(screen, textvariable = exam5)
    exam5_entry.pack()
    enter_button = tk.Button(screen, text = "Enter", padx = 10, pady = 5
                                        ,fg="black",command=modify_info_courses)
    enter_button.pack()
def modify_choice():
    screen = tk.Toplevel()
    modifyGrades = tk.Button(screen, text = "Modify Grades", padx = 10, pady = 5
                                        ,fg="black",command=modify_grades)
    modifyGrades.pack()

    modifyCourses = tk.Button(screen, text = "Modify Courses", padx = 10, pady = 5
                                        ,fg="black",command=modify_courses)
    modifyCourses.pack()

    screen.destroy()
def modify_info():
    grades = [int(exam1.get()),int(exam2.get()),int(exam3.get()),int(exam4.get()),int(exam5.get())]
    obj  = json.load(open("studentinfo.json"))
                          
    for i in range(0,len(obj["users"])):
        if obj["users"][i]["username"] == username3.get():
            obj["users"][i]["studentExamScores"] = grades 
            break
                                
    open("studentinfo.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))
    screen3.destroy()
def modify_info_courses():
    courses = [(exam1.get()),(exam2.get()),(exam3.get()),(exam4.get()),(exam5.get())]
    obj  = json.load(open("studentinfo.json"))
                          
    for i in range(0,len(obj["users"])):
        if obj["users"][i]["username"] == username3.get():
            obj["users"][i]["studentCourses"] = courses 
            break
                                
    open("studentinfo.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))
    screen3.destroy()
def modify_records():
    global username3
    global screen3
    screen3 = tk.Toplevel()
    username3 = StringVar()

    Label(screen3, text = "Enter the user whose record you wish to modify").pack()
    Label(screen3, text =  "Username * ").pack()
    username_entry = Entry(screen3, textvariable = username3)
    username_entry.pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Register", width = 10, height = 1,command=modify_choice).pack()

def admin_view():
    admin_screen = tk.Toplevel()
    admin_screen.title("Admin View")
    admin_screen.geometry("750x600")
    Label(admin_screen,text = "Admin",bg = "red", height ="2", width="750").pack()

    insertRecords = tk.Button(admin_screen, text = "Insert Records", padx = 10, pady = 5
                                        ,fg="black",command=insert_records)
    insertRecords.pack()

    deleteRecords = tk.Button(admin_screen, text = "Delete Records", padx = 10, pady = 5
                                        ,fg="black",command=delete_records)
    deleteRecords.pack()

    modifyRecords = tk.Button(admin_screen, text = "Modify Records", padx = 10, pady = 5
                                        ,fg="black",command=modify_records)
    modifyRecords.pack()

    admin_screen.mainloop()
def view_grades(username,screen):
    labelframe1=LabelFrame(screen,text="Courses")
    labelframe1.pack(side=LEFT)
    labelframe2=LabelFrame(screen,text="Grades")
    labelframe2.pack(side=LEFT)
    
    with open('studentinfo.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    for i in data["users"]:
        if i["username"]==username: 
            for j in range(0,len(i["studentCourses"])):
                Label(labelframe1,text = (i["studentCourses"][j]),bg = "gray", height ="2", width="8").pack(side = TOP)

            for j in range(0,len(i["studentCourses"])):
                Label(labelframe2,text = str(i["studentExamScores"][j]),bg = "gray", height ="2", width="8").pack(side = TOP)

            Label(screen,text = "Student First: "+i["studentFirst"],bg = "light gray").pack(side = TOP)
            Label(screen,height="1").pack()
            Label(screen,text = "Student Last: "+i["studentLast"],bg = "light gray").pack(side = TOP)
            Label(screen,height="1").pack()

            Label(screen,text = "Student Phone: "+i["studentPhoneNum"],bg = "light gray").pack(side = TOP)
            Label(screen,height="1").pack()

            Label(screen,text = "Student ID: " +i["studentID"],bg = "light gray").pack(side = TOP)
            Label(screen,height="1").pack()

            Label(screen,text = "Student Address: "+i["studentAddress"],bg = "light gray").pack(side = TOP)
        
def user_view(user):
    user_screen = tk.Toplevel()
    user_screen.title("User View")
    user_screen.geometry("400x300")
    Label(user_screen,text = user,bg = "green", height ="2", width="300").pack()

    view_grades(user,user_screen)

    user_screen.mainloop()
