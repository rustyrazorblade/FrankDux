
class Descriptor(object):
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass



class Int(Descriptor):
    pass

class Float(Descriptor):
    pass

class String(Descriptor):
    pass

class Bytes(Descriptor):
    pass


class BaseType(object):
    def __init__(self, **kwargs):
        pass


class Type(BaseType):
    _values = None

    def __metaclass__(name, bases, attrs):
        bases = tuple([BaseType])
        values = {}

        for key, value in attrs.iteritems():
            print key, value

        body = {"_values": values }
        # are we trying to create a class with something other than a descriptor?  BANNED

        return type(name, bases, body)



