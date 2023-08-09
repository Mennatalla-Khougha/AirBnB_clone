#!/usr/bin/python3
"""This program is for the console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import shlex


allowed_classes = ["BaseModel", "User"]


def error(args):
    if not args:
        print("** class name missing **")
        return True

    if args[0] not in allowed_classes:
        print("** class doesn't exist **")
        return True

    if len(args) < 2:
        print(" ** instance id missing **")
        return True

    key = f"{args[0]}.{args[1]}"
    if key not in storage.all().keys():
        print("** no instance found **")
        return True
    return False


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF"""
        print()
        return True

    def do_help(self, arg):
        """Show help information"""
        super().do_help(arg)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, class_name):
        """Create a new instance of a given class."""
        if not class_name:
            print("** class name missing **")
            return
        if class_name in allowed_classes:
            obj = eval(class_name)()
            print(obj.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print string representation on the class"""
        args = arg.split()
        if error(args):
            return
        key = f"{args[0]}.{args[1]}"
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if error(args):
            return
        key = f"{args[0]}.{args[1]}"
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """" Prints all string representation of all instances"""
        lst = []
        if not arg:
            for value in storage.all().values():
                lst.append(str(value))
        elif arg not in allowed_classes:
            print("** class doesn't exist **")
            return
        else:
            for key, value in storage.all().items():
                if arg in key:
                    lst.append(str(value))
        print(lst)

    def do_update(self, arg):
        """" Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if error(args):
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        if args[2] in obj.__class__.__dict__.keys():
            att_type = type(obj.__class__.__dict__[args[2]])
            obj.__dict__[args[2]] = att_type(args[3])
        else:
            obj.__dict__[args[2]] = args[3]
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
