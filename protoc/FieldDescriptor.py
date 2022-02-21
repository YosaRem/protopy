from Exceptions import FieldNameException
import keyword


class FieldDescriptor:
    def __init__(self, message_name, specifying, field_type, name, index, subtypes=None, is_enum=False):
        self.message_name = message_name
        self.specifying = specifying
        self.field_type = field_type
        self.name = name
        self.check_name()
        self.index = index
        self.subtypes = subtypes if subtypes is not None else None
        self.is_enum = is_enum

    def __str__(self):
        result = '{{"name": "{name}", ' \
                 '"type": {type}, ' \
                 '"subtypes": {subtypes}, ' \
                 '"index": {index}, ' \
                 '"is_enum": {is_enum}}}'.format(name=self.name,
                                                 type=self.field_type,
                                                 index=self.index,
                                                 subtypes=self.subtypes,
                                                 is_enum=self.is_enum)
        return result

    def check_name(self):
        if self.name in keyword.kwlist:
            raise FieldNameException(self.message_name,
                                     description="This name is keyword for python",
                                     name=self.name)
        if not self.name[0].isalpha():
            raise FieldNameException(self.message_name,
                                     description="Name must start with alpha",
                                     name=self.name)
        if self.name.find("-") != -1:
            raise FieldNameException(self.message_name,
                                     description="Name can't contain '-'",
                                     name=self.name)



