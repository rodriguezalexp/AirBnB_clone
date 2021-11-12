#!/usr/bin/python3
""""""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        """Create method"""
        shlex.split(line)

    def do_show(self, obj):
        """Show method"""
        if obj is not None:
            self.__objects.update(
                {"{}.{}\
".format(obj.__class__.__name__, obj.id): obj})

    def do_destroy(self):
        """Destroy method"""
        pass

    def do_all(self):
        """Prints all string representation of all
        instances based or not on the class name"""
        pass

    def do_update(self):
        """Updates an instace based on class name and id"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
