from frankdux import TypeRegistry
from pytest import fixture, raises
from frankdux.types import Type, Int, String, Map, Float, List

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
    cats = Map(String, Int) # name to age
    fav_nums = List(Int)


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
    data = SimpleUser(name="jon", age=34).encode()
    assert data["name"] == "jon"
    assert data["age"] == 34


def test_complex_to_dict():
    # type and dict
    data = User(name="jon", age=34, rec=Rectangle(height=4, width=8)).encode()
    assert data["name"] == "jon"
    assert data["age"] == 34

    rec = data["rec"]
    assert rec["width"] == 8
    assert rec["height"] == 4


def test_map_collection_to_dict():
    encoded = User(name="jon", age=34,
                  addresses={"home":Address(street="whatever", state="CA", zip="90254")}).encode()
    """
    {'addresses': {'home': {'state': 'CA', 'street': 'whatever', 'zip': '90254'}},
     'age': 34,
     'name': 'jon'}
    """
    addresses = encoded["addresses"]
    assert len(addresses) > 0
    assert addresses["home"] == {'state': 'CA', 'street': 'whatever', 'zip': '90254'}

    decoded = User.decode(encoded)
    assert isinstance(decoded.addresses["home"], Address)


def test_list_collection_to_dict():
    u = User(name="steve", fav_nums=[1,2,3])
    encoded = u.encode()

    decoded = User.decode(encoded)
    assert decoded.fav_nums == [1,2,3]

def test_simple_encoding(registry):
    s = SimpleUser(name="jon", age=34)
    encoded = registry.encode(s)

    original = registry.decode(encoded)

    assert original.name == "jon"
    assert original.age == 34


def test_complex_encoding(registry):
    r = Rectangle(height=10, width=5)
    s = User(name="jon", age=34, rec=r)

    encoded = registry.encode(s)
    original = registry.decode(encoded)

    assert original.name == "jon"
    assert original.age == 34


def test_primitive_in_map():
    s = User(name="jon", age=34, cats={"Max": 10, "Mittens": 9}).encode()

def test_user_internal_object_share_bug():
    tmp = User(name="jon", age=34,
               addresses={"home":Address(street="whatever", state="CA", zip="90254")})

    r = Rectangle(height=10, width=5)
    s = User(name="jon", age=34, rec=r)
    assert tmp.addresses != s.addresses

    s2 = User(name="jon")
    assert s2.age != 34
