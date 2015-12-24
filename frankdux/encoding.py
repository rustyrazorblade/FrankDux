# message encoding / decoding
# this file will be included with the client libraries
# so we need to be careful about dependencies
# on the client side, every type will be automatically registered in the import process

from collections import namedtuple
from struct import pack, unpack
from functools import partial

Type = namedtuple("Type", ["encoder", "decoder"])

class TypeRegistry(object):
    types = None

    def __init__(self):
        self.types = {}
        # self.register("int",
        #               encoder=partial(pack("!I")),
        #               decoder=lambda x: unpack("!I", x)[0])

    def register(self, type, encoder, decoder):
        t = Type(encoder=encoder, decoder=decoder)
        self.types[type] = t

    def encode_int(self, i):
        return pack("!I", i)

    def decode_int(self, bytes):
        return unpack("!I", bytes)[0]

    def encode(self):
        pass

    def decode(self):
        pass
