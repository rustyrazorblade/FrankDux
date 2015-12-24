from collections import namedtuple

import logging

Function = namedtuple("Function", ["args", "return_type"], verbose=True)

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
        # logging.debug("Registering function with args:")
        # print self
        # print args
        # print kwargs

        # i
        # import ipdb; ipdb.set_trace()
        def new_func(func):
            # register the function here

            returns = kwargs.get("returns", None)
            name = func.func_name
            # pull out the arg types & match to the names
            # import ipdb; ipdb.set_trace()
            f = Function(args=args, return_type=returns)
            self.registry[name] = f
            print "Created func:", func, args, kwargs
            return func

        return new_func

    def call(self, func, **kwargs):
        pass

    def __getitem__(self, item):
        return self.registry[item]

