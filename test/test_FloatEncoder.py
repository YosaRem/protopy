from unittest import TestCase
from encoder.ProtoEncoder import ProtoEncoder
from test.TestClass import TestClass


class FloatEncoderTest(TestCase):
    def setUp(self) -> None:
        self.class_for_decode = TestClass()

    def test_zero(self):
        self.class_for_decode.float_value = 0.0
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b"!")

    def test_big_float(self):
        self.class_for_decode.float_value = 2000000000.0
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!N\xeek(')

    def test_float_with_big_after_point_part(self):
        self.class_for_decode.float_value = 20.120003103200103202
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!A\xa0\xf5\xc4')

    def test_negative_float(self):
        self.class_for_decode.float_value = -20.120003103200103202
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!\xc1\xa0\xf5\xc4')