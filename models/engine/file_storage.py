#!/usr/bin/python3
"""
FileStorage serializes and deserializes
"""
import json
import models


class FileStorage:
    """
    Serializes and deserializes
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return filestorage objects
        """
        return self.__objects

    def new(self, obj):
        """
        Set __objects with key class name.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes objects to JSON
        """
        result = {}
        for k, v in self.__objects.items():
            result[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(result, f)

    def reload(self):
        """
        Deserialize JSON file to __object
        """
        try:
            with open(self.__file_path) as f:
                j_dict = json.load(f)
            for k, v in j_dict.items():
                cls_str = v['__class__']
                cls_func = models.cls_list[cls_str]
                self.__objects[k] = cls_func(**v)
        except FileNotFoundError as e:
            pass
