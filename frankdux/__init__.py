import logging
from collections import OrderedDict
from functools import wraps


from gevent import spawn
import zmq.green as zmq

#
from .exceptions import ArgumentCountException
from .encoding import MessageEncoder
from frankdux.codegen import CodeGen


class Function(object):
    name = None
    types = None # OrderedDict of key=type pairs, str:type
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
    context = None

    def __init__(self):
        self.registry = {}  # str: Function

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

        def new_func(func):
            # register the function here

            returns = kwargs.get("returns", None)
            # make sure param counts match
            if len(func.func_code.co_varnames) != len(args):
                raise ArgumentCountException()

            name = func.func_name
            # pull out the arg types & match to the names
            # str:type
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
        # if len(typemap) != len(kwargs):
        #     raise ArgumentCountException()

        result = {}
        for k, v in typemap.iteritems():
            tmp = kwargs.get(k, None)
            if tmp is None or isinstance(tmp, v):
                result[k] = tmp
            else:
                raise TypeError

        return result

    def run(self, port=5000):
        # You have made it to the Kumite!
        # Run FrankDux on some port
        # probably need to use ZeroMQ Router/Dealer w/ device
        self.context = zmq.Context()
        frontend = self.context.socket(zmq.ROUTER)
        frontend.bind("tcp://*:5559")
        spawn(self.router, frontend)
        return

        # socket = self.context.socket(zmq.REP)
        # socket.bind("tcp://127.0.0.1:{}".format(port))
        # print "Socket available"
        #
        # while True:
        #     print "Receiving"
        #     data = socket.recv()
        #     print "got data: ", data
        #     socket.send("you are my friend")

    def router(self, frontend):
        # ZeroMQ router
        logging.info("Starting router")
        # router =


    def generate_client_libraries(self, output_dir, language):
        code = CodeGen(self, output_dir, language=language)
        code.write()


    def decode_request(self, data):
        pass

