#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '
    classes = ['BaseModel']

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

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""

        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = eval("{}()".format(arg[0]))
            print(obj.id)
            models.storage.save

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id"""

        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            try:
                obj = objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            try:
                obj = objs[key]
                objs.pop(key)
                del obj
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name"""

        arg = parse(line)
        objs = models.storage.all()
        obj_list = []
        if len(arg) >= 1:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, obj in objs.items():
                    if key.startswith(arg[0]):
                        obj_list.append(obj.__str__())
                print(obj_list)
        else:
            for obj in objs.values():
                obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""

        arg = parse(line)
        objs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            try:
                obj = objs[key]
                if len(arg) == 2:
                    print("** attribute name missing **")
                elif len(arg) == 3:
                    print("** value missing **")
                else:
                    try:
                        eval(arg[3])
                    except (SyntaxError, NameError):
                        arg[3] = "'{}'".format(arg[3])
                        setattr(obj, arg[2], eval(arg[3]))
                        obj.save()
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
