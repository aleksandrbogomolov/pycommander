#!/usr/bin/python
"""Main script"""

import cmd
import util

root_folder = util.get_properties('rootFolder')

current_folder = root_folder

user = util.get_properties('userName')

args = ['']

while args[0] != 'exit':
    util.print_greetings(user, current_folder)
    args = raw_input().lower().split()
    print 'Entered: %s' % args[0]
    if args[0] == 'ls':
        cmd.list_files(current_folder)
    elif args[0] == 'cd':
        current_folder = cmd.change_directory(current_folder, args[1])
    elif args[0] == 'cp':
        cmd.copy(current_folder + '/' + args[1], root_folder + '/' + args[2])
    elif args[0] == 'mv':
        cmd.move_file(args[1], args[2])
    # elif args[0] == 'rm':
    # elif args[0] == 'mkdir':
    elif args[0] == 'exit':
        print 'Goodbye!'
    else:
        print 'Wrong command, try again'
