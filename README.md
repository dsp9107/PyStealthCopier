# PyStealthCopier

### Requirements
- Windows Environment
- Python 3.7.3 +

And the python packages :
- tkinter
- os

### Usage
Follow these instructions to make a usb stealthcopier :
- plug in your usb drive into your system
- preferably, create a new folder
- put `PyStealthCopier.py` in the folder
- run `PyStealthCopier.py`
- select files you want to be copied to victim's system
- wait for execution to complete
- plug out your usb drive
- done

Follow these instructions to run your usb stealthcopier :
- plug in your usb drive into victim's system
- run `copy.bat` under whichever folder you copied it in
- all the files in sub-folder data will be copied to `Documents\obsolete`
- usb drive can be safely removed
- when done, simply run `Documents\obsolete\purge.bat`
- done
