#!/usr/bin/python3
'''Command console interpreter'''
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    '''hbnb console'''
    prompt = '(hbnb) '
    cls_list = ['BaseModel', 'User', 'City', 'State', 'Place', 'Review',
                'Amenity']

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
            new = arg[0]()
            models.storage.save()
            print(new.id)

    def do_show(self, line):
        '''Display instance info based on class name and id
        '''
        arg = line.split()
        obj_list = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[1] is None):
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
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[1] is None):
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
            print("** class name missing **")
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        else:
            new_list = []
            if arg[0] is True:
                for k, v in obj_list.items():
                    if arg[0] = v('__class__'):
                        new_list.append(v)
            else:
                for k, v in obj_list.items:
                    new_list.append(v)
            print(new_list)

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
        elif (arg[0] in cls_list) is False:
            print("** class doesn't exist **")
        elif (arg[1] is None):
            print("** instance id missing **")
        elif (arg[0]+'.'+arg[1] in obj_list) is False:
            print("** no instance found **")
        elif (arg[2] is None):
            print("** attribute name missing **")
        elif (arg[3] is None):
            print("** value missing **")
        else:
            obj = obj_list[arg[0]+'.'+arg[1]]
            setattr(obj, arg[2], arg[3])
            models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
