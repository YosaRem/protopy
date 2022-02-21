class WireTypeChoicer:
    def get_wire_type_bytes(self, index, type_f):
        return bytes.fromhex(format((index << 3) | self.get_wire(type_f), "02X"))

    @staticmethod
    def get_wire(type_f):
        field_type = type_f
        if field_type in [int, bool]:
            return 0
        if field_type is float:
            return 1
        if field_type is str:
            return 2
        if field_type is dict:
            return 3

    @staticmethod
    def get_wires_types(descriptor):
        wires = {}
        choicer = WireTypeChoicer()
        for i in descriptor:
            if "is_enum" in descriptor[i] and descriptor[i]["is_enum"]:
                wires[choicer.get_wire_type_bytes(descriptor[i]["index"], int)] = i
            else:
                wires[choicer.get_wire_type_bytes(descriptor[i]["index"], descriptor[i]["type"])] = i
        return wires
