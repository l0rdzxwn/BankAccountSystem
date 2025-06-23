import tkinter as gui
import Account



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
                        text=f'CASH                ${Account.accDetails.balance}',
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
