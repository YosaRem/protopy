from typing import Tuple

from constants import SINGULAR, REPEATED, SCALAR_VALUE, CUSTOM
from Exceptions import UnknownWord, IndexesRepeatedException, FieldNameException
from FieldDescriptor import FieldDescriptor
import re


HAVE_SPECIFYING = True


class FieldsClassDescriptor:
    def __init__(self, message_name, message, custom_types, in_class_enum):
        self.in_class_enum = in_class_enum
        self.custom_types = custom_types
        self.message_name = message_name
        self.message = message

    def __str__(self):
        result = ""
        for i in self.get_fields_descriptors():
            result += '"{name}": {descriptor}, \n'.format(name=i.name,
                                                          descriptor=str(i))
        return result

    def get_class_descriptor(self):
        descriptors = self.get_fields_descriptors()
        self.check_fields(descriptors)
        return descriptors

    def get_fields_descriptors(self):
        descriptors = []
        for field in self.message:
            descriptors.append(self.get_field_descriptor(field))
        return descriptors

    def get_field_descriptor(self, string) -> FieldDescriptor:
        map_descriptor, is_map = self.map_descriptor(string)
        if is_map:
            return map_descriptor
        tokens = string.split()
        position = 0
        is_enum = False
        specify, have_specify = self.get_specifying_field(tokens[position], self.custom_types)
        if specify == CUSTOM:
            is_enum = True
        if have_specify:
            position += 1
        field_type = self.get_type(tokens[position], self.custom_types)
        position += 1
        name = tokens[position]
        index = self.get_index(tokens[-1])
        return FieldDescriptor(self.message_name, specify, field_type, name, index, is_enum=is_enum)

    def map_descriptor(self, string) -> Tuple[FieldDescriptor, bool]:
        types = re.search(r"map<([\w ,]*?)>", string)
        if types is None:
            return None, False
        types = types[1].split(",")
        types_result = []
        for t in types:
            types_result.append(self.get_type(t.strip(), self.custom_types))
        types = types_result
        tokens = string.split(" ")
        index = self.get_index(tokens[-1])
        return FieldDescriptor(
            message_name=self.message_name,
            specifying="",
            field_type="dict",
            subtypes=types,
            name=tokens[-3],
            index=index
        ), True

    def check_fields(self, descriptors):
        self.check_names([i.name for i in descriptors])
        self.check_indexes([i.index for i in descriptors])

    def check_names(self, names):
        if len(names) != len(set(names)):
            raise FieldNameException(self.message_name, duplicate=True)

    def check_indexes(self, indexes):
        if len(indexes) != len(set(indexes)):
            raise IndexesRepeatedException(self.message_name)

    @staticmethod
    def get_index(token):
        token = token.strip(";")
        try:
            int(token)
        except ValueError:
            raise UnknownWord("index = " + token)
        return token

    @staticmethod
    def get_specifying_field(token, custom_types):
        if token == REPEATED:
            return REPEATED, HAVE_SPECIFYING
        if token == SINGULAR:
            return SINGULAR, HAVE_SPECIFYING
        if token in SCALAR_VALUE:
            return SINGULAR, not HAVE_SPECIFYING
        if token in custom_types:
            return CUSTOM, not HAVE_SPECIFYING
        raise UnknownWord(token)

    @staticmethod
    def get_type(token, custom_types):
        try:
            return SCALAR_VALUE[token]
        except KeyError:
            if token in custom_types:
                return custom_types[token]
            else:
                raise UnknownWord(token)
