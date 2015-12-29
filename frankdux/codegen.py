import os
from capnp import load
from importlib import import_module

class PluginNotFoundException(Exception): pass

PYTHON="python"


class CodeGen(object):
    """
    class responsible for generating a few files:

    1. new capn proto schema which is a merge of the
       existing schema and the new RPC calls

    2. uses capn proto to generate data structures

    3. generate client RPC library

    See how to use the loader: https://github.com/jparyani/pycapnp/blob/2516e3e4f1fcc6be1060310daf43100c28faa21f/capnp/lib/capnp.pyx#L3098
    """
    schema = None
    output_dir = None
    language = None
    frank = None

    def __init__(self, frank_instance,
                 output_dir="output",
                 cap_schema=None,
                 language=None):

        if language is None:
            raise TypeError("Language is required")

        self.output_dir = output_dir
        self.language = language
        self.frank = frank_instance
        # load the python plugin


    def write(self):
        """
        writes the full schema to the file handle
        :param fp:
        :return:
        """
        self.check_plugin_exists()
        self.create_output_directory()
        self.create_client_library()
        self.copy_schema_to_output()

    def check_plugin_exists(self):
        pass

    def generate_rpc_struct(self, typemap):
        """

        :param typemap: dict of key/type pairs
        :return: str - capn proto compliant struct string
        """
        # u.schema.node.displayName.split(":")[1]
        result = "struct {}"
        pass

    def create_output_directory(self):
        try:
            os.makedirs(self.output_dir)
        except OSError:
            print "Directory already exists"


    def copy_schema(self):
        pass

    def create_client_library(self):
        # raise exception if we can't find the plugin
        path = ".plugins.{}".format(self.language)
        import_module(path, "frankdux").main(self.frank, self.output_dir)  # executes main() from imported lib


    def copy_schema_to_output(self):
        pass


