from unittest import TestCase
from protoc.ClassGenerator import ClassGenerator


class FileGenerationTest(TestCase):
    def test_file_generator(self):
        def filter_empty_string(line):
            if line == "":
                return False
            else:
                return True
        generator = ClassGenerator("book.proto")
        file = generator.generate()
        with open("TestClass.py", "r") as f:
            file_lines = filter(filter_empty_string, map(str.strip, f.readlines()))
            generated_lines = filter(filter_empty_string, map(str.strip, file.split("\n")))
            self.assertEqual("".join(file_lines), "".join(generated_lines))

