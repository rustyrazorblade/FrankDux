from collections import namedtuple



class FrankDux(object):
    reg = None

    def __init__(self):
        self.reg = {}

    def register(self, *args, **kwargs):
        """
        Usage:

        # how to set default values?

        @app.register(str, int)
        def my_stuff(a, b):
            pass

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


