class ValidationError(Exception): pass
class InternalTypeError(Exception): pass


class Descriptor(object):
    name = None
    def __get__(self, instance, owner):
        return instance._values.get(self.name, None)

    def __set__(self, instance, value):
        value = self._validate(value)
        instance._values[self.name] = value

    @classmethod
    def _validate(cls, val):
        try:
            # if we return a validation function, call it w/ the arg
            return getattr(cls, "_validation_func")(val)
        except AttributeError: # could not find a validation function
            pass

        return val


class Primitive(Descriptor):
    pass


# primitive types.  will get mapped directly to a language's primitives
class Int(Primitive):
    @classmethod
    def _validation_func(cls, val):
        if not isinstance(val, int):
            raise ValueError
        return val


class Float(Primitive):
    _validation_func = float


class String(Primitive):
    @classmethod
    def _validation_func(cls, val):
        if not isinstance(val, basestring):
            raise ValueError
        return val


class Bytes(Primitive):
    _validation_func = bytes


# all collections are tracking a value type
class Collection(Descriptor):
    _value_type = None


# private, to be used internally only.  use Map() instead
class TypedMap(dict):
    _key_type = None
    _value_type = None

    def set_key_type(self, key_type):
        # if not isinstance(key_type, Primitive):
        #     raise TypeError("Key must be a primitive")

        self._key_type = key_type

    def set_value_type(self, value_type):
        self._value_type = value_type

    def __setitem__(self, key, value):
        new_key = self._key_type._validate(key)
        new_value = self._value_type._validate(value)
        return super(TypedMap, self).__setitem__(new_key, new_value)

class Map(Collection):
    _key_type = None


    def __init__(self, key_type, value_type):
        self._key_type = key_type
        self._value_type = value_type

    def _validate(self, val):

        # is this a map with all valid k/v pairs
        for k,v in val.iteritems():
            if not self._key_type._validate(k) or not self._value_type._validate(v):
                raise ValueError
        m = TypedMap(val)
        m.set_key_type(self._key_type)
        m.set_value_type(self._value_type)
        return m
        # return self._value_type._validate(val)

# internal use only, use List
class TypedList(list):
    _value_type = None
    def __init__(self, value_type, iterable):
        self._value_type = value_type
        super(TypedList, self).__init__(iterable)

    def append(self, value):
        # import ipdb; ipdb.set_trace()
        value = self._value_type._validate(value)
        return super(List, self).append(value)

class List(Collection):
    def __init__(self, value_type):
        self._value_type = value_type

    def _validate(self, val):
        # upgrade to a TypedList if it's a regular list
        if type(val) is list:
            val = TypedList(self._value_type, val)
        for v in val:
            self._value_type._validate(v)
        return val


class TypeMetaClass(type):
    def __new__(cls, name, bases, attrs):
        # get a list of all the
        fields = {name:value for (name, value) in attrs.items() if isinstance(value, Descriptor)}

        # assign the field names
        for name, instance in fields.iteritems():
            instance.name = name

        attrs["_fields"] = fields  # k/v list of name:type
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
        if len(set(fields) - set(self._fields.keys())) > 0:
            raise TypeError

        for (name, value) in kwargs.iteritems():
            field = self._fields[name]
            field.__set__(self, value)

# inherit from this
class Type(BaseType):
    __metaclass__ = TypeMetaClass






