import sys
from cx_Freeze import setup, Executable
import os.path


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"],"include_files":["tcl86t.dll","tk86t.dll"]}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Cryptosis",
        version = "0.1",
        description = "Cryptosis",
        options = {"build_exe": {"packages":["tkinter"],"include_files":["icon.ico"]}},
        executables = [Executable("Cryptosis.py", base=base,icon='icon.ico')])