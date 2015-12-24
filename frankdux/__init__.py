from collections import namedtuple

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
        # print self
        # print args
        # print kwargs

        # i
        def new_func(func, *args, **kwargs):
            # register the function here

            returns = kwargs.get("returns", None)
            name = func.func_name
            f = Function(args=args, return_type=returns)
            self.registry[name] = f
            print "Created func:", func, args, kwargs
            return None

        return new_func


