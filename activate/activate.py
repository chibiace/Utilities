#!/usr/bin/env python

# !Untested!
# -----------------------------------------------------------
#  Enters a python virtual environment in a new shell
#  chibiace 04/12/2023
# -----------------------------------------------------------
#
import subprocess
import os


shell = os.environ['SHELL']
shell_name = shell.split("/")[-1]
command = 'source ./{{PATH}}/bin/activate{{SHELL}};'

# print(f'{shell} | {shell_name}')

if shell_name == "bash":
    command = command.replace("{{SHELL}}","")
if shell_name == "fish":
    command = command.replace("{{SHELL}}",".fish")
if shell_name == "csh":
    command = command.replace("{{SHELL}}",".csh")

def activate():

    global command
    if os.path.exists("./venv"):
        path = "venv"
        command = command.replace("{{PATH}}",path)
        subprocess.call(f'{command};{shell_name}', shell=True, executable=shell)
        return True
    else:
        if os.path.exists("./env"):
            path = "env"
            command = command.replace("{{PATH}}",path)
            subprocess.call(f'{command};{shell_name}', shell=True, executable=shell)
            return True

activate()
