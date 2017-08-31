import os

def listfile(path):
    files = os.listdir(path)
    for f in files:
        print(f)

def changedirectory(currentfolder, path):
    if path == '..':
        return currentfolder[0:currentfolder.rindex('/')]
    if path == '':
        return util.getproperties('rootFolder')
    else:
        return currentfolder + '/' + path
