import struct
from BaseTypeEncoder import BaseTypeEncoder


class FloatEncoder(BaseTypeEncoder):
    def get_encode(self) -> bytes:
        result = b""
        result += self.get_wire_type_bytes()
        if self.value == 0:
            return result
        return result + struct.pack("!f", self.value)
