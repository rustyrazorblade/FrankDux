from frankdux import FrankDux
from pytest import fixture, raises

from frankdux.encoding import TypeRegistry

@fixture
def registry():
    t = TypeRegistry()

    return t


# def test_int(registry):
#     t.

