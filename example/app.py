from frankdux import FrankDux

frank = FrankDux()

# Generate the client library
# frankdux app:frank

@frank.register(int, int, returns=int)
def add(first_var, second_var):
    return first_var + second_var

@frank.register(int, int, returns=int)
def subtract(a, b):
    return a - b

if __name__ == "__main__":
    frank.run()
