from capnp import load

class CodeGen(object):
    """
    class responsible for generating a few files:

    1. new capn proto schema which is a merge of the
       existing schema and the new RPC calls

    2. uses capn proto

    3. client RPC library

    See how to use the loader: https://github.com/jparyani/pycapnp/blob/2516e3e4f1fcc6be1060310daf43100c28faa21f/capnp/lib/capnp.pyx#L3098
    """
    schema = None
    def __init__(self, frank_instance, cap_schema):
        schema = load(cap_schema)
