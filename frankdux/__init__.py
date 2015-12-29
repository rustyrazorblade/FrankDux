from collections import namedtuple, OrderedDict
from functools import wraps
import logging
from encoding import MessageEncoder

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

            zipped = OrderedDict(zip(func.func_code.co_varnames, args))

            @wraps(func)
            def new_rpc(*new_args, **new_kwargs):
                # check types
                # get a list of the default args
                # make sure types are optional

                arguments = self.validate_args(zipped, new_kwargs)
                result = func(**arguments)
                # TODO type check return type
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
        :param typemap: dict of key:type
        :param kwargs: dict of key:value
        :return: key:value, type checked
        """
        result = {}
        for k, v in typemap.iteritems():
            tmp = kwargs.get(k, None)
            if tmp is None or isinstance(tmp, v):
                result[k] = tmp
            else:
                raise TypeError

        return result

    def run(self, port):
        # You have made it to the Kumite!
        # Run FrankDux on some port
        pass


    def decode_request(self, data):
        pass

