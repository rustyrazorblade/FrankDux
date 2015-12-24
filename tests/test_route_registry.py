import sys
print sys.path

from frankdux import FrankDux
from pytest import fixture, raises

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

    @frank.register(int, returns=int)
    def none_test(i):
        return 1 if i is None else 0


    return frank

@fixture
def typemap():
    return {"i":int}


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
    assert f.types["i"] == int


def test_funcs_can_be_called(app):
    f = app["is_greater_than_five"]
    assert f(i=10)


def test_type_checking_is_enforced(app):
    with raises(TypeError):
        app["is_greater_than_five"](i="bacon")


def test_default_none_is_passed_in(app):
    assert app["none_test"]() == 1


def test_returned_from_register_is_callable():
    frank = FrankDux()

    @frank.register(int, returns=int)
    def test_func(i):
        return i

    assert(test_func(i=1) == 1)


def test_validate_args(typemap):
    frank = FrankDux()
    result = frank.validate_args(typemap, {"i": 1})
    assert result["i"] == 1

    result = frank.validate_args(typemap, {})
    assert result["i"] is None

    with raises(TypeError):
        frank.validate_args(typemap, {"i": "happy birthday"})

