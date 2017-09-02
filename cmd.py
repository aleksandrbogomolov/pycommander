"""Collect implementation of command"""
import os
from shutil import copyfile, move
import util


def listFiles(path):
    """List files"""
    for file in os.listdir(path):
        print file


def changeDirectory(currentFolder, path):
    """Change directory"""
    if path == '..':
        return currentFolder[0:currentFolder.rindex('/')]
    if path == '':
        return util.getProperties('rootFolder')
    return currentFolder + '/' + path


def copy(src, dst):
    """Copy file"""
    copyfile(src, dst)


def movefile(src, dst):
    """Move file"""
    move(src, dst)
