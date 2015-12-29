from frankdux import FrankDux

frank = FrankDux()

# Generate the client library
# frankdux app:frank

@frank.register(int, int, returns=int)
def add(self, a, b):
    return a + b

@frank.register(int, int, returns=int)
def subtract(self, a, b):
    return a - b

if __name__ == "__main__":
    frank.run()
