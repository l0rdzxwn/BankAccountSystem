from tkinter import messagebox
import tkinter as gui
import mysql.connector
from Account import accDetails
import bank_gui
import sqlite3
import withdraw_gui
import depositBank
import checkBal

print(dir(withdraw_gui))

root = gui.Tk()
root.geometry("400x500")

root.columnconfigure(0, weight=1)

conn = mysql.connector.connect(host='localhost',user='root',password='gRadingsystemDB2024',database='bankaccounts')
accessDB = conn.cursor()

###---Variables---###

accNum = gui.StringVar()
Pin = gui.StringVar()






###---Homepage---###

def runThisShit(acc,pin):



###---Getting Display Name---###

    values = (acc, pin)
    accessDB.execute('SELECT Name FROM accounts WHERE AccNum = %s AND PIN = %s', values)
    displayName = accessDB.fetchone()[0]

###--- GUI ---###

    new = gui.Toplevel()
    new.geometry('400x500')
    new.title('Bank')
    new.columnconfigure(0,weight=1)

###---BankGUI---###

    title = gui.Label(new,
                      text=f'Welcome, {displayName}',
                      font=('Poppins', 28,'bold'),
                      fg='#0ec93a',
                      pady=47
                      )

    checkbal = gui.Button(new,
                          text='Check Balance',
                          command=runCB,
                          relief = 'flat',
                          bg='#0ec93a',
                          font=('Poppins', 15, 'bold'),
                          width=13,
                          fg='white',
                          activebackground='white',
                          activeforeground='#0ec93a'
                          )

    deposit = gui.Button(new,
                          text='Deposit',
                          command=runDP,
                          relief = 'flat',
                          bg='#0ec93a',
                          font=('Poppins', 15, 'bold'),
                          width=13,
                          fg='white',
                          activebackground='white',
                          activeforeground='#0ec93a'
                          )

    withdraw = gui.Button(new,
                          text='Withdraw',
                          command=runWD,
                          relief = 'flat',
                          bg='#0ec93a',
                          font=('Poppins', 15, 'bold'),
                          width=13,
                          fg='white',
                          activebackground='white',
                          activeforeground='#0ec93a'
                          )

    spacing2 = gui.Label(new,
                         text="",
                         font=('Poppins', 2, 'bold')
                         )
    spacing3 = gui.Label(new,
                         text="",
                         font=('Poppins', 2, 'bold')
                         )

    title.grid(row=0,column=0)
    checkbal.grid(row=1,column=0)
    spacing2.grid(row=2, column=0)
    deposit.grid(row=3,column=0)
    spacing3.grid(row=4, column=0)
    withdraw.grid(row=5,column=0)
    new.mainloop()

#------------------------------------------------------------------------ END OF BANKGUI ----------------------------------------------------------------------------------------#








###---Withdraw GUI---###

def runWD():
    wit = gui.Tk()
    wit.geometry('400x500')
    wit.title('Withdraw Cash')


    values = (accNum.get(), Pin.get())
    accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
    balanceVal = accessDB.fetchone()[0]

    def addHundred():
        accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = accessDB.fetchone()[0]

        finalValue = latestValue - 100
        if finalValue < 0:
            logLabel.config(text='Insufficient funds to withdraw')
        else:
            dbVal = (finalValue, accNum.get())
            accessDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
            conn.commit()
            balance.config(text=f'CASH                ${finalValue}')
            logLabel.config(text='Successfully added $100...')

    def addThousand():
        accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = accessDB.fetchone()[0]
        finalValue = latestValue - 1000
        if finalValue < 0:
            logLabel.config(text='Insufficient funds to withdraw')
        else:
            dbVal = (finalValue, accNum.get())
            accessDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
            conn.commit()
            balance.config(text=f'CASH                ${finalValue}')
            logLabel.config(text='Successfully withdrawn $1000...')

    def addTenThousand():
        accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = accessDB.fetchone()[0]

        finalValue = latestValue - 10000
        if finalValue < 0:
            logLabel.config(text='Insufficient funds to withdraw')
        else:
            dbVal = (finalValue, accNum.get())
            accessDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
            conn.commit()
            balance.config(text=f'CASH                ${finalValue}')
            logLabel.config(text='Successfully withdrawn $10,000...')

    def addHundredThousand():
        accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = accessDB.fetchone()[0]

        finalValue = latestValue - 100000
        if finalValue < 0:
            logLabel.config(text='Insufficient funds to withdraw')
        else:
            dbVal = (finalValue, accNum.get())
            accessDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
            conn.commit()

            balance.config(text=f'CASH                ${finalValue}')
            logLabel.config(text='Successfully withdrawn $100,000...')

    ###---Withdraw---###
    title = gui.Label(wit,
                      text='Withdraw',
                      font=('Poppins', 28, 'bold'),
                      fg='#0ec93a',
                      pady=20
                      )

    balance = gui.Label(wit,
                        text=f'CASH                ${balanceVal}',
                        font=('Poppins', 25, 'bold'),
                        fg='white',
                        pady=25,
                        padx=35,
                        bg='#0ec93a',
                        height=1
                        )

    buttonFrm = gui.Frame(wit, bg='#f0f0f0')
    buttonFrm2 = gui.Frame(wit, pady=10, bg='#f0f0f0')

    hundred = gui.Button(buttonFrm,
                         text='100$',
                         command=addHundred,
                         relief='flat',
                         bg='#0ec93a',
                         font=('Poppins', 15, 'bold'),
                         width=13,
                         fg='white',
                         activebackground='white',
                         activeforeground='#0ec93a'
                         )
    hundred.pack(side='left', padx=2)

    thousand = gui.Button(buttonFrm,
                          text='1000$',
                          command=addThousand,
                          relief='flat',
                          bg='#0ec93a',
                          font=('Poppins', 15, 'bold'),
                          width=13,
                          fg='white',
                          activebackground='white',
                          activeforeground='#0ec93a'
                          )
    thousand.pack(side='right', padx=2)

    tenThs = gui.Button(buttonFrm2,
                        text='10000$',
                        command=addTenThousand,
                        relief='flat',
                        bg='#0ec93a',
                        font=('Poppins', 15, 'bold'),
                        width=13,
                        fg='white',
                        activebackground='white',
                        activeforeground='#0ec93a'
                        )
    tenThs.pack(side="left", padx=2)

    hundredThs = gui.Button(buttonFrm2,
                            text='100000$',
                            command=addHundredThousand,
                            relief='flat',
                            bg='#0ec93a',
                            font=('Poppins', 15, 'bold'),
                            width=13,
                            fg='white',
                            activebackground='white',
                            activeforeground='#0ec93a'
                            )
    hundredThs.pack(side="right", padx=2)

    spacing1 = gui.Label(wit,
                         text="",
                         font=('Poppins', 2, 'bold')
                         )

    spacing2 = gui.Label(wit,
                         text="",
                         font=('Poppins', 2, 'bold')
                         )

    ###---log Frame---###

    buttonFrm3 = gui.Frame(wit, bg='#f0f0f0', pady=10)

    logLabel = gui.Label(buttonFrm3,
                         text="",
                         fg='#e62727',
                         font=('Poppins', 14, 'bold')
                         )
    logLabel.pack(side='left')

    title.grid(row=0, column=0)
    balance.grid(row=1, column=0)
    spacing1.grid(row=2, column=0)
    buttonFrm.grid(row=3, column=0)
    buttonFrm2.grid(row=4, column=0)
    buttonFrm3.grid(row=5, column=0)
    wit.mainloop()

#------------------------------------------------------------------------ END OF WITHDRAW GUI ----------------------------------------------------------------------------------------#








###--- Deposit GUI ---###

def runDP():
    dep = gui.Tk()
    dep.geometry('400x500')
    dep.title('Deposit Cash')


    values = (accNum.get(), Pin.get())
    accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
    balanceVal = accessDB.fetchone()[0]

    def addHundred():
        accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = accessDB.fetchone()[0]

        finalValue = latestValue + 100
        dbVal = (finalValue, accNum.get())
        accessDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
        conn.commit()
        balance.config(text=f'CASH                ${finalValue}')
        logLabel.config(text='Successfully added $100...')

    def addThousand():
        accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = accessDB.fetchone()[0]

        finalValue = latestValue + 1000
        dbVal = (finalValue, accNum.get())
        accessDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
        conn.commit()
        balance.config(text=f'CASH                ${finalValue}')
        logLabel.config(text='Successfully added $1,000...')

    def addTenThousand():
        accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = accessDB.fetchone()[0]

        finalValue = latestValue + 10000
        dbVal = (finalValue, accNum.get())
        accessDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
        conn.commit()
        balance.config(text=f'CASH                ${finalValue}')
        logLabel.config(text='Successfully added $10,000...')

    def addHundredThousand():
        accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = accessDB.fetchone()[0]

        finalValue = latestValue + 100000
        dbVal = (finalValue, accNum.get())
        accessDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
        conn.commit()
        balance.config(text=f'CASH                ${finalValue}')
        logLabel.config(text='Successfully added $100,000...')

    ###---Deposit---###
    title = gui.Label(dep,
                      text='Deposit',
                      font=('Poppins', 28, 'bold'),
                      fg='#0ec93a',
                      pady=20
                      )

    balance = gui.Label(dep,
                        text=f'CASH                ${balanceVal}',
                        font=('Poppins', 25, 'bold'),
                        fg='white',
                        pady=25,
                        padx=35,
                        bg='#0ec93a',
                        height=1
                        )



    buttonFrm = gui.Frame(dep, bg= '#f0f0f0')
    buttonFrm2 = gui.Frame(dep,pady=10, bg='#f0f0f0')

    hundred = gui.Button(buttonFrm,
                         text='100$',
                         command=addHundred,
                         relief='flat',
                         bg='#0ec93a',
                         font=('Poppins', 15, 'bold'),
                         width=13,
                         fg='white',
                         activebackground='white',
                         activeforeground='#0ec93a'
                         )
    hundred.pack(side='left', padx=2)

    thousand = gui.Button(buttonFrm,
                         text='1000$',
                          command=addThousand,
                         relief='flat',
                         bg='#0ec93a',
                         font=('Poppins', 15, 'bold'),
                         width=13,
                         fg='white',
                         activebackground='white',
                         activeforeground='#0ec93a'
                         )
    thousand.pack(side='right',padx=2)

    tenThs = gui.Button(buttonFrm2,
                            text='10000$',
                            command=addTenThousand,
                            relief='flat',
                            bg='#0ec93a',
                            font=('Poppins', 15, 'bold'),
                            width=13,
                            fg='white',
                            activebackground='white',
                            activeforeground='#0ec93a'
                            )
    tenThs.pack(side="left", padx=2)

    hundredThs = gui.Button(buttonFrm2,
                          text='100000$',
                          command=addHundredThousand,
                          relief='flat',
                          bg='#0ec93a',
                          font=('Poppins', 15, 'bold'),
                          width=13,
                          fg='white',
                          activebackground='white',
                          activeforeground='#0ec93a'
                          )
    hundredThs.pack(side="right", padx=2)

    spacing1 = gui.Label(dep,
                         text="",
                         font=('Poppins', 2, 'bold')
                         )

    spacing2 = gui.Label(dep,
                         text="",
                         font=('Poppins', 2, 'bold')
                         )

    ###---log Frame---###

    buttonFrm3 = gui.Frame(dep, bg='#f0f0f0', pady=10)

    logLabel = gui.Label(buttonFrm3,
                         text= "",
                         fg= '#0ec93a',
                         font=('Poppins',14,'bold')
                         )
    logLabel.pack(side='left')


    title.grid(row=0, column=0)
    balance.grid(row=1, column=0)
    spacing1.grid(row=2, column=0)
    buttonFrm.grid(row=3,column=0)
    buttonFrm2.grid(row=4,column=0)
    buttonFrm3.grid(row=5, column=0)
    dep.mainloop()

#------------------------------------------------------------------------ END OF DEPOSIT GUI ----------------------------------------------------------------------------------------#




###--- Check Balance GUI ---###

def runCB():

    values = (accNum.get(),Pin.get())
    accessDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
    currentBalance = accessDB.fetchone()[0]


    balGui = gui.Tk()
    balGui.geometry('400x500')
    balGui.title('Bank')
    balGui.columnconfigure(0,weight=1)

    ###--MainGUI---###
    title = gui.Label(balGui,
                          text='Check Balance',
                          font=('Poppins', 28,'bold'),
                          fg='#0ec93a',
                          pady=20
                          )

    balance = gui.Label(balGui,
                        text=f'CASH                ${currentBalance}',
                        font=('Poppins',25, 'bold'),
                        fg='white',
                        pady=25,
                        padx=35,
                        bg='#0ec93a',
                        height=1
                        )

    deposit = gui.Button(balGui,
                              text='Deposit',
                              command= runDP,
                              relief = 'flat',
                              bg='#0ec93a',
                              font=('Poppins', 15, 'bold'),
                              width=13,
                              fg='white',
                              activebackground='white',
                              activeforeground='#0ec93a'
                              )

    withdraw = gui.Button(balGui,
                              text='Withdraw',
                              command= runWD,
                              relief = 'flat',
                              bg='#0ec93a',
                              font=('Poppins', 15, 'bold'),
                              width=13,
                              fg='white',
                              activebackground='white',
                              activeforeground='#0ec93a'
                              )

    spacing1 = gui.Label(balGui,
                             text="",
                             font=('Poppins', 2, 'bold')
                             )

    spacing2 = gui.Label(balGui,
                             text="",
                             font=('Poppins', 2, 'bold')
                             )


    title.grid(row=0,column=0)
    balance.grid(row=1,column=0)
    spacing1.grid(row=2,column=0)
    deposit.grid(row=3,column=0)
    spacing2.grid(row=4,column=0)
    withdraw.grid(row=5,column=0)
    balGui.mainloop()

#------------------------------------------------------------------------ END OF CHECK BALANCE GUI ----------------------------------------------------------------------------------------#


def login():

    values = (accNum.get(), Pin.get())
    accessDB.execute('SELECT * FROM accounts WHERE AccNum = %s AND PIN = %s', values)

    if accNum.get() or Pin.get():
        if accessDB.fetchone():
            messagebox.showinfo('Login Successful',f'Welcome to your account, {accDetails.Name}!')
            runThisShit(accNum.get(), Pin.get())

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


