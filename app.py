import tkinter as tk
from tkinter import *



def admin_view():
    admin_screen = tk.Tk()
    admin_screen.title("Admin View")
    admin_screen.geometry("750x600")
    Label(admin_screen,text = "Admin",bg = "red", height ="2", width="750").pack()
    canvas_adminview = tk.Canvas(admin_screen,bg="grey",width ="650",height="500")
    canvas_adminview.pack()

    insertRecords = tk.Button(admin_screen, text = "Insert Records", padx = 10, pady = 5
                                        ,fg="black")
    insertRecords.pack()

    deleteRecords = tk.Button(admin_screen, text = "Delete Records", padx = 10, pady = 5
                                        ,fg="black")
    deleteRecords.pack()

    modifyRecords = tk.Button(admin_screen, text = "Modify Records", padx = 10, pady = 5
                                        ,fg="black")
    modifyRecords.pack()

    admin_screen.mainloop()
def user_view():
    user_screen = tk.Tk()
    user_screen.title("Admin View")
    user_screen.geometry("750x600")
    Label(user_screen,text = "User",bg = "blue", height ="2", width="750").pack()
    canvas_userview = tk.Canvas(user_screen,bg="grey",width ="650",height="500")
    canvas_userview.pack()

    userLog = tk.Button(user_screen, text = "Change Grades", padx = 10, pady = 5
                                        ,fg="black")
    userLog.pack()

    user_screen.mainloop()
def main_screen():
    screen = tk.Tk()
    screen.title("Learning Managment System")
    screen.geometry("300x250")
    Label(text = "Login",bg = "grey", height ="2", width="250").pack()
    
    adminLog = tk.Button(screen, text = "Admin Login", padx = 10, pady = 5
                                        ,fg="black", command =admin_view)
    adminLog.pack()

    userLog = tk.Button(screen, text = "User Login", padx = 10, pady = 5
                                        ,fg="black", command= user_view)
    userLog.pack()

    screen.mainloop()

main_screen()