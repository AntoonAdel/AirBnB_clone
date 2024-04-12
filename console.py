#!/usr/bin/python3
"""
The console, to manage everything
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Contains functionality of the console"""

    intro = 'Welcome to the interpreter! Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def creation(self, line):
        """Creates a new object"""

        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.__class__.classes[line]()
            obj.save()
            print(obj.id)

    def showing(self, line):
        """
        Prints the string representation of an instance
        Args:
            line -> Class id ( In that order)
        """

        class_object = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif class_object[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(class_object) == 1:
            print("** instance id missing **")
            return
        else:
            key = class_object[0] + "." + class_object[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key]
                print(str(obj))

    def updating(self, line):
        """Updates attributes of an object"""
        updates = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif updates[0] not in __class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(updates) == 1:
            print("** instance id missing **")
            return
        elif len(updates) == 2:
            print("** attribute name missing **")
        elif len(updates) == 3:
            print("** value missing **")
        else:
            key = updates[0] + "." + updates[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key]
                setattr(obj, updates[2], updates[3])
                storage.save()

    def destruction(self, args):
        """ Destroys an object based on the Class Name and ID """

        target_list = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        elif target_list[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(target_list) == 1:
            print("** instance id missing **")
            return
        else:
            key = target_list[0] + "." + target_list[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                del all_instances[key]
                storage.save()

    def do_all(self, line):
        """ Print string representation of all instances """

        object_list = []
        objs = storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, val in objs.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(objs[key])
                    object_list.append(val)
            else:
                val = str(objs[key])
                object_list.append(val)
        print(object_list)

    def empty_line(self):
        """ Overwrite default behavior to repeat last cmd """
        pass

    def do_operations(self, args):
        """ Do operations on objects """

    def do_EOF(self, args):
        """ Handles EOF to exit program """
        print()
        return True

    def quit(self, args):
        """ Quits the interpreter """
        raise SystemExit

    def counter(self, args):
        """ Count all instances of a class """
        to_count = args.split(" ")
        instances = 0
        for object_ in models.storage.all().values():
            if to_count[0] == type(object_).__name__:
                instances += 1
        print(instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
