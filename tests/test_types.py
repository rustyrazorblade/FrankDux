from pytest import fixture, raises

from frankdux.types import *

@fixture
def User():
    class User(Type):
        name = String()
        age = Int()

    return User


def test_user_creation():
    class User(Type):
        name = String()
        age = Int()

    u = User(name="jon", age=34)

    assert "name" in u._fields
    assert "age" in u._fields

    assert u.name == "jon"
    assert u.age == 34

    u.name = "new jon"

    assert u.name == "new jon"



def test_complex_objects():
    class Birthday(Type):
        month = Int()
        day = Int()
        year = Int()

    class User(Type):
        name = String()
        birthday = Birthday()

    birthday = Birthday(month=7, day=11, year=1981)

    u = User(name="Jon",
             birthday=birthday)

    assert u.birthday.month == 7
    assert u.birthday.day == 11
    assert u.birthday.year == 1981

    u = User(name="Jon",
             birthday=Birthday(month=7, day=11, year=1981))

    assert u.birthday.month == 7
    assert u.birthday.day == 11
    assert u.birthday.year == 1981


def test_list():
    class Phone(Type):
        name = String()
        number = String()

    class User(Type):
        name = String()
        numbers = List(Phone)


    u = User(name="Jon", numbers=[Phone(name="home", number="111111111")])

    assert len(u.numbers) == 1
    assert u.numbers[0].name == "home"


def test_map():
    class User(Type):
        name = String()
        pies = Map(String, Int)

    u = User(name="jon")
    u.pies["apple"] = 10
    u.pies["blueberry"] = 7

@fixture
def ValidationFixture():
    class Validation(Type):
        i = Int()
        f = Float()
        s = String()
        b = Bytes()
    return Validation

def test_int_validation(ValidationFixture):
    with raises(ValueError):
        ValidationFixture(i="blah")
