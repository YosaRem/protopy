from unittest import TestCase
from .TestClass import TestClass
from encoder.ProtoEncoder import ProtoEncoder


class IntEncoderTest(TestCase):
    def setUp(self) -> None:
        self.class_for_decode = TestClass()

    def test_one_byte_int(self):
        self.class_for_decode.int_value = 15
        encoder = ProtoEncoder(self.class_for_decode)
        result = encoder.encode_to_string()
        self.assertEqual(result, b'\x10\x00\x00\x00\x0f!')

    def test_more_then_one_byte(self):
        self.class_for_decode.int_value = 1024
        encoder = ProtoEncoder(self.class_for_decode)
        result = encoder.encode_to_string()
        self.assertEqual(result, b'\x10\x00\x00\x04\x00!')

    def test_negative(self):
        self.class_for_decode.int_value = -1
        self.class_for_decode.int_value2 = -100000
        encoder = ProtoEncoder(self.class_for_decode)
        result = encoder.encode_to_string()
        self.assertEqual(result, b'\x10\xff\xff\xff\xff!(\xff\xfey`')
