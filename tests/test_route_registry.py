import sys
print sys.path

from frankdux import FrankDux
from pytest import fixture

@fixture
def app():
    app = FrankDux()

    @app.register()
    def test_func():
        pass

def test_basic_registration():
    pass


