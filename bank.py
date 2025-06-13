import tkinter as gui

def run():
    new = gui.Tk()
    new.geometry('400x500')
    new.title('Bank')
    new.columnconfigure(0,weight=1)

    checkBal = gui.Button(new,
                          text='Check Balance',
                          relief = 'flat',
                          bg='#0ec93a',
                          font=('Poppins', 12, 'bold'),
                          width=13,
                          fg='white',
                          activebackground='white',
                          activeforeground='#0ec93a',
                          )

    deposit = gui.Button(new,
                          text='Deposit',
                          relief = 'flat',
                          bg='#0ec93a',
                          font=('Poppins', 12, 'bold'),
                          width=13,
                          fg='white',
                          activebackground='white',
                          activeforeground='#0ec93a',
                          )

    withdraw = gui.Button(new,
                          text='Withdraw',
                          relief = 'flat',
                          bg='#0ec93a',
                          font=('Poppins', 12, 'bold'),
                          width=13,
                          fg='white',
                          activebackground='white',
                          activeforeground='#0ec93a',
                          )
    checkBal.grid(row=0,column=0)
    deposit.grid(row=1,column=0)
    withdraw.grid(row=2,column=0)
    new.mainloop()