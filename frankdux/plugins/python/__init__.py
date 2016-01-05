from jinja2 import Environment, FileSystemLoader


def main(frank, output_dir):
    print "Executing python codegen: main()", frank
    # load up the jinja template
    # env = Environment(loader=FileSystemLoader(""))
    env = Environment(loader=FileSystemLoader(__path__))

    client = env.get_template("client.jinja")

    rendered_client = client.render(frank=frank)

    # copy frankdux.types over
    # the client is going to reuse all our metaclass stuff
    loc = "{}/client.py".format(output_dir)
    fp = open(loc, 'w')
    fp.write(rendered_client)
    fp.write("\n")
    fp.close()

    # setup.py
    setup = env.get_template("setup.jinja")
    rendered_setup = setup.render(frank=frank)

    loc = "{}/setup.py".format(output_dir)
    fp = open(loc, 'w')
    fp.write(rendered_client)
    fp.write("\n")
    fp.close()


    # make sure we've got an empty __init__ so it's a real package
    loc = "{}/__init__.py".format(output_dir)
    open(loc, 'w').close()


