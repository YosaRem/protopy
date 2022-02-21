class StrDecoder:
    def __init__(self, descriptor, to_decode_class=None):
        self.descriptor = descriptor
        self.class_instance = to_decode_class

    def declaim_field(self, string):
        length = self.get_length_str(string[0])
        value = self.get_value(string[1:], length)
        self.set_value(value)
        return length + 1

    def set_value(self, value):
        if self.class_instance is not None:
            self.class_instance.__setattr__(self.descriptor["name"], value)

    @staticmethod
    def get_value(string, length):
        result = string[:length]
        return result.decode()

    @staticmethod
    def get_length_str(length_byte):
        return int(str(length_byte))
