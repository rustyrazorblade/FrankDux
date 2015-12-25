from pytest import fixture
from frankdux.codegen import CodeGen
from fixtures import app

@fixture
def codegen():
    frank = app()
    return CodeGen(frank, "output", language="python")

def test_route_generation(codegen):
    pass
