FrankDux is a small python RPC framework that works with ZeroMQ and Capn Proto.  

Goals:

Capn Proto gives us static typing (in languages where it's available)

Server example (subject to change):

```
from frankdux import FrankDux

# import capn proto interfaces

app = FrankDux()

@app.register(User) # arguments 
def create_user(user):
    pass

app.run(port=8888)
```
