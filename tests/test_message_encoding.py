from frankdux import TypeRegistry
from pytest import fixture, raises
from frankdux.types import Type, Int, String, Map

class SimpleUser(Type):
    name = String()
    age = Int()

class Address(Type):
    street = String()
    state = String()
    zip = String()

class User(Type):
    name = String()
    age = String()
    addresses = Map(String, Address)

@fixture
def registry():
    r = TypeRegistry()
    r.add_type(SimpleUser)
    r.add_type(User)

    return r


def test_simple_encoding(registry):
    s = SimpleUser(name="jon", age=34)
    registry.encode(s)


