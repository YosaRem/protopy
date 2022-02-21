import struct


class EnumDecoder:
    def __init__(self, descriptor, to_decode_class=None):
        self.descriptor = descriptor
        self.class_instance = to_decode_class
        self.length = 4

    def declaim_field(self, string):
        value = self.get_value(string)
        self.set_value(value)
        return self.length

    def set_value(self, value):
        if self.class_instance is not None:
            self.class_instance.__setattr__(self.descriptor["name"], value)

    @staticmethod
    def get_value(string):
        return struct.unpack("!l", string[:4])[0]
