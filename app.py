import tkinter as tk
from tkinter import *
import json

def admin_view():
    admin_screen = tk.Tk()
    admin_screen.title("Admin View")
    admin_screen.geometry("750x600")
    Label(admin_screen,text = "Admin",bg = "red", height ="2", width="750").pack()

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
def view_grades(username,screen):
    with open('studentinfo.json') as json_file:
        data = json.load(json_file)
        for i in data["users"]:
            if i["username"]==username: 
                canv = tk.Canvas(screen, bg='yellow', width=250, height=250)
                canv.pack()

        
def user_view(user):
    user_screen = tk.Tk()
    user_screen.title("User View")
    user_screen.geometry("750x600")
    Label(user_screen,text = "User",bg = "green", height ="2", width="750").pack()

    userLog = tk.Button(user_screen, text = "View Grades", padx = 10, pady = 5
                                        ,fg="black",command=view_grades(user,user_screen))
    userLog.pack()

    user_screen.mainloop()
