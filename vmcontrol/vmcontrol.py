import sys
import tkinter as tk
from tkinter import messagebox
from vmcontrol import vboxmanage
from vmcontrol import userinput



def main():

    #Surpresses some default window, don't know why :D
    app = tk.Tk()
    app.withdraw()

    #Retrieve VM to control
    VM = userinput.vm_to_control()

    if VM in vboxmanage.list_runningvms():
        if tk.messagebox.askyesno('VM-Control', f'Shutdown {VM}?'):
            print(f'{VM} will be shutdown')
            vboxmanage.stop_vm(VM)
    else:
        if tk.messagebox.askyesno('VM-Control', f'Start {VM}?'):
            print(f'{VM} will be started.')
            vboxmanage.start_vm(VM)
