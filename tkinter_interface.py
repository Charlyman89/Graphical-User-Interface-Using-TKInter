# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import sqlite3
from tkinter import messagebox


with sqlite3.connect("Registration.db") as db:
    # access to database or query db
    cursor = db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS myusers (id integer PRIMARY KEY AUTOINCREMENT, \
               username text NOT NULL, password text NOT NULL);""")
    

def add_new_user():
    # collect inputs
    newUsername = username.get()
    newPassword = password.get()
    
    cursor.execute("SELECT COUNT(*) FROM myusers WHERE username = '"+ newUsername + "' ")
    
    # result is vaed here
    result = cursor.fetchone()
    
    if newUsername=="" and newPassword=="":
        messagebox.showinfo("", "Blank not allowed")    
    elif len(newPassword) < 6:
        messagebox.showinfo("", "Password too short!")
    elif int(result[0]) > 0:
        messagebox.showinfo("", "Username already exists")
    else: 
        success["text"] = "Added New User"
        cursor.execute("INSERT INTO myusers(username, password) VALUES(?,?)", \
                       (newUsername, newPassword))
    db.commit()
    

def display_info():
    cursor.execute("SELECT * FROM myusers")
    for x in cursor.fetchall():
        listbox1.insert(tk.END, x)
    
def clear():
    listbox1.delete(0, tk.END)

window = tk.Tk()
window.title("Registration Page")
window.geometry("600x300")

success = tk.Message(text="", fg='red', width=160)
success.place(x=30, y=10)


label1 = tk.Label(text="Enter Username")
label1.place(x=25, y=30)

username = tk.Entry(text=" ")
username.place(x = 160, y = 30, width=250, height=30)
username.bind("<Button-1>", lambda event: username.delete(0, tk.END))


label2 = tk.Label(text="Enter password")
label2.place(x=25, y=60)

password = tk.Entry(text="")
password.place(x=160, y=60, width=250, height=30)
password.bind("<Button-1>", lambda event: password.delete(0, tk.END))


save = tk.Button(window, text="Save", command=add_new_user)
save.place(x=160, y=100, width=80, height=30)

clear_1 = tk.Button(text="Clear", command=clear)
clear_1.place(x=270, y=100, width=80, height=30)


label3 = tk.Label(text="Display all usernames and passwords in the database")
label3.place(x=150, y=131)


display = tk.Button(window, text="Display", command=display_info)
display.place(x=30, y=180, width=100, height=30)


listbox1 = tk.Listbox()
listbox1.place(x = 150, y = 160, width=300, height=100)

window.mainloop()