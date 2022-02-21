from BaseTypeEncoder import BaseTypeEncoder


class BoolEncoder(BaseTypeEncoder):
    def get_encode(self) -> bytes:
        result = b""
        value = self.encode_value()
        if value is None:
            return result
        result += self.get_wire_type_bytes()
        return result + self.encode_value()

    def encode_value(self):
        if self.value is False:
            return None
        return b"\x01"
