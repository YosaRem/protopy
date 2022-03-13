from unittest import TestCase
from .TestClass import TestClass
from encoder.ProtoEncoder import ProtoEncoder
from decoder.ProtoDecoder import ProtoDecoder


class ProtoEncoderTest(TestCase):
    def setUp(self) -> None:
        self.class_for_encode = TestClass()

    def test_all_values_test(self):
        self.class_for_encode.str_value = "a"
        self.class_for_encode.int_value = 15
        self.class_for_encode.bool_value = True
        self.class_for_encode.dict_value = {
            "a": "b"
        }
        self.class_for_encode.dict_value2 = {
            1: "abc"
        }
        self.class_for_encode.float_value = -321.21
        self.class_for_encode.enum_cond = 0
        self.class_for_encode.enum_color = 2
        encoder = ProtoEncoder(self.class_for_encode)
        result = encoder.encode_to_string()
        self.assertEqual(
            result,
            b'\n\x01a\x10\x00\x00\x00\x0f\x18\x01!'
            b'\xc3\xa0\x9a\xe18\x00\x00\x00\x02C\n'
            b'\x01aC\x12\x01bK\x08\x00\x00\x00\x01K\x12\x03abc'
        )

    def test_last_value(self):
        self.class_for_encode.bool_value = True
        encoder = ProtoEncoder(self.class_for_encode)
        result = encoder.encode_to_string()
        self.assertEqual(result, b'\x18\x01!')

    def test_default_values(self):
        decoder = ProtoEncoder(self.class_for_encode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b'!')

    def test_encode_decode(self):
        float_value = -321.21
        self.class_for_encode.str_value = "a"
        self.class_for_encode.int_value = 15
        self.class_for_encode.bool_value = True
        self.class_for_encode.dict_value = {
            "a": "b"
        }
        self.class_for_encode.dict_value2 = {
            1: "abc"
        }
        self.class_for_encode.float_value = float_value
        self.class_for_encode.enum_cond = 0
        self.class_for_encode.enum_color = 2
        encoder = ProtoEncoder(self.class_for_encode)
        encoded = encoder.encode_to_string()
        decoder = ProtoDecoder(TestClass())
        result = decoder.decode_from_string(encoded)
        self.assertTrue(result.float_value - float_value < 0.0001)
        self.assertEqual(result.str_value, "a")
        self.assertEqual(result.bool_value, True)
        self.assertEqual(result.dict_value["a"], "b")
        self.assertEqual(result.int_value, 15)
        self.assertEqual(result.enum_cond.value, 0)
        self.assertEqual(result.enum_color.value, 2)
