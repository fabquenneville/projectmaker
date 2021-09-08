#!/usr/bin/env python3
'''
    These are various tools used by projectmakerpy
'''

import os
import sys
import stat

from datetime import datetime

def load_arguments():
    '''Get/load command parameters 

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    arguments = {
        "path":str(),
        "name":str(),
        "license":False,
        "owner":str(),
    }

    for arg in sys.argv:
        # Confirm with the user that he selected to delete found files
        if "-path:" in arg:
            arguments["path"] = arg[6:]
        elif "-name:" in arg:
            arguments["name"] = arg[6:]
        elif "-license:" in arg:
            arguments["license"] = arg[9:]
        elif "-owner:" in arg:
            arguments["owner"] = arg[7:]

    return arguments

def make_directory(path):
    try:
        os.mkdir(path)
    except OSError:
        print (f"Creating {path} failed")
        return False
    print (f"Successfully created {path}")
    return True

def make_empty(path):
    open(path, 'a').close()
    print (f"Successfully created {path}")

def make_gitignore(path):
    templatespath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/"
    with open(templatespath + "gitignore.txt") as fi:
        with open(path + '.gitignore', 'w') as fo:
            for line in fi:
                fo.write(line)
    print (f"Successfully created {path + '.gitignore'}")

def make_todo(path):
    templatespath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/"

    with open(templatespath + "todo.md") as fi:
        with open(path + 'TODO.md', 'w') as fo:
            for line in fi:
                fo.write(line)

    print (f"Successfully created {path + 'TODO.md'} ")

def make_readme(path, name):
    templatespath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/"

    with open(templatespath + "readme.md") as fi:
        with open(path + 'README.md', 'w') as fo:
            for line in fi:
                fo.write(line.replace("projectname", name))

    print (f"Successfully created {path + 'TODO.md'} ")

def make_license(path, owner, license = False):
    templatespath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/"

    licensefname = "licenses/mit.txt"
    if license == "gpl2":
        licensefname = "licenses/gpl-2.0.txt"
    elif license == "gpl3":
        licensefname = "licenses/gpl-3.0.txt"
    elif license == "moz2":
        licensefname = "licenses/moz2.txt"
    elif license == "apache":
        licensefname = "licenses/apache.txt"

    with open(templatespath + licensefname) as fi:
        with open(path + 'LICENSE', 'w') as fo:
            for line in fi:
                fo.write(line.replace("projectyear", str(datetime.now().year)).replace("projectowner", owner))

    print (f"Successfully created {path + 'LICENSE'} ")

def make_setup(path, owner, name):
    templatespath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/"
    fileoutpath = path + 'setup.py'

    with open(templatespath + "setup.py") as fi:
        with open(fileoutpath, 'w') as fo:
            for line in fi:
                fo.write(line.replace("projectname", name).replace("projectowner", owner))
    print (f"Successfully created {fileoutpath}")

    st = os.stat(fileoutpath)
    os.chmod(fileoutpath, st.st_mode | stat.S_IXUSR | stat.S_IXGRP)
    print (f"Gave executable permission to {fileoutpath}")

def make_main(path, name):
    templatespath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/"
    fileoutpath = path + name + '.py'

    with open(templatespath + "helloworld.py") as fi:
        with open(fileoutpath, 'w') as fo:
            for line in fi:
                fo.write(line)
    print (f"Successfully created {fileoutpath}")

    st = os.stat(fileoutpath)
    os.chmod(fileoutpath, st.st_mode | stat.S_IXUSR | stat.S_IXGRP)
    print (f"Gave executable permission to {fileoutpath}")

    with open(path + '__init__.py', 'w') as f:
        f.write(f"__all__ = ['{name}']")
    print (f"Successfully created {path + '__init__.py'}")
