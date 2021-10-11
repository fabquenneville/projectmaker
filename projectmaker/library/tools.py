#!/usr/bin/env python3
'''
    These are various tools used by projectmakerpy
'''

import git
import os
import sys
import stat

from datetime import datetime
from shutil import copyfile

def load_arguments():
    '''Get/load command parameters 

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    arguments = {
        "path":str(),
        "name":str(),
        "language":"python",
        "license":False,
        "readme":True,
        "docs":True,
        "git":False,
        "owner":str(),
    }

    for arg in sys.argv:
        # Confirm with the user that he selected to delete found files
        if "-path:" in arg:
            path = arg[6:]
            if path[-1:] != "/":
                path = path + "/"
            arguments["path"] = path
        elif "-name:" in arg:
            arguments["name"] = arg[6:]
        elif "-language:" in arg:
            arguments["language"] = arg[10:]
        elif "-license:" in arg:
            arguments["license"] = arg[9:]
            if arguments["license"] == "none":
                arguments["license"] = False
        elif "-readme:" in arg:
            if arg[8:] == "none":
                arguments["readme"] = False
        elif "-docs:" in arg:
            if arg[6:] == "none":
                arguments["docs"] = False
        elif "-git:" in arg:
            arguments["git"] = arg[5:]
            if arg[5:] == "none":
                arguments["git"] = False
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

def make_empty_file(path):
    open(path, 'a').close()
    print (f"Successfully created {path}")

def make_gitignore(path):
    templatespath = get_templates_path()
    copyfilled(templatespath + "gitignore.txt", path + '.gitignore')

def make_todo(path):
    templatespath = get_templates_path()

    copyfilled(templatespath + "todo.md", path + 'TODO.md')

def make_readme(path, projectname):
    templatespath = get_templates_path()
    copyfilled(
        pathin          = templatespath + "readme.md",
        pathout         = path + 'README.md',
        projectname     = projectname
    )

def make_css(path):
    templatespath = get_templates_path()
    copyfilled(
        pathin          = templatespath + "sections.css",
        pathout         = path + 'default.css',
    )

def make_php_libraries(path, projectowner, projectname):
    templatespath = get_templates_path()
    copyfilled(
        pathin          = templatespath + "functions.php",
        pathout         = path + 'functions.php',
        projectname     = projectname,
        projectowner    = projectowner
    )
    copyfilled(
        pathin          = templatespath + "functions_builds.php",
        pathout         = path + 'functions_builds.php',
        projectname     = projectname,
        projectowner    = projectowner
    )

def make_license(path, projectowner, license = False):
    templatespath = get_templates_path()

    licensefname = "licenses/mit.txt"
    if license == "gpl2":
        licensefname = "licenses/gpl-2.0.txt"
    elif license == "gpl3":
        licensefname = "licenses/gpl-3.0.txt"
    elif license == "moz2":
        licensefname = "licenses/moz2.txt"
    elif license == "apache":
        licensefname = "licenses/apache.txt"

    copyfilled(
        pathin          = templatespath + licensefname,
        pathout         = path + 'LICENSE',
        projectowner    = projectowner,
        projectyear     = str(datetime.now().year)
    )

def make_setup(path, projectowner, projectname):
    templatespath = get_templates_path()
    fileoutpath = path + 'setup.py'

    copyfilled(
        pathin          = templatespath + "setup.py",
        pathout         = fileoutpath,
        projectname     = projectname,
        projectowner    = projectowner
    )

def make_main_python(path, name):
    templatespath = get_templates_path()
    fileoutpath = path + name + '.py'

    copyfilled(templatespath + "helloworld.py", fileoutpath)

    with open(path + '__init__.py', 'w') as f:
        f.write(f"__all__ = ['{name}']")
    print (f"Successfully created {path + '__init__.py'}")

def make_main_php(path, projectname):
    templatespath = get_templates_path()

    copyfilled(
        pathin          = templatespath + "index.php",
        pathout         = path + 'index.php',
        projectname     = projectname
    )


def make_docs(path, projectowner, projectname):
    templatespath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/docsource"

    # Making folders
    origfolders = [result[0] for result in os.walk(templatespath)]
    origfolders = [folder for folder in origfolders if folder[len(templatespath)+1:len(templatespath) + 5] != ".git"]
    folderstomake = [folder.replace(templatespath, "") for folder in origfolders if folder.replace(templatespath, "") != ""]
    for i in range(len(folderstomake)):
        if folderstomake[i][:1] == "/":
            folderstomake[i] = folderstomake[i][1:]
    for folder in folderstomake:
        make_directory(path + "docsource/" + folder)
    
    # Copying files
    for folder in origfolders:
        files = os.listdir(folder)
        for filename in files:
            if filename[-4:] in [".git", ]:
                continue
            if filename[-10:] in [".gitignore", ]:
                continue
            if not os.path.isfile(os.path.join(folder, filename)):
                continue
            copyfilled(
                pathin          = folder + "/" + filename,
                pathout         = path + "docsource/" + folder.replace(templatespath, "")[1:] + filename,
                projectname     = projectname,
                projectowner    = projectowner
            )

def copyfilled(pathin, pathout, projectowner = False, projectname = False, projectyear = False):
    try:
        with open(pathin) as fi:
            with open(pathout, 'w') as fo:
                text = fi.read()
                if projectowner:
                    text = text.replace("projectowner", projectowner)
                if projectname:
                    text = text.replace("projectname", projectname)
                if projectyear:
                    text = text.replace("projectyear", projectyear)
                fo.write(text)
    except UnicodeDecodeError:
        copyfile(pathin, pathout)
    print (f"Successfully created {pathout}")
    if pathout[-2:] in ["sh", "py"] or pathout[-3:] in ["bat"]:
        st = os.stat(pathout)
        os.chmod(pathout, st.st_mode | stat.S_IXUSR | stat.S_IXGRP)
        print (f"Gave executable permission to {pathout}")

def get_templates_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/"

def make_git(path, url, language, projectname):
    repo = git.Repo.init(path)
    # repo.git.add(u=True)
    repo.git.add('--all')
    repo.index.commit("initial commit")
    print (f"Commited to initial git repository.")
    if language == "php":
        git.Submodule.add(
            repo = repo,
            url = "git@github.com:FortAwesome/Font-Awesome.git",
            name = "Font-Awesome",
            path = path + projectname + "/www/Font-Awesome"
        )
        repo.index.commit("Added Font-Awesome submodule")
        print (f"Added Font-Awesome submodule to git repository.")
    repo.create_remote("origin", url=url)
    repo.remote("origin").push("main")