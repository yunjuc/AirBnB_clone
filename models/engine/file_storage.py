#!/usr/bin/python3
"""
FileStorage serializes and deserializes
"""


import json
import models

class FileStorage():
    """
    serializes and deserializes
    """

    __file_path = "file.json"
    __object = {}

    def all(self):
        """
        returns filestorage objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets __objects with key class name.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes objects to JSON
        """
        result = {}
        for k, v in self.__objects.items():
            result[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(result, file)

    def reload(self):
        """
        deserializes JSON file to __objects
        """
        
