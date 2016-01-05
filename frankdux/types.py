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

    def __init__(self, *kwargs):
        pass

    def __metaclass__(name, bases, attrs):
        bases = tuple([BaseType])
        body = dict()

        # import ipdb; ipdb.set_trace()
        return type(name, bases, body)



