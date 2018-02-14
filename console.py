#!/usr/bin/python3
'''Command console interpreter'''
import cmd
import models


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

    def do_create(self, line):
        '''Create a new instanac
        '''
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in models.cls_list) is False:
            print("** class doesn't exist **")
        else:
            cls_func = models.cls_list[arg[0]]
            new = cls_func()
            models.storage.save()
            print(new.id)

    def do_show(self, line):
        '''Display instance info based on class name and id
        '''
        arg = line.split()
        obj_list = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in models.cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[0] in models.cls_list and len(arg) == 1):
            print("** instance id missing **")
        elif (arg[0]+'.'+arg[1] in obj_list) is False:
            print("** no instance found **")
        else:
            print(obj_list[arg[0]+'.'+arg[1]])

    def do_destory(self, line):
        '''Delete instance based on class name and id
        '''
        arg = line.split()
        obj_list = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in models.cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[0] in models.cls_list and len(arg) == 1):
            print("** instance id missing **")
        elif (arg[0]+'.'+arg[1] in obj_list) is False:
            print("** no instance found **")
        else:
            del obj_list[arg[0]+'.'+arg[1]]
            models.storage.save()

    def do_all(self, line):
        '''Display all instances info based on class name
        '''
        arg = line.split()
        obj_list = models.storage.all()
        if len(arg) == 0:
            for k, v in obj_list.items():
                print(v)
        elif (arg[0] in models.cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[0] in models.cls_list):
            cls = models.cls_list[arg[0]]
            for k, v in obj_list.items():
                if cls == type(v):
                    print(v)

    def do_update(self, line):
        '''Update an instance based on class name and id with \
           attribute info.

           Usage: update <class name> <id> <attribute name> \
           "<attribute value>"
        '''
        arg = line.split()
        obj_list = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in models.cls_list) is False:
            print("** class doesn't exist **")
        elif arg[0] in models.cls_list:
            if len(arg) == 1:
                print("** instance id missing **")
            elif (arg[0]+'.'+arg[1] in obj_list) is False:
                print("** no instance found **")
            elif len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                obj = obj_list[arg[0]+'.'+arg[1]]
                setattr(obj, arg[2], arg[3])
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
