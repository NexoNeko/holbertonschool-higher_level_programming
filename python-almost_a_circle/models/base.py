#!/usr/bin/python3
""" Defines the base class """


class Base:
    """ Base instance for future objects
    Manages IDs. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Rturns the JSON of a list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ Writes the JSON of an object list to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the deserealized JSON string """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns a class from a dict of attribs """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                nushape = cls(1, 1)
            else:
                nushape = cls(1)
            nushape.update(**dictionary)
            return nushape

    @classmethod
    def load_from_file(cls):
        """ Returns a list of classes from a JSON file
        containing strings """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
