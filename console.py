#!/usr/bin/python3
"""
The console, to manage everything
"""


import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class HBNB to read command """
    prompt = '(hbnb) '
    __all_1 = 0

    def empty_line(self):
        """ Pass if no command is given """
        pass

    def precmd(self, line):
        """ Edit given command to allow second type of input """

        if not sys.stdin.isatty():
            print()
        if '.' in line:
            HBNBCommand.__all_1 = 1
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            cmd_argvs = line.split()
            cmd_argvs[0], cmd_argvs[1] = cmd_argvs[1], cmd_argvs[0]
            line = " ".join(cmd_argvs)
        return cmd.Cmd.precmd(self, line)

    def quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print()
        return True

    def create(self, arg):
        """" Create an instance if the Model exists """

        if not arg:
            print("** class name missing **")
            return None
        try:
            my_model = eval(arg + "()")
            my_model.save()
            print(my_model.id)
        except Exception:
            print("** class doesn't exist **")

    def show(self, arg):
        """ Print dict of a instance in base of it's ID """

        cmd_argvs = arg.split()
        if not cmd_argvs:
            print("** class name missing **")
            return None
        try:
            eval(cmd_argvs[0])
        except Exception:
            print("** class doesn't exist **")
            return None

        all_objects = storage.all()

        if len(cmd_argvs) < 2:
                print("** instance id missing **")
                return None

        cmd_argvs[1] = cmd_argvs[1].replace("\"", "")
        key = cmd_argvs[0] + '.' + cmd_argvs[1]

        if all_objects.get(key, False):
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Print all the instances saved in file.json """

        cmd_argvs = arg.split()

        if cmd_argvs:
            try:
                eval(cmd_argvs[0])
            except Exception:
                print("** class doesn't exist **")
                return None

        all_objects = storage.all()
        print_list = []
        len_objs = len(all_objects)
        for key, value in all_objects.items():
            if not cmd_argvs:
                if HBNBCommand.__all_1 == 0:
                    print_list.append("\"" + str(value) + "\"")
                else:
                    print_list.append(str(value))
            else:
                checker = key.split('.')
                if cmd_argvs[0] == checker[0]:
                    if HBNBCommand.__all_1 == 0:
                        print_list.append("\"" + str(value) + "\"")
                    else:
                        print_list.append(str(value))
        print("[", end="")
        print(", ".join(print_list), end="")
        print("]")

    def destroy(self, arg):
        """
        Deletes an instance based on it's ID and save the changes\n \
        Usage: destroy <class name> <id>
        """

        cmd_argvs = arg.split()
        if not cmd_argvs:
            print("** class name missing **")
            return None
        try:
            eval(cmd_argvs[0])
        except Exception:
            print("** class doesn't exist **")
            return None

        all_objects = storage.all()

        if len(cmd_argvs) < 2:
                print("** instance id missing **")
                return None

        cmd_argvs[1] = cmd_argvs[1].replace("\"", "")
        key = cmd_argvs[0] + '.' + cmd_argvs[1]

        if all_objects.get(key, False):
            all_objects.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def update(self, arg):
        """ Usage: update <class name> <id> <attribute name> <attribute value> """

        cmd_argvs = []
        part2_argvs = []
        is_dict = 0
        if "\"" in arg:
            if "," in arg:
                if "{" in arg:
                    is_dict = 1
                    part1_argvs = arg.split(",")[0].split()
                    for n in part1_argvs:
                        cmd_argvs.append(n.replace("\"", ""))
                    part2_argvs = arg.replace("}", "").split("{")[1].split(", ")
                    for n in part2_argvs:
                        for t in n.split(": "):
                            cmd_argvs.append(t.replace("\"", "")
                                            .replace('\'', ""))
                else:
                    arg_key = arg.replace(",", "")
                    part1_argvs = arg_key.split()
                    for n in part1_argvs[:2]:
                        cmd_argvs.append(n.replace("\"", ""))
                    part2_argvs = arg.split(", ")[1:]
                    for n in part2_argvs:
                        cmd_argvs.append(n.replace("\"", ""))
            else:
                part1_argvs = arg.split("\"")[0]
                for n in part1_argvs.split():
                    cmd_argvs.append(n)
                part2_argvs = arg.split("\"")[1:]
                for n in part2_argvs:
                    if n != " " and n != "":
                        cmd_argvs.append(n.replace("\"", ""))

        else:
            part1_argvs = arg.split()
            for n in range(len(part1_argvs)):
                if n == 4:
                    break
                cmd_argvs.append(part1_argvs[n])

        if (len(cmd_argvs) == 0):
            print("** class name missing **")
            return None

        try:
            eval(cmd_argvs[0])
        except Exception:
            print("** class doesn't exist **")
            return None

        if len(cmd_argvs) < 2:
            print("** instance id missing **")
            return None

        all_objects = storage.all()

        key = cmd_argvs[0] + '.' + cmd_argvs[1]
        if all_objects.get(key, False):
            if (len(cmd_argvs) >= 3):
                if (len(cmd_argvs) % 2) == 0:
                    for n in range(2, len(cmd_argvs), 2):
                        attr = cmd_argvs[n]
                        type_att = getattr(all_objects[key], cmd_argvs[n], "")
                        try:
                            cast_val = type(type_att)(cmd_argvs[n + 1])
                        except Exception:
                            cast_val = type_att
                        setattr(all_objects[key], cmd_argvs[n], cast_val)
                        all_objects[key].save()
                        if is_dict == 0:
                            break
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")
        else:
            print("** no instance found **")

    def counter(self, arg):
        """ Usage: counter <class name> or <class name>.counter() """

        cmd_argvs = arg.split()

        if cmd_argvs:
            try:
                eval(cmd_argvs[0])
            except Exception:
                print("** class doesn't exist **")
                return None

        all_objects = storage.all()
        counter = 0

        for key, value in all_objects.items():
            if not cmd_argvs:
                counter += 1
            else:
                checker = key.split('.')
                if cmd_argvs[0] == checker[0]:
                    counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
