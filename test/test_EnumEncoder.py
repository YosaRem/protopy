from unittest import TestCase
from encoder.ProtoEncoder import ProtoEncoder
from test.TestClass import *


class FloatEncoderTest(TestCase):
    def setUp(self) -> None:
        self.class_for_decode = TestClass()

    def test_one_enum(self):
        self.class_for_decode.enum_cond = COND.TRUE
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!0\x00\x00\x00\x01')
        self.class_for_decode.enum_cond = COND.FALSE
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!')

    def test_another_enum(self):
        self.class_for_decode.enum_color = COLOR.GREEN
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!8\x00\x00\x00\x02')

    def test_two_enum(self):
        self.class_for_decode.enum_color = COLOR.GREEN
        self.class_for_decode.enum_cond = COND.TRUE
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!0\x00\x00\x00\x018\x00\x00\x00\x02')
