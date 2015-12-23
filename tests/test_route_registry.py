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
    
    return app

def test_basic_registration(app):
    pass


