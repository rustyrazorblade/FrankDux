from frankdux import FrankDux
import logging

# output everything
logging.basicConfig(level=logging.INFO)


frank = FrankDux()

# Generate the client library
# frankdux app:frank python

@frank.register(int, int, returns=int)
def add(first_var, second_var):
    return first_var + second_var

@frank.register(int, int, returns=int)
def subtract(a, b):
    return a - b

@frank.register(str, str, returns=str)
def concat_and_make_fun(a, b):
    return a + b + " you suck"

@frank.register([str])
def concat_all(list_of_str):
    pass


if __name__ == "__main__":
    frank.run()
