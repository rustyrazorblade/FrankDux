class Int(object):
    pass

class Float(object):
    pass

class String(object):
    pass

class Bytes(object):
    pass

class BaseType(object):
    def __init__(self, **kwargs):
        pass


class Type(BaseType):
    _values = None

    def __init__(self, **kwargs):
        pass

    def __metaclass__(name, *stuff):
        bases = tuple([BaseType])
        body = dict()

        return type(name, bases, body)



