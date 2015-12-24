from pytest import fixture
from frankdux import FrankDux

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
