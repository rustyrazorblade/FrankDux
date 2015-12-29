import sys
from frankdux import FrankDux
from importlib import import_module
sys.path.append("")

def main():
    print "Generating stuff"
    (module, obj) = sys.argv[1].split(":")
    print module, obj
    # m = __import__(module, fromlist=[obj])
    m = import_module(module)
    frank = getattr(m, obj)
    frank.generate_client_libraries(output_dir="output",
                                    language="python")
    print "Done"


if __name__ == "__main__":
    main()
