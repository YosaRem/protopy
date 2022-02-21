class WrongClassException(Exception):
    def __init__(self, wrong_class):
        self.text = "Can't encode instance of this class - " + wrong_class
