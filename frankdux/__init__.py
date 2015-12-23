from collections import namedtuple



class FrankDux(object):
    reg = None

    def __init__(self):
        self.reg = {}

    def register(self, **args):
        """
        Usage:

        # how to set default values?

        @app.register(str, int)
        def my_stuff(a, b):
            pass

        :param args:
        :return:
        """
        pass

    def returns(self, t):
        pass
