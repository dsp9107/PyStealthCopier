import os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
files = filedialog.askopenfilenames(initialdir="shell:MyComputerFolder", title="Select Files")
#drive = filedialog.askdirectory(initialdir=os.getcwd(), title="Select USB Drive")
#print(drive)
drive = os.getcwd()

if files:
    os.system("mkdir data")
    for file in files:
        os.system("xcopy \"" + file.replace("/","\\") + "\" \"" + drive.replace("/","\\") + "data\" /c /q /i /y")

    with open("copy.bat", "w") as bat:
        bat.write("@echo off\n")
        bat.write("xcopy \"%~d0\\data\" \"%userprofile%\\Documents\\obsolete\" /c /q /i /e /y")

    with open("data\\purge.bat", "w") as bat:
        bat.write("@echo off\n")
        bat.write("if exist \"%userprofile%\Documents\obsolete\" rd /s /q \"%userprofile%\Documents\obsolete\"")
