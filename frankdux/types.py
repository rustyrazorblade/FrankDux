
class Descriptor(object):
    name = None
    def __get__(self, instance, owner):
        return instance._values.get(self.name, None)

    def __set__(self, instance, value):
        instance._values[self.name] = value

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

        # assign the field names
        for name, instance in fields:
            instance.name = name

        attrs["_fields"] = set([x[0] for x in fields])
        attrs["_values"] = {}
        # ensure each of the metaclass instances knows it's field name


        return super(TypeMetaClass, cls).__new__(cls, name, bases, attrs)


# Descriptor because we want to have nested types
class BaseType(Descriptor):
    _fields = None
    _values = None
    def __init__(self, **kwargs):
        # check if the fields all exist
        fields = kwargs.keys()
        if len(set(fields) - self._fields) > 0:
            raise TypeError

        for field, value in kwargs.iteritems():
            self._values[field] = value



# inherit from this
class Type(BaseType):
    __metaclass__ = TypeMetaClass






