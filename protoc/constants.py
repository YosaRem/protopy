SINGULAR = "singular"
REPEATED = "repeated"
CUSTOM = "custom"

SCALAR_VALUE = {
    "double": "float",
    "float": "float",
    "int32": "int",
    "int64": "int",
    "uint32": "int",
    "uint64": "int",
    "sint32": "int",
    "sint64": "int",
    "fixed32": "int",
    "fixed64": "int",
    "sfixed32": "int",
    "sfixed64": "int",
    "bool": "bool",
    "string": "str",
    "bytes": "str",
}


DEFAULT_TYPE = {
    "int": "0",
    "long": "0",
    "float": "0.0",
    "bool": "False",
    "str": '""',
    "dict": '{}'
}
