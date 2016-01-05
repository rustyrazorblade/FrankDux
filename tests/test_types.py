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




