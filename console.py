#!/usr/bin/python3
"""This is the entry point of the command interpreter.
"""


import cmd
from models.base_model import BaseModel
from models.user import User
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Operates on objects-storage_system via console,
        supports interactive and non-inter modes.
    """
    intro = """Welcome to the AirBnB CLI tool.
    ---Type help or ? to list commands.\n"""
    ruler = "*"
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel,
               "User": User}

    def emptyline(self):
        """Ignore emptyline inputs
        """
        pass

    def do_EOF(self, arg):
        """Exits the CLI
        """
        return True

    def help_EOF(self):
        print("\nType 'quit' to exit")
        print("---You can also press <C-d>\n")

    def do_quit(self, arg):
        """Exits the CLI
        """
        return True

    def help_quit(self):
        print("\nType 'quit' to exit")
        print("---You can also press <C-d>\n")

    def do_create(self, args):
        """Creates a new instance of <class>,
            saves it (to the JSON file) and prints the id.
                Ex: $ create BaseModel
        """
        if not args:
            print("** class name missing **")
            return
        elif args not in self.classes:
            print("** class doesn't exist **")
            return

        new_inst = self.classes[args]()
        new_inst.save()
        print(new_inst.id)

    def help_create(self):
        print("\n[Usage]: create <className>\n")
        print("Creates a class of any type")
        print("Ex: $ create BaseModel\n")

    def do_show(self, args):
        """Prints the string representation of an instance
            based on the class name and id.
                Ex: $ show BaseModel 1234-1234-1234
        """
        part = args.partition(" ")
        name = part[0]
        id = part[2]

        if not args:
            print("** class name missing **")
            return
        elif name not in self.classes:
            print("** class doesn't exist **")
            return
        elif not id:
            print("** instance id missing **")
            return

        session = storage.all()
        key = f"{name}.{id}"
        try:
            print(session[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        print("\n[Usage]: show <className> <id>\n")
        print("Show the 'str' representation of an instance")
        print("""Ex: $ show BaseModel 1234-1234-1234\n""")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
            and id (save the change into the JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234
        """
        part = args.partition(" ")
        name = part[0]
        id = part[2]

        if not args:
            print("** class name missing **")
            return
        elif name not in self.classes:
            print("** class doesn't exist **")
            return
        elif not id:
            print("** instance id missing **")
            return

        session = storage.all()
        key = f"{name}.{id}"
        try:
            del session[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        print("\n[Usage]: destroy <className> <id>\n")
        print("Deletes an existing instance")
        print("Ex: $ destroy BaseModel 1234-1234-1234\n")

    def do_all(self, args):
        """Prints all string representation of all instances
            based or not on the class name.
                Ex: $ all BaseModel or $ all
        """
        str_rep = []
        if args:
            args = args.split(' ')[0]
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            for key, val in storage._FileStorage__objects.items():
                if key.split(".")[0] == args:
                    str_rep.append(str(val))
        else:
            for key, val in storage._FileStorage__objects.items():
                str_rep.append(str(val))
        print(str_rep)

    def help_all(self):
        print("\n[Usage]: all [<className>]\n")
        print("Prints all instances string representations")
        print("Ex: $ all BaseModel or $ all\n")

    def do_update(self, line):
        """Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) >= 1:
            if len(args) < 2:
                print("** instance id missing **")
                return
            elif len(args) < 3:
                print("** attribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return
            else:
                try:
                    session = storage.all()
                    key = f"{args[0]}.{args[1]}"
                    name = args[2]
                    value_str = args[3][1:-1]
                    if re.match(r"^\d+$", value_str):
                        value = int(value_str)
                    elif re.match(r"^\d+\.\d+$", value_str):
                        value = float(value_str)
                    else:
                        value = value_str
                    setattr(session[key], name, value)
                    storage.save()

                except KeyError:
                    print("** no instance found **")

    def help_update(self):
        print("\n[Usage]: update <class name> <id> " +
              """<attribute name> "<attribute value>"\n""")
        print("Updates an instance based on the class name and id")
        print("Ex: $ update BaseModel 1234-1234-1234 " +
              """email "aibnb@mail.com"\n""")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
