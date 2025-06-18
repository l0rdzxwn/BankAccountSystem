import tkinter as gui
from Account import accDetails
import bank

def runDep():
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
                        text=f'CASH                ${accDetails.balance}',
                        font=('Poppins', 25, 'bold'),
                        fg='white',
                        pady=25,
                        padx=35,
                        bg='#0ec93a',
                        height=1
                        )

    backBtn = gui.Button(dep,
                         text='Go Back',

                         relief='flat',
                         bg='#0ec93a',
                         font=('Poppins', 15, 'bold'),
                         width=13,
                         fg='white',
                         activebackground='white',
                         activeforeground='#0ec93a'
                         )

    hundred = gui.Button(dep,
                         text='100$',
                         relief='flat',
                         bg='#0ec93a',
                         font=('Poppins', 15, 'bold'),
                         width=13,
                         fg='white',
                         activebackground='white',
                         activeforeground='#0ec93a'
                         )

    thousand = gui.Button(dep,
                         text='1000$',
                         relief='flat',
                         bg='#0ec93a',
                         font=('Poppins', 15, 'bold'),
                         width=13,
                         fg='white',
                         activebackground='white',
                         activeforeground='#0ec93a'
                         )

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
    hundred.grid(row=3, column=0)
    thousand.grid(row=3, column=1)
    backBtn.grid(row=4, column=0)

    dep.mainloop()

runDep()