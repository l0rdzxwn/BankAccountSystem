import tkinter as gui
from Account import accDetails

balGui = gui.Tk()
balGui.geometry('400x500')
balGui.title('Bank')
balGui.columnconfigure(0,weight=1)

###--MainGUI---###
title = gui.Label(balGui,
                      text='Check Balance',
                      font=('Poppins', 28,'bold'),
                      fg='#0ec93a',
                      pady=47
                      )

symbol = gui.Label(balGui,
                   text='$',
                   font=('Poppins',20, 'bold'),
                   fg='#0ec93a'
                   )

balance = gui.Label(balGui,
                    text=accDetails.balance,
                    font=('Poppins',20, 'bold'),
                    fg='#0ec93a'
                    )

title.grid(row=0,column=0)
symbol.grid(row=1,column=0)
balance.grid(row=1,column=0)
balGui.mainloop()