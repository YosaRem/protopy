from .StrDecoder import StrDecoder
from .IntDecoder import IntDecoder
from .BoolDecoder import BoolDecoder
from .WireTypeChoicer import WireTypeChoicer


class MapDecoder:
    def __init__(self, descriptor, to_decode_class):
        self.descriptor = descriptor
        self.class_instance = to_decode_class
        types = self.descriptor["subtypes"]
        first_type = self.subtype_to_type(types[0])
        second_type = self.subtype_to_type(types[1])
        self.subtype_descriptor = {
            "first": {
                "name": "first",
                "index": 1,
                "type": first_type
            },
            "second": {
                "name": "second",
                "index": 2,
                "type": second_type
            }
        }

    def declaim_field(self, string):
        result_dict = {}
        wires = WireTypeChoicer.get_wires_types(descriptor=self.subtype_descriptor)
        i = 0
        dict_pare = self.DictPare()
        pare_count = 1
        while True:
            try:
                field = wires[bytes.fromhex(format(string[i], "02x"))]
            except Exception:
                break
            decoder = self.select_decoder(field)(self.subtype_descriptor[field], dict_pare)
            i += decoder.declaim_field(string[i + 1:]) + 2
            if pare_count % 2 == 0:
                result_dict[dict_pare.first] = dict_pare.second
                dict_pare = self.DictPare()
            pare_count += 1
        self.set_value(result_dict)
        return i - 1

    def set_value(self, value):
        self.class_instance.__setattr__(self.descriptor["name"], value)

    def select_decoder(self, field):
        if self.subtype_descriptor[field]["type"] is str:
            return StrDecoder
        if self.subtype_descriptor[field]["type"] is int:
            return IntDecoder
        if self.subtype_descriptor[field]["type"] is bool:
            return BoolDecoder
        if self.subtype_descriptor[field]["type"] is dict:
            return MapDecoder

    class DictPare:
        def __init__(self):
            self.first = False
            self.second = False

    @staticmethod
    def subtype_to_type(subtype):
        if subtype == "str":
            return str
        if subtype == "int":
            return int
        if subtype == "float":
            return float
        if subtype == "bool":
            return bool
