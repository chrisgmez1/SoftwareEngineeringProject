import tkinter as tk
from tkinter import *

def main_screen():
    screen = tk.Tk()
    screen.title("Learning Managment System")
    screen.geometry("300x250")
    Label(text = "Login",bg = "grey", height ="2", width="250").pack()
    adminLog = tk.Button(screen, text = "Admin Login", padx = 10, pady = 5
                                        ,fg="black")
    adminLog.pack()

    userLog = tk.Button(screen, text = "User Login", padx = 10, pady = 5
                                        ,fg="black")
    userLog.pack()

    screen.mainloop()

main_screen()