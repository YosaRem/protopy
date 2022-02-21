class UnsupportedSyntaxException(Exception):
    def __init__(self, syntax):
        self.text = "This syntax unsupported - " + syntax


class MessagesOverException(Exception):
    def __init__(self):
        self.text = "No more messages in file"


class UnknownWord(Exception):
    def __init__(self, word):
        self.text = "Unknown word - " + word


class IndexesRepeatedException(Exception):
    def __init__(self, message_name):
        self.text = "In '" + message_name + "' index was repeated"


class FieldNameException(Exception):
    def __init__(self, message_name, description="", name=None, duplicate=False):
        if duplicate:
            self.text = "In '" + message_name + "' duplicated names\n" + description
        else:
            self.text = "In '" + message_name + "' name = " \
                        + name + " is not allowed\n" + description
