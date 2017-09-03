"""Collect implementation of command"""
import os
from shutil import copyfile, move

import util


def list_files(path):
    """List files"""
    for file_name in os.listdir(path):
        print file_name


def change_directory(current_folder, path):
    """Change directory"""
    if path == '..':
        return current_folder[0:current_folder.rindex('/')]
    if path == '':
        return util.get_properties('rootFolder')
    return current_folder + '/' + path


def copy(src, dst):
    """Copy file"""
    copyfile(src, dst)


def move_file(src, dst):
    """Move file"""
    move(src, dst)


def remove_file(src):
    """Remove file"""
    if os.path.isdir(src):
        os.rmdir(src)
    else:
        os.remove(src)
