from .BaseTypeEncoder import BaseTypeEncoder
from .BoolEncoder import BoolEncoder
from .IntEncoder import IntEncoder
from .StrEncoder import StrEncoder


class MapEncoder(BaseTypeEncoder):
    def get_encode(self) -> bytes:
        result = b""
        first_type = self.subtype_to_type(self.description["subtypes"][0])
        second_type = self.subtype_to_type(self.description["subtypes"][1])
        for key in self.value:
            result += self.encode_dict_value(key, first_type, 1)
            result += self.encode_dict_value(self.value[key], second_type, 2)
        return result

    def encode_dict_value(self, value, subtype, index):
        code = b""
        code += self.get_wire_type_bytes()

        descriptor = {
            "type": subtype,
            "index": index
        }
        if subtype is int:
            encoder = IntEncoder(descriptor, value)
            code += encoder.get_encode()
        if subtype is str:
            encoder = StrEncoder(descriptor, value)
            code += encoder.get_encode()
        if subtype is bool:
            encoder = BoolEncoder(descriptor, value)
            code += encoder.get_encode()
        return code

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
