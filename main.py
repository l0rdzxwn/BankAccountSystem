from tkinter import messagebox
import tkinter as gui
import mysql.connector
from Account import accDetails
import bank_gui
import sqlite3


print(dir(bank_gui))

root = gui.Tk()
root.geometry("400x500")

root.columnconfigure(0, weight=1)

conn = mysql.connector.connect(host='localhost',user='root',password='gRadingsystemDB2024',database='bankaccounts')
accessDB = conn.cursor()

###---Variables---###

accNum = gui.StringVar()
Pin = gui.StringVar()

###---Functions---###

def login():

    values = (accNum.get(), Pin.get())
    accessDB.execute('SELECT * FROM accounts WHERE AccNum = %s AND PIN = %s', values)

    if accNum.get() or Pin.get():
        if accessDB.fetchone():
            messagebox.showinfo('Login Successful',f'Welcome to your account, {accDetails.Name}!')
            bank_gui.runThisShit(accNum.get(), Pin.get())

        else:
            messagebox.showerror('Error','Incorrect account number or pin')
            accNum.set("")
            Pin.set("")
    else:
        messagebox.showerror('Error', 'Please enter a value')



###---LoginGUI---###
topPad = gui.Label(root,
                      text="LOGIN",
                      font=('Poppins', 28, 'bold'),
                      pady= 45,
                      fg='#0ec93a'

                      )

userLabel = gui.Label(root,
                      text="Account Number:",
                      font=('Poppins', 13, 'bold'),
                      pady= 7
                      )
passLabel = gui.Label(root,
                      text="PIN:",
                      font=('Poppins', 13, 'bold'),
                      pady= 6
                      )
spacing = gui.Label(root,
                      text="",
                      font=('Poppins', 2, 'bold')
                      )

user = gui.Entry(root,
                 textvariable=accNum,
                 font=('Poppins', 12),
                 justify='center',
                 relief='flat',
                 highlightbackground='#c7c9c8',
                 highlightcolor='#0ec93a',
                 highlightthickness=2
                 )
pw = gui.Entry(root,
               textvariable=Pin,
               font=('Poppins', 12),
               justify='center',
               relief='flat',
               show='*',
               highlightbackground='#c7c9c8',
               highlightcolor='#0ec93a',
               highlightthickness=2
               )

login = gui.Button(root,
                   text='Proceed',
                   command=login,
                   relief="flat",
                   bg='#0ec93a',
                   font=('Poppins',12,'bold'),
                   width=13,
                   fg= 'white',
                   activebackground='white',
                   activeforeground='#0ec93a',
                   )

topPad.grid(row=0,column=0)
userLabel.grid(row=1, column=0)
passLabel.grid(row=3,column=0)
user.grid(row=2, column=0)
pw.grid(row= 4, column=0)
spacing.grid(row=5,column=0)
login.grid(row=6,column=0)
root.mainloop()


