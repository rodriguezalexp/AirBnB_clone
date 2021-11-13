#!/usr/bin/python3
""""""
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import models
import shlex

classes = {"BaseModel"}


class HBNBCommand(cmd.Cmd):
    """"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """method to EOF"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, objs):
        """Create method"""
        args = objs.split()
        argc = len(objs)
        if argc == 0:
            print("** class name missing **")
        else:
            if args[0] in classes:
                newclass = classes[args[0]]()
                newclass.save()
                print(newclass.id)

            else:
                print("** class doesn't exist **")

    def do_show(self, objs):
        """Show method"""
        args = objs.split()
        argc = len(objs)
        if argc == 0:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif argc == 1:
            print("** instance id missing **")
            return
        __objects = storage.all()
        k_value = str("{}.{}".format(args[0], args[1]))
        if k_value in __objects.keys():
            print(__objects[k_value])
        else:
            print("** no instance found **")

    def do_destroy(self):
        """Destroy method"""
        pass

    def do_all(self):
        """Prints all string representation of all
        instances based or not on the class name"""
        pass

    def do_update(self):
        """Updates an instace based on class name and id"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
