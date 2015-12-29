from pytest import fixture, raises
from frankdux.codegen import CodeGen, PluginNotFoundException, PYTHON
from frankdux import FrankDux
from fixtures import app

@fixture
def codegen():
    frank = app()
    return CodeGen(frank, "output", language="python")

def test_route_struct_generation(codegen):
    pass


def test_generate_library(codegen):
    codegen.write()
