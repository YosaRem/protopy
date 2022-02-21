from unittest import TestCase
from decoder.BoolDecoder import BoolDecoder
from test.TestClass import TestClass


class BoolDecoderTest(TestCase):
    def setUp(self) -> None:
        self.descriptor = {"name": "bool_value", "type": bool, "index": 3}
        self.class_for_decode = TestClass()

    def test_if_true_for_decode(self):
        decoder = BoolDecoder(self.descriptor, self.class_for_decode)
        decoder.declaim_field("\x18\x01")
        self.assertEqual(self.class_for_decode.bool_value, True)
