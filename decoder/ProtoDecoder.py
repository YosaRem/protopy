from .WireTypeChoicer import WireTypeChoicer
from .StrDecoder import StrDecoder
from .IntDecoder import IntDecoder
from .BoolDecoder import BoolDecoder
from .MapDecoder import MapDecoder
from .FloatDecoder import FloatDecoder
from .EnumDecoder import EnumDecoder


class ProtoDecoder:
    def __init__(self, instance_class):
        self.to_result_class = instance_class
        self.descriptor = instance_class.DESCRIPTOR

    def decode_from_string(self, string):
        wires = WireTypeChoicer.get_wires_types(self.descriptor)
        i = 0
        while i < len(string):
            field = wires[bytes.fromhex(format(string[i], "02x"))]
            decoder = self.select_decoder(field)(self.descriptor[field], self.to_result_class)
            i += decoder.declaim_field(string[i + 1:]) + 1
        return self.to_result_class

    def select_decoder(self, field):
        if self.descriptor[field]["is_enum"]:
            return EnumDecoder
        if self.descriptor[field]["type"] is str:
            return StrDecoder
        if self.descriptor[field]["type"] is int:
            return IntDecoder
        if self.descriptor[field]["type"] is bool:
            return BoolDecoder
        if self.descriptor[field]["type"] is float:
            return FloatDecoder
        if self.descriptor[field]["type"] is dict:
            return MapDecoder
