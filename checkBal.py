import tkinter as gui
from Account import accDetails
import bank

def runCB():

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
                        text=f'CASH                ${accDetails.balance}',
                        font=('Poppins',25, 'bold'),
                        fg='white',
                        pady=25,
                        padx=35,
                        bg='#0ec93a',
                        height=1
                        )

    deposit = gui.Button(balGui,
                              text='Deposit',
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

