from unittest import TestCase
from encoder.ProtoEncoder import ProtoEncoder
from test.TestClass import TestClass


class StrEncoderTest(TestCase):
    def setUp(self) -> None:
        self.class_for_decode = TestClass()

    def test_one_ascii_symbol(self):
        self.class_for_decode.str_value = "a"
        encoder = ProtoEncoder(self.class_for_decode)
        result = encoder.encode_to_string()
        self.assertEqual(result, b"\n\x01a!")

    def test_more_then_one_ascii_symbol(self):
        self.class_for_decode.str_value = "aaa"
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'\n\x03aaa!')

    def test_one_utf_symbol(self):
        self.class_for_decode.str_value = "ё"
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'\n\x02\xd1\x91!')

    def test_more_then_one_utf_symbol(self):
        self.class_for_decode.str_value = "ёё"
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'\n\x04\xd1\x91\xd1\x91!')
