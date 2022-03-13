from unittest import TestCase
from decoder.StrDecoder import StrDecoder
from .TestClass import TestClass


class BoolDecoderTest(TestCase):
    def setUp(self) -> None:
        self.descriptor = {"name": "str_value", "type": str, "index": 3}
        self.class_for_decode = TestClass()

    def test_one_ascii_symbol(self):
        decoder = StrDecoder(self.descriptor, self.class_for_decode)
        length = decoder.declaim_field(b"\x01a")
        self.assertEqual(length, 2)
        self.assertEqual(self.class_for_decode.str_value, "a")

    def test_more_then_one_ascii_symbol(self):
        decoder = StrDecoder(self.descriptor, self.class_for_decode)
        length = decoder.declaim_field(b"\x03aaa")
        self.assertEqual(length, 4)
        self.assertEqual(self.class_for_decode.str_value, "aaa")

    def test_one_utf_symbol(self):
        decoder = StrDecoder(self.descriptor, self.class_for_decode)
        length = decoder.declaim_field(b"\x02\xd1\x91")
        self.assertEqual(length, 3)
        self.assertEqual(self.class_for_decode.str_value, "ё")

    def test_more_then_one_utf_symbol(self):
        decoder = StrDecoder(self.descriptor, self.class_for_decode)
        length = decoder.declaim_field(b"\x06\xd1\x91\xd1\x91\xd1\x91")
        self.assertEqual(length, 7)
        self.assertEqual(self.class_for_decode.str_value, "ёёё")
