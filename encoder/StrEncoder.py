from BaseTypeEncoder import BaseTypeEncoder


class StrEncoder(BaseTypeEncoder):
    def get_encode(self) -> bytes:
        result = b""
        length = self.encode_length()
        if length is None:
            return result
        result += self.get_wire_type_bytes()
        result += length
        result += self.encode_value()
        return result

    def encode_value(self):
        value = b""
        for i in self.value:
            value += i.encode()
        return value

    def encode_length(self):
        length = len(self.value.encode())
        if length == 0:
            return None
        return bytes.fromhex(format(length, "02X"))

