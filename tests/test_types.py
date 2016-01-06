from pytest import fixture

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


