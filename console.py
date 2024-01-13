#!/usr/bin/python3
"""This is the entry point of the command interpreter.
"""


import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import os
import re
import json


class HBNBCommand(cmd.Cmd):
    """
    Operates on objects-storage_system via console,
        supports interactive and non-inter modes.
    """
    intro = """Welcome to the AirBnB CLI tool.
    ---Type help or ? to list commands.
    """
    ruler = "*"
    prompt = "(hbnb) "
    models = {"BaseModel": BaseModel,
              "User": User,
              "Amenity": Amenity,
              "City": City,
              "Review": Review,
              "State": State,
              "Place": Place
              }

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

    def precmd(self, line):
        """(precmd)
        special commands format support:

        Fomrat:
            <cls>.<cmd>(<potential args>)
        """
        l_match = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if not l_match:
            return line

        else:
            l_match = list(l_match.groups())
            _cmd, _cls, _args = l_match[1], l_match[0], l_match[2]

            if (
                len(l_match) <= 3 and
                len(l_match) > 1 and
                type(_args) is str and
                _cmd != "update"
            ):
                return f"{_cmd} {_cls} {_args}"
            else:
                d_match = re.search(r'{(.+)}', line)
                _args = _args.replace(",", "")
                _args = _args.split(" ")
                _id = _args[0][1:-1]
                if not d_match:
                    return (
                        f"{_cmd} {_cls} {_id} "
                        f"{_args[1][1:-1]} {_args[2]}"
                    )
                else:
                    d_args = "{" + d_match.group(1).replace("'", '"') + "}"
                    d_args = json.loads(d_args)

                    for i in d_args:
                        d_line = (
                            f"{_cmd} {_cls} {_id} {i} \"{d_args[i]}\""
                        )
                        self.onecmd(d_line)
                    return ""

    def help_precmd(self):
        print("""\n***Special command Sformat support:
        Format:
            <cls>.<cmd>(<potential args>)

        Ex:
            User.all()
            User.update("-id-", "name", "value")

        Type: '? <cmd>' for supported Sformat
        """)

    def do_clear(self, args):
        """Clear command similar to clear from shell"""
        os.system('clear')

    def do_create(self, args):
        """Creates a new instance of <class>,
            saves it (to the JSON file) and prints the id.
                Ex: $ create BaseModel
        """
        if not args:
            print("** class name missing **")
            return
        elif args not in self.models:
            print("** class doesn't exist **")
            return

        new_inst = self.models[args]()
        new_inst.save()
        print(new_inst.id)

    def help_create(self):
        print("\n[Usage]: create <className>\n")
        print("Creates a class of any type")
        print("Ex: $ create BaseModel\n")
        print("""Sformat:
        <class name>.show(<id>)""")

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
        elif name not in self.models:
            print("** class doesn't exist **")
            return
        elif not id:
            print("** instance id missing **")
            return

        session = storage.all()
        key = f"{name}.{id}"
        try:
            print()
            print(session[key], end='\n\n')
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        print("\n[Usage]: show <className> <id>\n")
        print("Show the 'str' representation of an instance")
        print("""Ex: $ show BaseModel 1234-1234-1234\n""")
        print("""Sformat:
        <class name>.show(<id>)""")

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
        elif name not in self.models:
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
        print("""Sformat:
        <class name>.destroy(<id>)""")

    def do_all(self, args):
        """Prints all string representation of all instances
            based or not on the class name.
                Ex: $ all BaseModel or $ all
        """
        str_rep = []
        if args:
            args = args.split(' ')[0]
            if args not in self.models:
                print("** class doesn't exist **")
                return
            for key, val in storage._FileStorage__objects.items():
                if key.split(".")[0] == args:
                    str_rep.append(str(val))
        else:
            for key, val in storage._FileStorage__objects.items():
                str_rep.append(str(val))
        print()
        print(str_rep, end='\n\n')

    def help_all(self):
        print("\n[Usage]: all [<className>]\n")
        print("Prints all instances string representations")
        print("Ex: $ all BaseModel or $ all\n")
        print("""Sformat:
        <class name>.all()""")

    def do_count(self, line):
        """retrieve the number of instances of a class
            Ex:
                <class name>.count()
        """
        if line not in self.models:
            print("** class doesn't exist **")
            return

        session = storage.all()
        i = 0
        for instance in session:
            if (session[instance].to_dict()["__class__"] == line):
                i += 1
        print(i)

    def help_count(self):
        print("""Retrieve the number of instances of a class
        \n[Usage]: <class name>.count()
        """)

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
        if args[0] not in self.models:
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
                    if args[3][0] == "\"" and args[3][-1] == "\"":
                        value_str = args[3][1:-1]
                    else:
                        value_str = args[3]

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
        print("""Sformat:
        <class name>.update(<id>, <attribute name>, <attribute value>)
        --or--
        <class name>.update(<id>, <dictionary representation>)""")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
