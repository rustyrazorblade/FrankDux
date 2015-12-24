from collections import namedtuple

import logging

# Function = namedtuple("Function", ["args", "return_type"], verbose=True)

class Function(object):
    name = None
    args = None # dict of key=type pairs
    return_type = None

    def __init__(self, name, args, return_type):
        self.name = name
        self.args = args
        # make sure this is list of dicts
        self.return_type = return_type

    def __call__(self, *args, **kwargs):
        pass


class FrankDux(object):
    registry = None

    def __init__(self):
        self.registry = {}

    def register(self, *args, **kwargs):
        """
        Registers a function to be available for RPC
        Specify arguments followed by return type

        Usage:

        # how to set default values?

        @app.register(int, returns=bool)
        def greater_than_zero(a):
            return a > 0


        :param args:
        :return:
        """
        logging.debug("Registering function with args:")
        print self
        print args
        print kwargs

        # i
        # import ipdb; ipdb.set_trace()
        def new_func(func):
            # register the function here

            returns = kwargs.get("returns", None)
            name = func.func_name
            # pull out the arg types & match to the names
            # import ipdb; ipdb.set_trace()

            zipped = dict(zip(func.func_code.co_varnames, args))

            f = Function(name=name, args=zipped, return_type=returns)
            self.registry[name] = f
            print "Created func:", func, args, kwargs
            return func

        return new_func

    def call(self, func, **kwargs):
        pass

    def __getitem__(self, item):
        return self.registry[item]

