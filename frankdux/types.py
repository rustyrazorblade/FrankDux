import msgpack

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

    def encode(self):
        result = {}
        for k,v in self._values.iteritems():
            ftype = self._fields[k]

            if isinstance(ftype, Primitive):
                result[k] = v
            elif isinstance(ftype, (Collection, Type)):
                result[k] = ftype.encode()
            else:
                raise NotImplementedError()

        return (self._name, result)



class Primitive(Descriptor):
    pass


# primitive types.  will get mapped directly to a language's primitives
class Int(Primitive):
    _name = "Int"
    @classmethod
    def _validation_func(cls, val):
        if not isinstance(val, int):
            raise ValueError
        return val



class Float(Primitive):
    _validation_func = float
    _name = "Float"


class String(Primitive):
    _name = "String"
    @classmethod
    def _validation_func(cls, val):
        if not isinstance(val, basestring):
            raise ValueError
        return val


class Bytes(Primitive):
    _name = "Bytes"
    _validation_func = bytes


# all collections are tracking a value type
class Collection(Descriptor):
    _value_type = None

    def encode(self):
        raise NotImplementedError()


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
    _map = None

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
        self._map = m
        return m
        # return self._value_type._validate(val)

    # maps will be encoded as a 2 item tuple as normal
    # except the value will be a 3 item tuple, the key & value types, then the dict
    # ("Map", (KeyType, ValueType, {k/v pairs})
    def encode(self):
        data = {}
        for k,v in self._map.iteritems():
            _, encoded = v.encode()
            data[k] = encoded
        types_and_data = (self._key_type._name, self._value_type._name, data)
        return ("Map", types_and_data)

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
        for n, instance in fields.iteritems():
            instance.name = n

        attrs["_fields"] = fields  # k/v list of name:type
        attrs["_values"] = {}
        attrs["_name"] = name
        # ensure each of the metaclass instances knows it's field name


        return super(TypeMetaClass, cls).__new__(cls, name, bases, attrs)


# Descriptor because we want to have nested types
class BaseType(Descriptor):
    _fields = None
    _values = None
    _name = None

    def __init__(self, **kwargs):
        # check if the fields all exist
        fields = kwargs.keys()
        if len(set(fields) - set(self._fields.keys())) > 0:
            raise TypeError

        for (name, value) in kwargs.iteritems():
            field = self._fields[name]
            field.__set__(self, value)

    def encode(self):
        result = {}
        for k,v in self._values.iteritems():
            ftype = self._fields[k]

            if isinstance(ftype, Primitive):
                result[k] = v
            elif isinstance(ftype, (Collection, Type)):
                result[k] = ftype.encode()
            else:
                raise NotImplementedError()

        return (self._name, result)

    @classmethod
    def decode(cls, obj):
        result = cls()
        for (name, value) in obj.iteritems():
            field = result._fields[name]
            # import ipdb; ipdb.set_trace()
            field.__set__(result, value)

        return result



# inherit from this
class Type(BaseType):
    __metaclass__ = TypeMetaClass



class Request(Type):
    func = String()
    body = Bytes() # will be decoded later

class Response(Type):
    body = Bytes()
    metrics = Map(String, Float)


class TypeRegistry(object):
    types = None

    def __init__(self):
        self.types = {}

    def add_type(self, t):
        name = t._name
        self.types[name] = t
        # register all subtypes if it's a Type
        if isinstance(t, Type):
            for subtype in filter(lambda x: isinstance(x, Type), t._fields.values()):
                self.add_type(subtype)

    def encode(self, obj):
        # extract all the keys and stats about usage
        encoded = obj.encode()
        typemap = {}
        typemap_and_data = (typemap, encoded)
        return msgpack.packb(typemap_and_data)

    def decode(self, data):
        (type_map, data) = msgpack.unpackb(data)
        (t, d) = data # type, data
        return self.types[t].decode(d)

