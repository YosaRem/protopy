from unittest import TestCase
from encoder.ProtoEncoder import ProtoEncoder
from test.TestClass import TestClass


class BoolEncoderTest(TestCase):
    def setUp(self) -> None:
        self.class_for_decode = TestClass()

    def test_bool_true_encode(self):
        self.class_for_decode.bool_value = True
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b"\x18\x01!")

    def test_bool_false_encode(self):
        self.class_for_decode.bool_value = False
        decoder = ProtoEncoder(self.class_for_decode)
        result = decoder.encode_to_string()
        self.assertEqual(result, b"!")
