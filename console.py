#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
'''Command console interpreter'''


class HBNBCommand(cmd.Cmd):
    '''hbnb console'''
    prompt = '(hbnb) '
    cls_list = ['BaseModel']

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

    def do_create(self, line):
        '''Create a new instanac
        '''
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        else:
            new = BaseModel(0) # replace with save to file later
            print(new.id)

    def do_show(self, line):
        '''Display instance info based on class name and id
        '''
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[1] is None):
            print("** instance id missing **")
        elif (arg[1] in json_file) is False:  # replace json_file
            print("** no instance found **")
        else:
            for i in json_file: # replace json_file
                print(i.id)

   def do_destory(self, line):
       '''Delete instance based on class name and id
       '''
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[1] is None):
            print("** instance id missing **")
        elif (arg[1] in json_file) is False:  # replace json_file
            print("** no instance found **")
        else:
            for i in json_file: # replace json_file
                del(i.id)       # check how to delete

    def do_all(self, line):   
        '''Display all instances info based on class name
        '''
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        else:
            for i in json_file: # replace json_file
                print(i.id)

    def do_update(self, line):
        '''Update an instance based on class name and id with \
           attribute info
        '''
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[1] is None):
            print("** instance id missing **")
        elif (arg[1] in json_file) is False:  # replace json_file
            print("** no instance found **")
        elif (arg[2] is None):
            print("** attribute name missing **")
        elif (arg[3] is None):
            print("** value missing **")
        else:
            # update json_file

if __name__ == '__main__':
    HBNBCommand().cmdloop()
