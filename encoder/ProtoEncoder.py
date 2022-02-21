from Exception import WrongClassException
from IntEncoder import IntEncoder
from StrEncoder import StrEncoder
from BoolEncoder import BoolEncoder
from MapEncoder import MapEncoder
from FloatEncoder import FloatEncoder


class ProtoEncoder:
    def __init__(self, class_to_encode):
        self.to_encode = class_to_encode
        self.code = bytes()
        try:
            self.descriptor = self.to_encode.DESCRIPTOR
        except AttributeError:
            raise WrongClassException(type(self.to_encode).__name__)

    def encode_to_string(self):
        for field in self.descriptor:
            if self.descriptor[field]["is_enum"]:
                encoder = IntEncoder(self.descriptor[field], self.to_encode.__getattribute__(field).value)
            else:
                encoder = self._ENCODERS[self.descriptor[field]["type"]](self.descriptor[field],
                                                                         self.to_encode.__getattribute__(field))
            self.code += encoder.get_encode()
        return self.code

    _ENCODERS = {
        int: IntEncoder,
        str: StrEncoder,
        dict: MapEncoder,
        float: FloatEncoder,
        bool: BoolEncoder
    }
