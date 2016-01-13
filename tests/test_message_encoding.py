from frankdux import TypeRegistry
from pytest import fixture, raises
from frankdux.types import Type, Int, String, Map, Float

class SimpleUser(Type):
    name = String()
    age = Int()


class Address(Type):
    street = String()
    state = String()
    zip = String()

class Rectangle(Type):
    height = Int()
    width = Int()


class User(Type):
    name = String()
    age = Int()
    rec = Rectangle()
    addresses = Map(String, Address)


@fixture
def registry():
    r = TypeRegistry()
    r.add_type(SimpleUser)
    r.add_type(User)
    return r


def test_registry_has_correct_type_name(registry):
    assert "SimpleUser" in registry.types
    assert "User" in registry.types
    assert "Rectangle" in registry.types

def test_simple_to_dict():
    # type and dict
    (t, d) = SimpleUser(name="jon", age=34).encode()
    assert t == "SimpleUser"
    assert d["name"] == "jon"
    assert d["age"] == 34

def test_complex_to_dict():
    # type and dict
    (t, d) = User(name="jon", age=34, rec=Rectangle(height=4, width=8)).encode()
    assert t == "User"
    assert d["name"] == "jon"
    assert d["age"] == 34

    rec = d["rec"]
    assert isinstance(rec, tuple)
    (k, v) = rec
    assert v["width"] == 8
    assert v["height"] == 4


def test_simple_encoding(registry):
    s = SimpleUser(name="jon", age=34)
    encoded = registry.encode(s)
    print encoded

    original = registry.decode(encoded)

    assert original.name == "jon"
    assert original.age == 34


def test_complex_encoding(registry):
    r = Rectangle(height=10, width=5)
    s = User(name="jon", age=34, rec=r)
    encoded = registry.encode(s)
    print "Complex:", encoded
    original = registry.decode(encoded)

    assert original.name == "jon"
    assert original.age == 34

