import os
import glob
import tkinter as tk
from tkinter import Label, Entry, Button, Toplevel
import subprocess
from Test import getMail
from file_utils import read_csv, write_csv, read_file, write_file
from generate import _render_template, preprocess


# getMail()
global root, root1

root = tk.Tk()
root.geometry('300x300')


data = read_csv()
participants = data
participants = preprocess(participants)




def destroyRoot():
    root.destroy()


def getData():
    emailid = emailentry.get()
    with open('credentials/email.txt', 'w') as emailFile:
        emailFile.write(emailid)

    password_file = passwordentry.get()
    with open('credentials/password.txt', 'w') as passFile:
        passFile.write(password_file)
    validate(emailid, password_file)


def validate(email, password):
    if email == '' and password == '':
        invalid()
    elif email == '':
        invalid()
    elif password == '':
        invalid()
    else:
        display_screen()


def destroyInvalid():
    no_input.destroy()


def invalid():
    global no_input

    no_input = Toplevel(root)
    no_input.title('Faild')
    no_input.geometry('150x100')

    req = Label(no_input, text='* field is Required', fg='#ff0000')
    req.pack()

    okay = Button(no_input, text='Okay', command=destroyInvalid)
    okay.pack()

def getEmail():
    data = []
    for parti in participants:
        data.append(parti['email'])
    return data


def display_screen():
    root1 = Toplevel(root)
    root1.geometry('900x300')
    email = Label(root1,text = getEmail())
    email.place(x=20,y=30)
    def destroyscreen():
        root1.destroy()
    terminate = Button(root1, text='x', fg='red', command=destroyscreen)
    terminate.place(x=10, y=270)

    root1.mainloop()


email = Label(root, text='E-mail')
email.place(x=20, y=30)
emailentry = Entry(root, width=20)
emailentry.place(x=90, y=30)
emailentry.focus_set()

password = Label(root, text='Password')
password.place(x=20, y=60)
passwordentry = Entry(root, width=20)
passwordentry.place(x=90, y=60)
passwordentry.focus_set()

startBtn = Button(root, text='Login', width=20, command=getData)
startBtn.place(x=50, y=120)

terminate = Button(root, text='x', fg='red', command=destroyRoot)
terminate.place(x=10, y=270)

root.mainloop()
