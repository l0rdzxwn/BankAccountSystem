import tkinter as gui
import Account
import mysql.connector
import main

conn = mysql.connector.connect(host='localhost',user='root',password='gRadingsystemDB2024',database='bankaccounts')
directToDB = conn.cursor()
values = (main.accNum.get(),main.Pin.get())
directToDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s',values)
balanceVal = directToDB.fetchone()[0]

def addHundred():
    finalValue = balanceVal + 100
    dbVal = (finalValue,main.accNum.get())
    directToDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s',dbVal)
    conn.commit()
'''
    directToDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
    getLatest = directToDB.fetchone()[0]
'''


def runDP():
    dep = gui.Tk()
    dep.geometry('400x500')
    dep.title('Deposit Cash')



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


    buttonFrm = gui.Frame(dep, bg='white')
    buttonFrm2 = gui.Frame(dep, bg='white',pady=10)

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

    title.grid(row=0, column=0)
    balance.grid(row=1, column=0)
    spacing1.grid(row=2, column=0)
    buttonFrm.grid(row=3,column=0)
    buttonFrm2.grid(row=4,column=0)
    dep.mainloop()

runDP()
