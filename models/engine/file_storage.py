#!/usr/bin/python3
"""
The main Storage engine for files, .JSON format
"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances

    Attrs: (private-class)
        __file_path: string - path to the JSON file (ex: file.json)

        __objects: dictionary - empty but will store all objects
            by <class name>.id
    Methods:
        all(self): returns the dictionary __objects

        new(self, obj): sets in __objects the obj with key <obj class name>.id

        save(self): serializes __objects to the JSON file (path: __file_path)

        reload(self): deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists)
    """

    __file_path = "AirBnB_storage.json"
    __objects = {}

    def all(self):
        """Return dictionary of __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets new __objects
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves __objects to __file_path
        """
        objs = {}
        for key, value in self.__objects.items():
            objs[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objs, f)

    def reload(self):
        """Loads __objects from __file_path
        """
        try:
            with open(self.__file_path, "r") as f:
                objs = json.load(f)

            for key, value in objs.items():
                class_name = key.split(".")[0]
                class_obj = globals().get(class_name)
                if class_obj is not None:
                    instance = class_obj(**value)
                    self.new(instance)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error reloading data: {e}")
