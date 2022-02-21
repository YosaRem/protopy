from ClassGenerator import ClassGenerator


class FileGenerator:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        path = path_to_file.split(".")[0]
        self.path_where_create = path + "_gen.py"

    def start(self):
        gen = ClassGenerator(self.path_to_file)
        self._write_to_file(gen.generate())

    def _write_to_file(self, classes):
        with open(self.path_where_create, "w") as f:
            f.write(classes)
