import tkinter as tk
import sys
import argparse
from functools import partial
from vmcontrol import vboxmanage


def close_window(app, variable, event=None):
    global VM
    VM = variable.get()
    app.destroy()


def move_down(variable, allVMs, event=None):
    index = allVMs.index(variable.get())
    if index - 1 < 0:
        index = len(allVMs) - 1
    else:
        index = index - 1
    variable.set(allVMs[index])


def move_up(variable, allVMs, event):
    index = allVMs.index(variable.get())
    if index + 1 > len(allVMs) - 1:
        index = 0
    else:
        index = index + 1
    variable.set(allVMs[index])


def prompt_user(allVMs=[], prompt_text='Please choose a VM to run:'):

    #Init application window
    app = tk.Tk()
    app.title('VMControlGUI')

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

    #key bindings
    app.bind('<Down>', partial(move_down, variable, allVMs))
    app.bind('<Up>', partial(move_up, variable, allVMs))
    app.bind('<Return>', partial(close_window, app, variable))

    app.mainloop()

    return VM


def vm_to_control():

    allVMs = vboxmanage.list_all_vms()

    #Name of VM to controll is passed as argument to the script
    parser = argparse.ArgumentParser()
    parser.add_argument('VirtualMachine', nargs='?', const=None, type=str)
    args = parser.parse_args()

    VM = args.VirtualMachine    

    if VM == None:
        VM = prompt_user(allVMs)

    if VM not in allVMs:
        VM = prompt_user(allVMs=allVMs, prompt_text=f'{VM} is unknown. Please choose a VM:')

    return VM
