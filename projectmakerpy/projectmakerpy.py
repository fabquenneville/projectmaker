#!/usr/bin/env python3


# Normal import
try:
    from projectmakerpy.library.tools import load_arguments, make_directory, make_gitignore, make_todo, make_readme, make_main, make_setup, make_empty, make_license
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, make_directory, make_gitignore, make_todo, make_readme, make_main, make_setup, make_empty, make_license


def main():

    # Get/load command parameters
    arguments = load_arguments()

    if len(arguments["path"]) < 1 or len(arguments["name"]) < 1:
        return False

    if arguments["path"][-1:] != "/":
        arguments["path"] = arguments["path"] + "/"
    
    if not make_directory(arguments["path"] + arguments["name"]):
        exit()
    
    projectpath = arguments["path"] + arguments["name"] + "/"
    codepath = projectpath + arguments["name"] + "/"

    make_directory(projectpath + "dist")
    make_directory(projectpath + "docs")
    make_directory(projectpath + "docsource")
    make_directory(projectpath + "misc")
    make_directory(projectpath + arguments["name"])
    make_directory(projectpath + arguments["name"] + "/library")

    make_gitignore(projectpath)
    make_todo(projectpath)
    make_readme(projectpath, arguments["name"])
    make_setup(projectpath, arguments["owner"], arguments["name"])
    make_license(projectpath, arguments["owner"], arguments["license"])
    make_empty(projectpath + "requirements.txt")
    
    make_main(codepath, arguments["name"])


if __name__ == '__main__':
    main()
