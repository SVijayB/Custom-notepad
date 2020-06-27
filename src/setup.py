import sys
from cx_Freeze import setup, Executable

build_exe_options = {'include_files': ['../assets/images/Icon.ico', '../temp/preferences.txt', '../temp/temp.txt'],
"optimize": 2}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('Notepad.py', base=base, icon = "../assets/images/Icon.ico")
]
  
setup(name = "Notepad" , 
      version = "1.0.0" , 
      description = "Customised Notepad" ,
      options= {"build_exe": build_exe_options},
      executables = executables) 