from unittest import TestCase
from encoder.ProtoEncoder import ProtoEncoder
from .TestClass import TestClass


class MapEncoderTest(TestCase):
    def setUp(self) -> None:
        self.class_for_decode = TestClass()

    def test_str_str_dict(self):
        self.class_for_decode.dict_value = {
            "a": "b",
            "c": "d"
        }
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!C\n\x01aC\x12\x01bC\n\x01cC\x12\x01d')

    def test_int_str_dict(self):
        self.class_for_decode.dict_value2 = {
            13: "b",
            15: "d"
        }
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!K\x08\x00\x00\x00\rK\x12\x01bK\x08\x00\x00\x00\x0fK\x12\x01d')
