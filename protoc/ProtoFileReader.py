from Exceptions import UnsupportedSyntaxException, MessagesOverException
import re


class ProtoReader:
    def __init__(self, path_to_file):
        self.path = path_to_file

    def get_messages(self):
        with open(self.path, "r") as f:
            self.check_syntax_version(f.readline())
            while True:
                try:
                    yield self.extract_message(f)
                except MessagesOverException:
                    break

    @staticmethod
    def extract_message(file) -> list:
        bracket_count = None
        message_lines = []
        in_class_enum = {}
        message_name = ""
        is_enum = False
        in_enum = False
        enum_name = ""
        for i in file:
            res = re.search(r"[{}]", i)
            if not bool(res) and bracket_count is None:
                continue
            elif in_enum:
                string = i.strip()
                if bool(re.search("}", string)):
                    in_enum = False
                    bracket_count -= 1
                    continue
                if len(string) == 0:
                    continue
                in_class_enum[enum_name].append(string)
                continue
            elif not bool(res):
                string = i.strip()
                if len(string) == 0:
                    continue
                if string.startswith("//"):
                    continue
                message_lines.append(string)
            elif res.group() == "{" and bracket_count is None:
                bracket_count = 1
                message_name = i.split(" ")[1]
                if i.split(" ")[0] == "enum":
                    is_enum = True
            elif res.group() == "{":
                bracket_count += 1
                if i.strip().startswith("enum"):
                    enum_name = i.strip().split(" ")[1]
                    in_enum = True
                    in_class_enum[enum_name] = []
                    continue
            elif res.group() == "}":
                bracket_count -= 1
            if bracket_count == 0:
                break
        if bracket_count is None:
            raise MessagesOverException
        return message_name, message_lines, is_enum, in_class_enum

    @staticmethod
    def check_syntax_version(line):
        result = re.match(r'syntax = "proto3";', line)
        if not bool(result):
            raise UnsupportedSyntaxException(line)

