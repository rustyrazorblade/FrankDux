from collections import namedtuple
from functools import wraps
import logging

# Function = namedtuple("Function", ["args", "return_type"], verbose=True)

class Function(object):
    name = None
    types = None # dict of key=type pairs
    return_type = None
    func = None

    def __init__(self, name, types, return_type, func):
        self.name = name
        self.types = types
        # make sure this is list of dicts
        self.return_type = return_type
        self.func = func

    def __call__(self, **kwargs):
        return self.func(**kwargs)


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

        # i
        # import ipdb; ipdb.set_trace()
        def new_func(func):
            # register the function here

            returns = kwargs.get("returns", None)
            name = func.func_name
            # pull out the arg types & match to the names

            zipped = dict(zip(func.func_code.co_varnames, args))
            # import ipdb; ipdb.set_trace()

            # create new function (functools.wraps)
            # check types when called
            @wraps(func)
            def new_rpc(*new_args, **new_kwargs):
                # check types
                # import ipdb; ipdb.set_trace()
                # get a list of the default args
                # make sure types are optional

                arguments = self.validate_args(zipped, new_kwargs)
                result = func(*new_args, **new_kwargs)
                # type check return type
                return result

            f = Function(name=name, types=zipped,
                         return_type=returns, func=new_rpc)

            self.registry[name] = f
            print "Created func:", func, args, kwargs


            return new_rpc

        return new_func

    def call(self, func, **kwargs):
        pass

    def __getitem__(self, item):
        return self.registry[item]


    def validate_args(self, typemap, kwargs):
        """
        checks each of the elements in kwargs
        returns a dictionary of k/v pairs
        sets None as default for all keys that aren't set explicitly
        :param typemap:
        :param kwargs:
        :return:
        """
        pass
