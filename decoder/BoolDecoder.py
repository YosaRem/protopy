class BoolDecoder:
    def __init__(self, descriptor, to_decode_class=None):
        self.descriptor = descriptor
        self.class_instance = to_decode_class

    def declaim_field(self, string):
        self.set_value(True)
        return 1

    def set_value(self, value):
        if self.class_instance is not None:
            self.class_instance.__setattr__(self.descriptor["name"], value)
