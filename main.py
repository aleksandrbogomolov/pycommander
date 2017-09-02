#!/usr/bin/python
"""Main script"""

import cmd
import util

rootFolder = util.getProperties('rootFolder')

currentFolder = rootFolder

user = util.getProperties('userName')

args = ['']

while args[0] != 'exit':
    util.printGreting(user, currentFolder)
    args = raw_input().lower().split()
    print 'Entered: %s' % args[0]
    if args[0] == 'ls':
        cmd.listFiles(currentFolder)
    elif args[0] == 'cd':
        currentFolder = cmd.changeDirectory(currentFolder, args[1])
    elif args[0] == 'cp':
        cmd.copy(currentFolder + '/' + args[1], rootFolder + '/' + args[2])
    elif args[0] == 'mv':
        cmd.move(args[1], args[2])
    # elif args[0] == 'rm':
    # elif args[0] == 'mkdir':
    elif args[0] == 'exit':
        print 'Goodbye!'
    else:
        print 'Wrong command, try again'
