# message encoding / decoding
# this file will be included with the client libraries
# so we need to be careful about dependencies
# on the client side, every type will be automatically registered in the import process

from collections import namedtuple
from struct import pack, unpack
from functools import partial

Type = namedtuple("Type", ["encoder", "decoder"])

class MessageEncoder(object):
    """
    we're going to create 1 message encoder per RPC call
    """
    schema = None  # k/v pairs of name:type
    def __init__(self, schema):
        """
        :param typemap: dict of name:type pairs
        :return:
        """
        self.schema = schema


class MessageDecoder(object):
    schema = None  # k/v pairs of name:type
    def __init__(self, schema):
        """
        :param typemap: dict of name:type pairs
        :return:
        """
        self.schema = schema
    pass



class TypeRegistry(object):
    types = None

    def __init__(self):
        self.types = {}

    def register(self, type, encoder, decoder):
        t = Type(encoder=encoder, decoder=decoder)
        self.types[type] = t

    def encode_int(self, i):
        return pack("!I", i)

    def decode_int(self, bytes):
        return unpack("!I", bytes)[0]

    def encode_object(self):
        pass

    def decode_object(self):
        pass
