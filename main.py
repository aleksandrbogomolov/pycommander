import util
import cmd

rootfolder = util.getproperties('rootFolder')

currentfolder = rootfolder

user = util.getproperties('userName')

args = ['']

while args[0] != 'exit':
    util.printgreting(user, currentfolder)
    args = input().lower().split()
    print('Entered: %s' % args[0])
    if args[0] == 'ls':
        cmd.listfile(currentfolder)
    if args[0] == 'cd':
        currentfolder = cmd.changedirectory(currentfolder, args[1])
