#!/usr/bin/env python3


# Normal import
try:
    from projectmaker.library.tools import load_arguments, make_directory, make_gitignore, make_todo, make_readme, make_php, make_php_scripts, make_php_library, make_python, make_setup, make_empty_file, make_license, make_docs, make_git, make_config
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, make_directory, make_gitignore, make_todo, make_readme, make_php, make_php_scripts, make_php_library, make_python, make_setup, make_empty_file, make_license, make_docs, make_git, make_config


def main():

    # Get/load command parameters
    arguments = load_arguments()
    if len(arguments["path"]) < 1 or len(arguments["name"]) < 1:
        print(f"No path seelected please see: https://fabquenneville.github.io/projectmaker/usage/manual.html")
        return False
    if not make_directory(arguments["path"] + arguments["name"]):
        print(f"Creating {arguments['path'] + arguments['name']} failed.")
        return False

    # Setting variables    
    projectpath = arguments["path"] + arguments["name"] + "/"

    make_directory(projectpath + "misc")

    # Making components
    make_gitignore(projectpath)
    make_todo(projectpath)
    if arguments["readme"]:
        make_readme(
            path            = projectpath,
            projectname     = arguments["name"]
        )
    if arguments["license"]:
        make_license(
            path            = projectpath,
            projectowner    = arguments["owner"],
            license         = arguments["license"]
        )

    # Documentation
    if arguments["docs"]:
        make_directory(projectpath + "docs")
        make_directory(projectpath + "docsource")
        make_docs(
            path            = projectpath, 
            projectowner    = arguments["owner"], 
            projectname     = arguments["name"]
        )
    
    # config.ini
    if arguments["config"]:
        make_config(
            path            = projectpath, 
            projectowner    = arguments["owner"], 
            projectname     = arguments["name"]
        )

    # Main script
    if arguments["language"] == "python":
        make_python(
            path            = projectpath,
            projectowner    = arguments["owner"],
            projectname     = arguments["name"]
        )
    elif arguments["language"] == "php":
        make_php(
            path            = projectpath,
            projectowner    = arguments["owner"],
            projectname     = arguments["name"]
        )
    elif arguments["language"] == "phpscripts":
        make_php_scripts(
            path            = projectpath,
            projectowner    = arguments["owner"],
            projectname     = arguments["name"]
        )
    elif arguments["language"] == "phplibrary":
        make_php_library(
            path            = projectpath,
            projectowner    = arguments["owner"],
            projectname     = arguments["name"]
        )

    # Git creation and commiting of the newly created project
    if arguments["git"]:
        make_git(
            path        = projectpath,
            url         = arguments["git"],
            language    = arguments["language"],
            projectname = arguments["name"],
            components  = arguments["components"]
        )


if __name__ == '__main__':
    main()
