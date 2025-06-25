import tkinter as gui
import checkBal
import depositBank
import withdrawBank
import main
import mysql.connector
'''
###---Setting up Database Connection---###

conn = mysql.connector.connect(host='localhost',user='root',password='gRadingsystemDB2024',database='bankaccounts')
getDisplayName = conn.cursor()

###---Getting Display Name---###

values = (main.accNum.get(),main.Pin.get())
getDisplayName.execute('SELECT Name FROM accounts WHERE AccNum = %s AND PIN = %s',values)
displayName = getDisplayName.fetchone()[0]
'''
def runThisShit():

    new = gui.Tk()
    new.geometry('400x500')
    new.title('Bank')
    new.columnconfigure(0,weight=1)

###---BankGUI---###

    title = gui.Label(new,
                      text='Welcome, ',
                      font=('Poppins', 28,'bold'),
                      fg='#0ec93a',
                      pady=47
                      )

    checkbal = gui.Button(new,
                          text='Check Balance',
                          command=checkBal.runCB,
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
                          command= depositBank.runDP,
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
                          command=withdrawBank.runWB,
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



