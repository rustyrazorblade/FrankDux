from collections import namedtuple



class FrankDux(object):
    reg = None

    def __init__(self):
        self.reg = {}

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
        print self
        print args
        print kwargs

        # i
        def new_func(*args, **kwargs):
            return None

        return new_func


