from frankdux import FrankDux
from pytest import fixture, raises

from frankdux.encoding import TypeRegistry, MessageEncoder


@fixture
def registry():
    t = TypeRegistry()

    return t

@fixture
def schema():
    return {"i": int,
            "s": str}

@fixture
def encoder():
    encoder = MessageEncoder(schema())
    return encoder

def test_high_level_encoding_and_decoding(encoder):

    data = {"i": 5}
    encoded = encoder.encode()
    original = encoder.decode(data)

