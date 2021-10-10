#!/usr/bin/env python3


# Normal import
try:
    from projectmakerpy.library.tools import load_arguments, make_directory, make_gitignore, make_todo, make_readme, make_main, make_setup, make_empty_file, make_license, make_docs
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, make_directory, make_gitignore, make_todo, make_readme, make_main, make_setup, make_empty_file, make_license, make_docs


def main():

    # Get/load command parameters
    arguments = load_arguments()
    if len(arguments["path"]) < 1 or len(arguments["name"]) < 1:
        return False
    if not make_directory(arguments["path"] + arguments["name"]):
        return False

    # Setting variables    
    projectpath = arguments["path"] + arguments["name"] + "/"
    codepath = projectpath + arguments["name"] + "/"

    # Making main folders
    make_directory(projectpath + "dist")
    make_directory(projectpath + "misc")
    make_directory(projectpath + arguments["name"])
    make_directory(projectpath + arguments["name"] + "/library")

    # Making components
    make_gitignore(projectpath)
    make_todo(projectpath)
    make_readme(
        path            = projectpath,
        projectname     = arguments["name"]
    )
    make_setup(
        path            = projectpath,
        projectowner    = arguments["owner"],
        projectname     = arguments["name"]
    )
    make_license(
        path            = projectpath,
        projectowner    = arguments["owner"],
        license         = arguments["license"]
    )
    make_empty_file(projectpath + "requirements.txt")
    make_main(codepath, arguments["name"])

    # Documentation
    make_directory(projectpath + "docs")
    make_directory(projectpath + "docsource")
    if arguments["docs"]:
        make_docs(
            path            = projectpath, 
            projectowner    = arguments["owner"], 
            projectname     = arguments["name"]
        )


if __name__ == '__main__':
    main()
