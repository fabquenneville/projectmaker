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
        "license":"mit",
        "components":list(),
        "readme":True,
        "docs":"sphinx",
        "config":True,
        "git":False,
        "owner":str(),
    }

    for arg in sys.argv:
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
        elif "-components:" in arg:
            arguments["components"] += arg[12:].split(",")
        elif "-readme:" in arg:
            if arg[8:] == "none":
                arguments["readme"] = False
        elif "-docs:" in arg:
            arguments["docs"] = arg[6:]
            if arguments["docs"] == "none":
                arguments["docs"] = False
        elif "-config:" in arg:
            arguments["config"] = arg[8:]
            if arguments["config"] == "none":
                arguments["config"] = False
        elif "-git:" in arg:
            arguments["git"] = arg[5:]
            if arg[5:] == "none":
                arguments["git"] = False
        elif "-owner:" in arg:
            arguments["owner"] = arg[7:]

    return arguments

def make_directory(path):
    ''' Make a directory at the specified path, print and return the success of the operation.

    Args:
        path: The path of the directory to make.

    Returns:
        boolean: The success of the operation
    '''
    try:
        os.mkdir(path)
    except OSError:
        print(f"Creating {path} failed")
        return False
    print(f"Successfully created {path}")
    return True

def make_empty_file(path):
    ''' Make an empty file at the specified path, print and return the success of the operation.

    Args:
        path: The path of the directory to make.

    Returns:
        boolean: The success of the operation
    '''
    try:
        open(path, 'a').close()
    except FileNotFoundError:
        print(f"Creating {path} failed")
        return False
    print(f"Successfully created {path}")
    return True

def make_gitignore(path):
    ''' Builds the projects .gitignore.

    Args:
        path: The path of the file to make.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    if not copyfilled(templatespath + "gitignore.txt", path + '.gitignore'):
        return False
    return True


def make_todo(path):
    ''' Builds the projects TODO.md.

    Args:
        path: The path of the file to make.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    if not copyfilled(templatespath + "todo.md", path + 'TODO.md'):
        return False
    return True

def make_readme(path, projectname, projectlanguage = False):
    ''' Builds the projects README.md.

    Args:
        path:           The path of the directory to make.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    if not copyfilled(
        pathin          = templatespath + "readme.md",
        pathout         = path + 'README.md',
        projectname     = projectname,
        projectlanguage = projectlanguage
    ):
        return False
    return True

def make_css(path):
    ''' Builds the projects default.css.

    Args:
        path: The path of the directory to make.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    if not copyfilled(
        pathin          = templatespath + "sections.css",
        pathout         = path + 'default.css',
    ):
        return False
    return True

def make_php(path, projectowner, projectname):
    ''' Builds the projects basic php files.

    Args:
        path:           The path of the directory to make.
        projectowner:   The name of the owner for the project to pre-fill.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    make_directory(path + projectname)
    make_directory(path + projectname + "/library")
    make_directory(path + projectname + "/library/javascript")
    make_directory(path + projectname + "/library/css")
    make_directory(path + projectname + "/library/php")
    make_directory(path + projectname + "/www")
    make_css(path + projectname + "/library/css/")
    copyfilled(
        pathin          = templatespath + "functions.php",
        pathout         = path + projectname + "/library/php/functions.php",
        projectname     = projectname,
        projectowner    = projectowner
    )
    copyfilled(
        pathin          = templatespath + "functions_builds.php",
        pathout         = path + projectname + "/library/php/functions_builds.php",
        projectname     = projectname,
        projectowner    = projectowner
    )
    copyfilled(
        pathin          = templatespath + "default.js",
        pathout         = path + projectname + '/library/javascript/default.js',
    )
    copyfilled(
        pathin          = templatespath + ".htaccess",
        pathout         = path + projectname + '/www/.htaccess',
    )
    copyfilled(
        pathin          = templatespath + "index.php",
        pathout         = path + projectname + "/www/index.php",
        projectname     = projectname
    )
    chmodx(path + projectname + "/www/index.php")

def make_php_scripts(path, projectowner, projectname):
    ''' Builds the projects basic php files.

    Args:
        path:           The path of the directory to make.
        projectowner:   The name of the owner for the project to pre-fill.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    make_directory(path + projectname)
    make_directory(path + projectname + "/library")
    make_directory(path + projectname + "/library/php")
    copyfilled(
        pathin          = templatespath + "functions.php",
        pathout         = path + projectname + "/library/php/functions.php",
        projectname     = projectname,
        projectowner    = projectowner
    )
    copyfilled(
        pathin          = templatespath + "script.php",
        pathout         = path + projectname + "/" + projectname +".php",
        projectname     = projectname
    )
    chmodx(path + projectname + "/" + projectname +".php")

def make_php_library(path, projectowner, projectname):
    ''' Builds the projects basic php files.

    Args:
        path:           The path of the directory to make.
        projectowner:   The name of the owner for the project to pre-fill.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    make_directory(path + "/library")
    # make_directory(path + projectname + "/library/php")
    copyfilled(
        pathin          = f"{templatespath}phpclass.php",
        pathout         = f"{path}/library/{projectname}.php",
        projectname     = projectname,
        projectowner    = projectowner
    )
    # copyfilled(
    #     pathin          = templatespath + "script.php",
    #     pathout         = path + projectname + "/" + projectname +".php",
    #     projectname     = projectname
    # )
    # chmodx(path + projectname + "/" + projectname +".php")

def make_bash(path, projectowner, projectname):
    ''' Builds the projects basic php files.

    Args:
        path:           The path of the directory to make.
        projectowner:   The name of the owner for the project to pre-fill.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    make_directory(path + projectname)

    copyfilled(
        pathin          = templatespath + "hello.sh",
        pathout         = path + projectname + "/hello.sh",
        projectname     = projectname,
        projectowner    = projectowner
    )
    chmodx(path + projectname + "/hello.sh")

def make_license(path, projectowner, license = False):
    ''' Builds the projects basic php files.

    Args:
        path:           The path of the directory to make.
        projectowner:   The name of the owner for the project to pre-fill.
        license:        The license acronym for the project to pre-fill.
                        (mit, gpl2, gpl3, moz2, apache)

    Returns:
        boolean: The success of the operation
    '''
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

    if not copyfilled(
        pathin          = templatespath + licensefname,
        pathout         = path + 'LICENSE',
        projectowner    = projectowner,
        projectyear     = str(datetime.now().year)
    ):
        return False
    return True

def make_config(path, projectowner, projectname):
    ''' Builds the projects basic php files.

    Args:
        path:           The path of the directory to make.
        projectowner:   The name of the owner for the project to pre-fill.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()

    if not copyfilled(
        pathin          = templatespath + "config.ini",
        pathout         = path + "config.ini",
        projectowner    = projectowner,
        projectname     = projectname
    ):
        return False
    return True

def make_setup(path, projectowner, projectname):
    ''' Builds a basic setup.py for module packaging.

    Args:
        path:           The path of the directory to make.
        projectowner:   The name of the owner for the project to pre-fill.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()
    fileoutpath = path + 'setup.py'

    if not copyfilled(
        pathin          = templatespath + "setup.py",
        pathout         = fileoutpath,
        projectname     = projectname,
        projectowner    = projectowner
    ):
        return False
    return True

def make_python(path, projectowner, projectname):
    ''' Builds a basic pre-filled hello world python module and its __init__.py.

    Args:
        path:           The path of the directory to make.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = get_templates_path()

    make_directory(path + projectname)
    make_directory(path + projectname + "/library")
    make_directory(path + "dist")
    make_setup(
        path            = path,
        projectowner    = projectowner,
        projectname     = projectname
    )
    make_empty_file(path + "requirements.txt")

    if not copyfilled(
        templatespath + "helloworld.py",
        path + projectname + "/" + projectname + '.py'
    ):
        return False

    try:
        with open(path + '__init__.py', 'w') as f:
            f.write(f"__all__ = ['{projectname}']")
    except EnvironmentError:
        return False
    print(f"Successfully created {path + '__init__.py'}")
    return True

def make_docs(path, projectowner, projectname):
    ''' Builds a basic sphinx project documentation and the shell scripts to manage the documentation for release.

    Args:
        path:           The path of the directory to make.
        projectowner:   The name of the owner for the project to pre-fill.
        projectname:    The name for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
    templatespath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/docsource"

    # Making folders
    origfolders = [result[0] for result in os.walk(templatespath)]
    origfolders = [folder for folder in origfolders if folder[len(templatespath)+1:len(templatespath) + 5] != ".git"]
    folderstomake = [folder.replace(templatespath, "") for folder in origfolders if folder.replace(templatespath, "") != ""]
    for i in range(len(folderstomake)):
        if folderstomake[i][:1] == "/":
            folderstomake[i] = folderstomake[i][1:]
    for folder in folderstomake:
        if not make_directory(path + "docsource/" + folder):
            return False
    
    # Copying files
    for folder in origfolders:
        files = os.listdir(folder)
        for filename in files:
            # Skipping some files and all folders
            if filename[-4:] in [".git", ]:
                continue
            if filename[-10:] in [".gitignore", ]:
                continue
            if not os.path.isfile(os.path.join(folder, filename)):
                continue
            
            # Correcting folders missing the slash
            newpath = path + "docsource/" + folder.replace(templatespath, "")[1:]
            if not newpath[-1] == "/":
                newpath += "/"
            
            # Copying the files filled
            if not copyfilled(
                pathin          = folder + "/" + filename,
                pathout         = newpath + filename,
                projectname     = projectname,
                projectowner    = projectowner
            ):
                return False
            if filename in ["makedocs", "make.bat", "Makefile", "conf.py"]:
                chmodx(newpath + filename)

    return True

def chmodx(filepath):
    st = os.stat(filepath)
    os.chmod(filepath, st.st_mode | stat.S_IXUSR | stat.S_IXGRP)
    print(f"Gave executable permission to {os.path.basename(filepath)}")


def copyfilled(pathin, pathout, projectowner = False, projectname = False, projectyear = False, projectlanguage = False):
    ''' Copies a file template filled witht the information passed as parameters.

    Args:
        pathin:         The path of the template.
        pathout:        The path of the file to make.
        projectowner:   The name of the owner for the project to pre-fill.
        projectname:    The name for the project to pre-fill.
        projectyear:    The year for the project to pre-fill.

    Returns:
        boolean: The success of the operation
    '''
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
                if projectlanguage:
                    text = text.replace("projectlanguage", projectlanguage)
                fo.write(text)
    except UnicodeDecodeError:
        try:
            copyfile(pathin, pathout)
        except OSError:
            print(f"Creating {pathout} failed")
            return False
    if pathout[-2:] in ["sh", "py"] or pathout[-3:] in ["bat"]:
        chmodx(pathout)
    print(f"Successfully created {pathout}")
    return True

def get_templates_path():
    ''' Returns the path where the templates are stored.

    Args:

    Returns:
        string: The path of the templates
    '''
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/templates/"

def make_git(path, url, language, projectname, components = list()):
    ''' Initiate a basic git repository and pre-attach some useful submodules for some languages.

    Args:
        path:           The path of the project.
        url:            The url of the blank git repository.
        language:       The programing language of the project.
        projectname:    The name for the project to pre-fill.

    Returns:
    '''
    repo = git.Repo.init(path)
    repo.git.add('--all')
    repo.index.commit("initial commit")
    branchname = repo.active_branch.name
    print(f"Commited to initial git repository.")
    if language == "php":
        if "fontawesome" in components:
            print(f"Adding Font-Awesome submodule to git repository.")
            git.Submodule.add(
                repo = repo,
                url = "git@github.com:FortAwesome/Font-Awesome.git",
                name = "Font-Awesome",
                path = path + projectname + "/www/Font-Awesome"
            )
            repo.index.commit("Added Font-Awesome submodule")
    repo.create_remote("origin", url=url)
    repo.remote("origin").push(branchname)