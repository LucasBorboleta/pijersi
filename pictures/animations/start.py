#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""start.py: create environment and start the scrit that makes animated GIF from existing pictures."""


import glob
import os
import subprocess
import sys


_script_home = os.path.abspath(os.path.dirname(__file__))
_make_script = os.path.join(_script_home, "make_gif.py")
_venv_home = os.path.join(_script_home, ".env")

os.chdir(_script_home)

print()
print("Checking virtual environment ...")
if not os.path.isdir(_venv_home):
    print("    Creating virtual environment ...")
    print("        using sys.executable = ", sys.executable)

    subprocess.run(args=[sys.executable, "-m", "venv", ".env"], shell=False, check=True)
    print("    Creating virtual environment done")
    _install_dependencies = True

else:
    _install_dependencies = False
print("Checking virtual environment done")


print()
print("Determining the python executable ...")
if os.name == 'nt':
    _venv_python_executable = os.path.join(_venv_home, "Scripts", "python.exe")

elif os.name == 'posix':
    _venv_python_executable = os.path.join(_venv_home, "bin", "python")

else:
    _venv_python_executable = glob.glob(os.path.join(_venv_home, "*/python*"))[0]

print("    _venv_python_executable = ", _venv_python_executable)
print("Determining the python executable done")


if _install_dependencies:
    print()
    print("Installing dependencies ...")
    print("    using _venv_python_executable = ", _venv_python_executable)

    if os.name == 'nt':
        # windows fix of "import _ssl" failure after "import ssl" during "pip" execution
        _sys_python_path = os.path.dirname(sys.executable)

        if 'PATH' in os.environ:
            os.environ['PATH'] =  (_sys_python_path + os.pathsep +
                                  os.path.join(_sys_python_path, 'Scripts') + os.pathsep +
                                  os.path.join(_sys_python_path, 'Library', 'bin') + os.pathsep +
                                  os.environ['PATH'] )
        else:
            os.environ['PATH'] = (_sys_python_path + os.pathsep +
                                  os.path.join(_sys_python_path, 'Scripts') + os.pathsep +
                                  os.path.join(_sys_python_path, 'Library', 'bin') )

    subprocess.run(args=[_venv_python_executable, "-m", "ensurepip", "--upgrade"], shell=False, check=True)
    subprocess.run(args=[_venv_python_executable, "-m", "pip", "install", "--upgrade", "pip"], shell=False, check=True)
    subprocess.run(args=[_venv_python_executable, "-m", "pip", "install", "-r", "requirements.txt"], shell=False, check=True)
    print()
    print("Installing dependencies done")


print()
print("make_gif ...")
subprocess.run(args=[_venv_python_executable, _make_script], shell=False, check=True)
print()
print("make_gif done")



