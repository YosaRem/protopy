import struct

class FloatDecoder:
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

    def get_value(self, string):
        return struct.unpack("!f", string[:4])[0]
