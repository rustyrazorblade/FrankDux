
class Descriptor(object):
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

class Primitive(Descriptor):
    pass


# primitive types.  will get mapped directly to a language's primitives
class Int(Primitive):
    pass


class Float(Primitive):
    pass


class String(Primitive):
    pass


class Bytes(Primitive):
    pass


class Collection(Descriptor):
    def __init__(self, collection_type):
        pass

class Map(Collection):
    pass


class List(Collection):
    pass


class Map(Collection):
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



