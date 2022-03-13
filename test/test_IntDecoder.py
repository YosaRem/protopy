from unittest import TestCase
from decoder.IntDecoder import IntDecoder
from .TestClass import TestClass


class BoolDecoderTest(TestCase):
    def setUp(self) -> None:
        self.descriptor = {"name": "int_value", "type": int, "index": 3}
        self.class_for_decode = TestClass()

    def test_one_byte_int(self):
        decoder = IntDecoder(self.descriptor, self.class_for_decode)
        hex_value = b'\x00\x00\x00\x0f!'
        decoder.declaim_field(hex_value)
        self.assertEqual(self.class_for_decode.int_value, 15)

    def test_more_then_one_byte(self):
        decoder = IntDecoder(self.descriptor, self.class_for_decode)
        decoder.declaim_field(b'\x00\x00\x04\x00!')
        self.assertEqual(self.class_for_decode.int_value, 1024)
