from frankdux import FrankDux
from frankdux.types import String

frank = FrankDux()

# Generate the client library
# frankdux app:frank python

@frank.register(String, returns=String)
def hello(name):
    return "Hello " + name

if __name__ == "__main__":
    frank.run()
