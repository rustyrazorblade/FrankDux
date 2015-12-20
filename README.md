FrankDux is a small python RPC framework that works with ZeroMQ and Capn Proto.  

Goals:

Capn Proto gives us static typing (in languages where it's available)

Server example (subject to change):

```
# app.py
from frankdux import FrankDux

# import capn proto interfaces

app = FrankDux()

@app.register(str, str) # arguments, first and last name
@app.returns(User)
def create_user(user):
    pass

app.run(port=8888)
```

Generate a client:

`frankdux compile app.py schema.capnp myserverpackage`

Client:

```
import myserverpackage


rpc = myserverpackage.RPC("localhost:8888")

user = rpc.create_user("jon", "haddad") # returns a capn proto object
```
