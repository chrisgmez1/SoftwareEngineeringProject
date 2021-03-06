from tkinter import *
import os

from record_funcs import admin_view,user_view
def delete2():  
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
    
def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Sucess")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Sucess!").pack()
    Button(screen3, text = "OK", command = delete2).pack()

def password_not_regconized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Sucess")
    screen4.geometry("150x100")
    Label(screen4, text = "Password Error").pack()
    Button(screen4, text = "OK", command = delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Sucess")
    screen5.geometry("150x100")
    Label(screen5, text = "User not found").pack()
    Button(screen5, text = "OK", command = delete4).pack()
    
def register_user():
    username_info = username.get()
    password_info = password.get()
    filepath = "usercredentials\\"
    file=open(filepath + username_info, "w")
    file.write(username_info+ "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Sucess!", fg = "blue", font = ("Calibri", 11)).pack()

def password_not_recognized():
    print("Password not recognized")

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    if username1 == "admin" and password1 == "password":
        admin_view()
    else:    
        list_of_files = os.listdir("usercredentials")
        if username1 in list_of_files:
            file1 = open("usercredentials\\" + username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                user_view(username1)
            else:
                password_not_recognized()
        else:
                user_not_found()


    
def register():

    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("600x500")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text =  "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1,text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command =  register_user).pack()
    
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("600x500")

    Label(screen2, text = "Please enter details below to login").pack()
    

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = StringVar()
    password_verify  = StringVar()
    
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    
    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x500")
    screen.title("UHD Blackboard 2.0")
    Label(text = "UHD Blackboard 2.0", bg = "dark blue", width = "300", height = "2", font = ("Calibri", 30 ), fg = "red").pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text =  "Register", height = "2", width = "30", command = register).pack()

    screen.mainloop()

main_screen()
