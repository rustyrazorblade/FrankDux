@0xc2b429cb75fe750c;

struct Argument {
    type @0 : Text;
    value @1 : Data;
}

struct Request {
    func @0 : Text;
    arguments @1 : List(Argument);
}
