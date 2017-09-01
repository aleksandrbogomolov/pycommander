"""Collect implementation of command"""
import os
from shutil import copyfile, move
import util


def listfiles(path):
    """List files"""
    for file in os.listdir(path):
        print file


def changedirectory(currentfolder, path):
    """Change directory"""
    if path == '..':
        return currentfolder[0:currentfolder.rindex('/')]
    if path == '':
        return util.getproperties('rootFolder')
    return currentfolder + '/' + path


def copy(src, dst):
    """Copy file"""
    copyfile(src, dst)


def movefile(src, dst):
    """Move file"""
    move(src, dst)
