import os
import constants
from os.path import isdir, exists


def check_init():
    cwd = os.getcwd()
    if isdir(constants.VCS_FOLDER_NAME):
        os.chdir(os.path.join(cwd, constants.VCS_FOLDER_NAME))
        if isdir("node") and exists("config") and exists("dag") and exists("stage"):
            return True
    return False


def init():
    try:
        cwd = os.getcwd()
        directory = constants.VCS_FOLDER_NAME
        node = 'node'
        # Parent Directory path
        parent_dir = cwd

        # Path
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        path_node = os.path.join(path, node)
        os.mkdir(path_node)
        os.chdir(path)
        open("dag", 'a').close()
        open("stage", 'a').close()
        open("config", 'a').close()
    except FileExistsError:
        print("Repository already initialized.")
