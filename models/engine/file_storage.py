#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import shlex


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage."""
        d = {}
        if not cls:
            return self.__objects
        dicts = self.__objects
        for key in dicts:
            s = shlex.split(key.replace('.', ' '))
            if (s[0] == cls.__name__):
                d[key] = self.__objects[key]
        return (d)

    def new(self, obj):
        """Add new key to the Objects dict."""
        self.__objects[
            f"{obj.__class__.__name__}.{obj.id}"
            ] = obj

    def save(self):
        """Save Objects dict into json file."""
        js = {}
        for key, value in self.__objects.items():
            js[key] = value.to_dict()
        self.jsons = json.dumps(js)
        self.jsonf = open(self.__file_path, 'w')
        print(self.jsons, file=self.jsonf)
        self.jsonf.close()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an existing element."""
        if not obj:
            return
        del self.__objects[f"{obj.__class__.__name__}.{obj.id}"]

    def close(self):
        """Close session."""
        self.reload()
