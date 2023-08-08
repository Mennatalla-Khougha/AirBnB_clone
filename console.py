#!/usr/bin/python3
"""This program is for the console"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
