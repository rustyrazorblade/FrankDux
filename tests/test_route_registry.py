import sys
print sys.path

from frankdux import FrankDux
from pytest import fixture

@fixture
def app():
    frank = FrankDux()

    @frank.register()
    def test_func():
        pass

    @frank.register(str, int)
    def test_args(name, age):
        pass

    @frank.register(int, returns=bool)
    def is_greater_than_five(i):
        return i > 5

    return frank

def test_basic_registration(app):

    # each of the calls should be available in the registry

    # I should be able to call the functions in the app directly
    assert app.is_greater_than_five(10)


