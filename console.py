#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        print()
        return True

    def empty_line(self):
        """Executes nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
