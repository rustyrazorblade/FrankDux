from pytest import fixture

from frankdux.types import *

@fixture
def User():
    class User(Type):
        name = String()
        age = Int()

    return User


def test_user_creation(User):
    u = User(name="jon", age=34)
    assert u.name == "jon"
    assert u.age == 34



def test_complex_objects():
    class Birthday(Type):
        month = Int()
        day = Int()
        year = Int()

    class User(Type):
        name = String()
        birthday = Birthday()

    u = User(name="Jon",
             birthday=Birthday(month=7, day=11, year=1981))
