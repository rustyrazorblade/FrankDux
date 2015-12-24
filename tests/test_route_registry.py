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
    # assert app.is_greater_than_five(10)
    assert "test_func" in app.registry
    assert "test_args" in app.registry
    assert "is_greater_than_five" in app.registry

    assert app.call("is_greater_than_five", i=10)

