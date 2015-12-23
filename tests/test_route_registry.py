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

    return frank

def test_basic_registration(app):
    pass


