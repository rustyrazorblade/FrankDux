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
        #schema = load(cap_schema)
        pass

    def write(self, fp):
        """
        writes the full schema to the file handle
        :param fp:
        :return:
        """
        pass

    def generate_rpc_schema(self, typemap):
        """

        :param typemap: dict of key/type pairs
        :return: str - capn proto compliant struct string
        """
        # u.schema.node.displayName.split(":")[1]
        result = "struct {}"
        pass

