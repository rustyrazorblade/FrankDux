
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

class TypeMetaClass(type):
    def __new__(cls, name, bases, attrs):
        # get a list of all the
        fields = [(name, value) for (name, value) in attrs.items() if isinstance(value, Descriptor)]
        attrs["_fields"] = set([x[0] for x in fields])
        return super(TypeMetaClass, cls).__new__(cls, name, bases, attrs)


# Descriptor because we want to have nested types
class BaseType(Descriptor):
    _fields = None
    def __init__(self, **kwargs):
        # check if the fields all exist
        fields = kwargs.keys()
        if len(set(fields) - self._fields) > 0:
            raise TypeError
        


# inherit from this
class Type(BaseType):
    __metaclass__ = TypeMetaClass






