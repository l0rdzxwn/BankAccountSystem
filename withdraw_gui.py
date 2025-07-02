import main
import mysql.connector
import tkinter as gui



def runWD():
    wit = gui.Tk()
    wit.geometry('400x500')
    wit.title('Withdraw Cash')

    conn = mysql.connector.connect(host='localhost', user='root', password='gRadingsystemDB2024',
                                   database='bankaccounts')
    directToDB = conn.cursor()
    values = (main.accNum.get(), main.Pin.get())
    directToDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
    balanceVal = directToDB.fetchone()[0]

    def addHundred():
        directToDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = directToDB.fetchone()[0]

        finalValue = latestValue - 100
        if finalValue < 0:
            logLabel.config(text='Insufficient funds to withdraw')
        else:
            dbVal = (finalValue, main.accNum.get())
            directToDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
            conn.commit()
            balance.config(text=f'CASH                ${finalValue}')
            logLabel.config(text='Successfully added $100...')

    def addThousand():
        directToDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = directToDB.fetchone()[0]
        finalValue = latestValue - 1000
        if finalValue < 0:
            logLabel.config(text='Insufficient funds to withdraw')
        else:
            dbVal = (finalValue, main.accNum.get())
            directToDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
            conn.commit()
            balance.config(text=f'CASH                ${finalValue}')
            logLabel.config(text='Successfully withdrawn $1000...')

    def addTenThousand():
        directToDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = directToDB.fetchone()[0]

        finalValue = latestValue - 10000
        if finalValue < 0:
            logLabel.config(text='Insufficient funds to withdraw')
        else:
            dbVal = (finalValue, main.accNum.get())
            directToDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
            conn.commit()
            balance.config(text=f'CASH                ${finalValue}')
            logLabel.config(text='Successfully withdrawn $10,000...')

    def addHundredThousand():
        directToDB.execute('SELECT Balance FROM accounts WHERE AccNum = %s AND PIN = %s', values)
        latestValue = directToDB.fetchone()[0]

        finalValue = latestValue - 1000
        if finalValue < 0:
            logLabel.config(text='Insufficient funds to withdraw')
        else:
            dbVal = (finalValue, main.accNum.get())
            directToDB.execute('UPDATE accounts SET Balance = %s WHERE AccNum = %s', dbVal)
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



