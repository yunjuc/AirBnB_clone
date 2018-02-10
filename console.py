#!/usr/bin/python3
import cmd
'''Command console interpreter'''


class HBNBCommand(cmd.Cmd):
    '''hbnb console'''
    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''Exit the program when end of file
        '''
        return True

    def emptyline(self):
        '''Do nothing with empty line + enter
        '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
