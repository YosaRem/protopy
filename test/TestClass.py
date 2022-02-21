from enum import Enum


class COND(Enum):
    FALSE = 0
    TRUE = 1


class A:
    def __init__(self):
        self.name = ""
        self.age = 0

    DESCRIPTOR = {"name": {"name": "name", "type": str, "subtypes": None, "index": 1, "is_enum": False}, 
"age": {"name": "age", "type": int, "subtypes": None, "index": 2, "is_enum": False}, 
}
    @property
    def name(self):
        return self.__name
                
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError
        self.__name = name
            
    @property
    def age(self):
        return self.__age
                
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError
        self.__age = age
            

class COLOR(Enum):
    BLACK = 0
    WHITE = 1
    GREEN = 2


class TestClass:
    def __init__(self):
        self.str_value = ""
        self.int_value = 0
        self.bool_value = False
        self.float_value = 0.0
        self.int_value2 = 0
        self.enum_cond = 0
        self.enum_color = 0
        self.dict_value = {}
        self.dict_value2 = {}

    DESCRIPTOR = {"str_value": {"name": "str_value", "type": str, "subtypes": None, "index": 1, "is_enum": False}, 
"int_value": {"name": "int_value", "type": int, "subtypes": None, "index": 2, "is_enum": False}, 
"bool_value": {"name": "bool_value", "type": bool, "subtypes": None, "index": 3, "is_enum": False}, 
"float_value": {"name": "float_value", "type": float, "subtypes": None, "index": 4, "is_enum": False}, 
"int_value2": {"name": "int_value2", "type": int, "subtypes": None, "index": 5, "is_enum": False}, 
"enum_cond": {"name": "enum_cond", "type": COND, "subtypes": None, "index": 6, "is_enum": True}, 
"enum_color": {"name": "enum_color", "type": COLOR, "subtypes": None, "index": 7, "is_enum": True}, 
"dict_value": {"name": "dict_value", "type": dict, "subtypes": ['str', 'str'], "index": 8, "is_enum": False}, 
"dict_value2": {"name": "dict_value2", "type": dict, "subtypes": ['int', 'str'], "index": 9, "is_enum": False}, 
}
    @property
    def str_value(self):
        return self.__str_value
                
    @str_value.setter
    def str_value(self, str_value):
        if not isinstance(str_value, str):
            raise ValueError
        self.__str_value = str_value
            
    @property
    def int_value(self):
        return self.__int_value
                
    @int_value.setter
    def int_value(self, int_value):
        if not isinstance(int_value, int):
            raise ValueError
        self.__int_value = int_value
            
    @property
    def bool_value(self):
        return self.__bool_value
                
    @bool_value.setter
    def bool_value(self, bool_value):
        if not isinstance(bool_value, bool):
            raise ValueError
        self.__bool_value = bool_value
            
    @property
    def float_value(self):
        return self.__float_value
                
    @float_value.setter
    def float_value(self, float_value):
        if not isinstance(float_value, float):
            raise ValueError
        self.__float_value = float_value
            
    @property
    def int_value2(self):
        return self.__int_value2
                
    @int_value2.setter
    def int_value2(self, int_value2):
        if not isinstance(int_value2, int):
            raise ValueError
        self.__int_value2 = int_value2
            
    @property
    def enum_cond(self):
        return self.__enum_cond
                
    @enum_cond.setter
    def enum_cond(self, enum_cond):
        if isinstance(enum_cond, int):
            self.__enum_cond = COND(enum_cond)
        elif not isinstance(enum_cond, COND):
            raise ValueError
        else:
            self.__enum_cond = enum_cond    
            
    @property
    def enum_color(self):
        return self.__enum_color
                
    @enum_color.setter
    def enum_color(self, enum_color):
        if isinstance(enum_color, int):
            self.__enum_color = COLOR(enum_color)
        elif not isinstance(enum_color, COLOR):
            raise ValueError
        else:
            self.__enum_color = enum_color    
            
    @property
    def dict_value(self):
        return self.__dict_value
                
    @dict_value.setter
    def dict_value(self, dict_value):
        if not isinstance(dict_value, dict):
            raise ValueError
        self.__dict_value = dict_value
            
    @property
    def dict_value2(self):
        return self.__dict_value2
                
    @dict_value2.setter
    def dict_value2(self, dict_value2):
        if not isinstance(dict_value2, dict):
            raise ValueError
        self.__dict_value2 = dict_value2
            

