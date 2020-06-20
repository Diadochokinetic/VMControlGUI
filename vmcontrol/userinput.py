import tkinter as tk
import sys
from functools import partial
from vmcontrol import vboxmanage


def close_window(app, variable):
    global VM
    VM = variable.get()
    app.destroy()


def prompt_user(allVMs=[], prompt_text='Please choose a VM to run:'):

    #Init application window
    app = tk.Tk()

    #Font and orientation setup
    app.geometry('300x150')
    
    #Variable
    variable = tk.StringVar(app)
    variable.set(allVMs[0])

    #Label
    label = tk.Label(text=prompt_text, font=('Helvetica', 12), fg='black')
    label.place(relx=0.5, rely=0.2, anchor='center')

    #Dropdown menu
    menu = tk.OptionMenu(app, variable, *allVMs)
    menu.config(width=20, font=('Helvetica', 12))
    menu.place(relx=0.5, rely=0.5, anchor='center')

    #Button
    button = tk.Button(text='OK', command=partial(close_window, app, variable))
    button.place(relx=0.5, rely=0.8, anchor='center')

    app.mainloop()

    return VM


def vm_to_control():

    allVMs = vboxmanage.list_all_vms()

    #Name of VM to controll is passed as argument to the script
    try:
        VM = sys.argv[1]
    except:
        VM = prompt_user(allVMs)

    if VM not in allVMs:
        VM = prompt_user(allVMs=allVMs, prompt_text=f'{VM} is unknown. Please choose a VM:')

    return VM
