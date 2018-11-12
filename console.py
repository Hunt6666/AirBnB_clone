#!/usr/bin/python3
"""Module for the console"""
import cmd
import json
import os
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """comand line prompt for air bnb"""
    models = ["BaseModel", "User"]

    def do_update(self, line):
        """Updates an instance by add ing or updating an attribute
        Args:
            line: line argument
        """

        """ Need add More once More models exist"""
        args = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = storage.all()
            key = args[0] + '.' + args[1]
            if key in dic:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    """ actual update"""
                    dictionary = dic[key].to_dict()
                    string = args[3][1:-1]
                    if args[2] == "name":
                        dictionary[args[2]] = str(string)
                    else:
                        dictionary[args[2]] = int(string)
                    """ change once mode models exist"""
                    new = BaseModel(**dictionary)
                    new.save()
            else:
                print("** no instance found **")

    def do_show(self, line):
        """Shows a given Model
        Args:
            line: command line
        """
        """ Need Work once more models made"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] in HBNBCommand.models:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    dic = storage.all()
                    ins_id = args[0] + '.' + args[1]
                    if ins_id in dic:
                        print(dic[ins_id])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints All Insteses of Spacific Model Type
        Args:
            line: command line
        """
        """Add More Once more Models added"""
        if len(line) == 0 or line in HBNBCommand.models:
            dic = {}
            dic = storage.all().copy()
            lst = []
            for k in dic.keys():
                lst.append(str(dic[k]))
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes a Spacific Object
        Args:
            line: Command line
        """
        """Add Mode Once More Models added"""
        args = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dic = storage.all()
            inst = args[0] + '.' + args[1]
            if inst in dic:
                dic.pop(inst)
                storage.save()
            else:
                print("** no instance found **")

    def do_create(self, line):
        """Creates a new Model
        Args:
            line: command line
        """
        if line == "BaseModel":
            new = BaseModel()
        elif line == "User":
            new = User()
        elif len(line) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
        new.save()
        print(new.id)

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """simply clicking enter goes to next line
        with prompt no other print"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd(self.lastcmd)

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(HBNB) '
    prompt.cmdloop('')
