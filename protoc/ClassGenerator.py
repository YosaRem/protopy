from FieldsClassDescriptor import FieldsClassDescriptor
from ProtoFileReader import ProtoReader
from constants import DEFAULT_TYPE


class ClassGenerator:
    def __init__(self, path_to_file):
        self.path = path_to_file
        self.python_classes = ""

    def generate(self):
        self.python_classes += "from enum import Enum\n\n\n"
        reader = ProtoReader(self.path)
        custom_types = {}
        for name, message, is_enum, in_class_enum in reader.get_messages():
            custom_types[name] = name
            for k in in_class_enum.keys():
                custom_types[k] = k
        reader = ProtoReader(self.path)
        for name, message, is_enum, in_class_enum in reader.get_messages():
            if is_enum:
                self.add_outer_enum(name, message)
                continue
            if len(in_class_enum.keys()) > 0:
                self.add_inner_enum(in_class_enum)
            self.add_class_declaration(name)
            descriptor = FieldsClassDescriptor(name, message, custom_types, in_class_enum)
            descriptors = descriptor.get_class_descriptor()
            self.add_init(descriptors)
            self.add_descriptors(descriptor)
            self.descriptors_to_python(descriptors)
        return self.python_classes

    def add_inner_enum(self, in_class_enum):
        for e in in_class_enum.keys():
            self.python_classes += "class {}(Enum):\n".format(e)
            for l in in_class_enum[e]:
                self.python_classes += "    {0}\n".format(l[:-1])
            self.python_classes += "\n\n"

    def add_outer_enum(self, name, lines):
        self.python_classes += "class {0}(Enum):\n".format(name)
        for line in lines:
            self.python_classes += "    {0}\n".format(line[:-1])
        self.python_classes += "\n\n"

    def descriptors_to_python(self, descriptors):
        for desc in descriptors:
            self.python_classes += """
    @property
    def {0}(self):
        return self.__{0}
                
    @{0}.setter
    def {0}(self, {0}):
        {1}""".format(desc.name, self.build_field_constructor(desc))
        self.python_classes += "\n\n"

    def add_init(self, descriptors):
        self.python_classes += "    def __init__(self):\n"
        for desc in descriptors:
            if str(desc.field_type) in DEFAULT_TYPE:
                self.python_classes += "        self.{0} = {1}\n".format(desc.name,
                                                                         DEFAULT_TYPE[desc.field_type])
            else:
                self.python_classes += "        self.{0} = 0\n".format(desc.name)
        self.python_classes += "\n"

    def add_class_declaration(self, name):
        self.python_classes += "class {0}:\n".format(name)

    def add_descriptors(self, descriptor):
        self.python_classes += "    DESCRIPTOR = {{{0}}}".format(str(descriptor))

    def build_field_constructor(self, descriptor):
        res = ""
        if descriptor.is_enum:
            res = """if isinstance({0}, int):
            self.__{0} = {1}({0})
        elif not isinstance({0}, {1}):
            raise ValueError
        else:
            self.__{0} = {0}    
            """.format(descriptor.name, descriptor.field_type)
        else:
            res = """if not isinstance({0}, {1}):
            raise ValueError
        self.__{0} = {0}
            """.format(descriptor.name, descriptor.field_type)
        return res
