class BaseTypeEncoder:
    def __init__(self, description, value):
        self.description = description
        self.value = value

    def get_wire_type_bytes(self):
        return bytes.fromhex(format((self.description["index"] << 3) | self.get_wire(), "02X"))

    def get_wire(self):
        if "is_enum" in self.description and self.description["is_enum"]:
            return 0
        field_type = self.description["type"]
        if field_type in [int, bool]:
            return 0
        if field_type is float:
            return 1
        if field_type is str:
            return 2
        if field_type is dict:
            return 3
