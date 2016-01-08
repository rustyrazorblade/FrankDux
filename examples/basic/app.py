from frankdux import FrankDux
from frankdux.types import Type, Int, Float, String


frank = FrankDux()

# Generate the client library
# frankdux app:frank python

class User(Type):
    name = String()
    age = Int()

@frank.register(String, Int, returns=User)
def create_user(name, age):
    return User(name=name, age=age)


if __name__ == "__main__":
    frank.run()
