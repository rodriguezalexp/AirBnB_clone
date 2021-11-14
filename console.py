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

classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
            "City": City, "Place": Place, "Review": Review,
            "State": State}


class HBNBCommand(cmd.Cmd):
    """Console class using cmd"""

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

    def do_destroy(self, objs):
        """Destroy method"""
        """Deletes an instance based on the class and id"""
        args = objs.split()
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
        args = objs.split()
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
        args = objs.split()
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
