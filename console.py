#!/usr/bin/python3
"""
Module: console
"""
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import models
import shlex
from datetime import datetime
import cmd

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    """Console class using cmd"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """method to EOF"""
        return True

    def emptyline(self):
        """Empty line"""
        return False

    def helper_create(self, args):
        """ """
        new_dict = {}
        for arg in args:
            if "=" in arg:
                cut = arg.split('=', 1)
                key = cut[0]
                value = cut[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Create method"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return False
        else:
            if args[0] in classes:
                new_obj = self.helper_create(args[1:])
                newclass = classes[args[0]](**new_obj)
            else:
                print("** class doesn't exist **")
                return False
        print(newclass.id)
        newclass.save()

    def do_show(self, objs):
        """Show method"""
        args = shlex.split(objs)
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

    def do_destroy(self, objs):
        """Destroy method"""
        """Deletes an instance based on the class and id"""
        args = shlex.split(objs)
        argc = len(objs)

        if argc == 0:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        if argc > 1:
            k_value = str("{}.{}".format(args[0], args[1]))
            if k_value in storage.all():
                storage.all().pop(k_value)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, objs):
        """Prints string representations of instances"""
        args = shlex.split(objs)
        objs_lst = []
        if len(args) == 0:
            for value in models.storage.all().values():
                objs_lst.append(str(value))
            print("[", end="")
            print(", ".join(objs_lst), end="")
            print("]")
        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    objs_lst.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(objs_lst), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, objs):
        """Updates an instace based on class name and id"""
        args = shlex.split(objs)
        argc = len(objs)
        if argc == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if argc == 1:
            print("** instance id missing **")
        instance = storage.all()
        k_value = str("{}.{}".format(args[0], args[1]))
        if k_value in instance.keys():
            nu_obj = instance[k_value]
            if argc == 2:
                print("** attribue name missing **")
                return
            elif argc == 3:
                print("** value missing **")
                return
            else:
                nu_obj.__dict__[args[2]] = args[3][1:-1]
                nu_obj.updated_at = datetime.now()
                storage.save()
        else:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
