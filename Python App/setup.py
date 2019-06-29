# -*- coding: utf-8 -*-

# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# SimpleTkApp.py is a very simple type of Tkinter application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

#builder in cmd
#python setup.py build

import sys, os
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('CNDH.py', base=base)
]

additional_mods = ['numpy.core._methods', 'numpy.lib.format', "imageio_ffmpeg"]
include_files = [r"C:\Users\momoh\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                 r"C:\Users\momoh\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll",
                 "assetsCNDH/"]
os.environ['TCL_LIBRARY'] = r'C:\Users\momoh\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\momoh\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(name='simple_Tkinter',
      version='0.1',
      description='Sample cx_Freeze Tkinter script',
      executables=executables,
      options = {"build_exe": {"packages": ["tkinter", "PIL", "imageio", "imageio_ffmpeg", "pkg_resources"],
                               "include_files":include_files, 'includes': additional_mods}}
)

sys.exit()