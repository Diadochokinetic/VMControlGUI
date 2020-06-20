import sys
import subprocess
import re

def list_vms(command):

    """
    List all existig or running Virtual Machines in Virtual Box.

    args:
        command: string
            Option for listing VMS. 'vms' for all existing VMs and
            'runningvms' for all running VMs.

    return:
        List of all existing or running Virtual Machines.
    """

    #execute shell command to list all existing VMs
    proc=subprocess.Popen(['VBoxManage', 'list', command], stdout=subprocess.PIPE, )

    #retrieve shell output: stdout[0] + statuscode[1]
    output=proc.communicate()

    #decode stdout and read only VM names, discard hashed IDs
    vms = re.findall(r'\"(.+?)\"', output[0].decode('utf-8')) 

    return vms


def list_all_vms():
    return list_vms('vms')


def list_runningvms():
    return list_vms('runningvms')


def start_vm(VM):
    subprocess.call(['VBoxManage', 'startvm', VM])


def stop_vm(VM):
    subprocess.call(['VBoxManage', 'controlvm', VM, 'acpipowerbutton'])
