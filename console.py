#!/usr/bin/python3
"""Imports"""
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_create(self, line):
        """Create a new instance"""

        args = line.split(' ')
        if args[0] == '':
            print("** class name missing **")
        elif len(args) > 1:
            kwargs = {}
            for idx in range(1, len(args)):
                subarg = args[idx].split('=')
                subarg[1] = subarg[1].replace('_', ' ')
                if '"' in subarg[1:]:
                    subarg[1] = subarg[1].replace('"', '\"')
                else:
                    subarg[1] = eval(subarg[1])
                kwargs.update(dict(zip(subarg[::2], subarg[1::2])))
            Class = HBNBCommand.classes.get(args[0])(**kwargs)
            Class.save()
            print(Class.id)
        elif len(args) == 1:
            if args[0] in HBNBCommand.classes:
                Class = HBNBCommand.classes.get(args[0])()
                Class.save()
                print(Class.id)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance
        """
        if line:
            args = line.split(' ')
            if args[0] in HBNBCommand.classes:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    objs = storage.all()
                    obj = "{}.{}".format(args[0], args[1])
                    if obj in objs.keys():
                        storage.delete(obj)
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, line):
        """Update a instance based on the class name
        """
        if line:
            args = line.split(' ')
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            elif args[0] in HBNBCommand.classes:
                objs = storage.all()
                obj = "{}.{}".format(args[0], args[1])
                if obj in objs.keys():
                    setattr(objs[obj], args[2], eval(args[3]))
                    objs[obj].save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, name):
        """Prints all instances
        """
        list_objs = []
        all_objs = list(storage.all().values())
        if name == "":
            for objs in all_objs:
                list_objs.append(str(objs))
            print(list_objs)
        elif name in HBNBCommand.classes:
            for objs in all_objs:
                if HBNBCommand.classes.get(name) is type(objs):
                    list_objs.append(str(objs))
            print(list_objs)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints a instance based on the class name
        """
        if line:
            args = line.split(' ')
            if args[0] in HBNBCommand.classes:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    objs = storage.all()
                    obj = "{}.{}".format(args[0], args[1])
                    if obj in objs.keys():
                        print(objs[obj])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program Ctrl+D
        """
        return True

    def emptyline(self):
        """emptyline do not execute before command"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
