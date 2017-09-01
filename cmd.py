"""Collect implementation of command"""
import os
from shutil import copyfile, move
import util

def listfile(path):
    """List file"""
    files = os.listdir(path)
    for file in files:
        print file

def changedirectory(currentfolder, path):
    """Changed directory"""
    if path == '..':
        return currentfolder[0:currentfolder.rindex('/')]
    if path == '':
        return util.getproperties('rootFolder')
    else:
        return currentfolder + '/' + path

def copy(src, dst):
    """Copy file"""
    copyfile(src, dst)

def movefile(src, dst):
    """Move file"""
    move(src, dst)
