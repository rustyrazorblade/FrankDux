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

def test_basic_registration_func_exists(app):

    # each of the calls should be available in the registry

    # I should be able to call the functions in the app directly
    # assert app.is_greater_than_five(10)
    assert "test_func" in app.registry
    assert "test_args" in app.registry
    assert "is_greater_than_five" in app.registry

def test_func_args_are_set_properly(app):

    f = app["is_greater_than_five"]
    # does the registry have the proper args set up?
    assert "i" in f.types
    assert f.args["i"] == int
    # expecting "i=int"
    # return type?

def test_funcs_can_be_called(app):
    f = app["is_greater_than_five"]
    assert f(i=10)


