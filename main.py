#!/usr/bin/python
"""Main script"""

import cmd
import util

rootfolder = util.getproperties('rootFolder')

currentfolder = rootfolder

user = util.getproperties('userName')

args = ['']

while args[0] != 'exit':
    util.printgreting(user, currentfolder)
    args = raw_input().lower().split()
    print 'Entered: %s' % args[0]
    if args[0] == 'ls':
        cmd.listfile(currentfolder)
    elif args[0] == 'cd':
        currentfolder = cmd.changedirectory(currentfolder, args[1])
    elif args[0] == 'cp':
        cmd.copy(currentfolder + '/' + args[1], rootfolder + '/' + args[2])
    elif args[0] == 'mv':
        cmd.move(args[1], args[2])
    # elif args[0] == 'rm':
    # elif args[0] == 'mkdir':
    elif args[0] == 'exit':
        print 'Goodbye!'
    else:
        print 'Wrong command, try again'
