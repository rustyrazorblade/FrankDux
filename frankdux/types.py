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

    def __metaclass__(name, bases, attrs):
        bases = tuple([BaseType])
        body = dict()

        return type(name, bases, body)



