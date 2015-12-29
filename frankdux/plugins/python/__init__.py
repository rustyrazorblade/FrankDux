from jinja2 import Environment, FileSystemLoader


def main(frank, output_dir):
    print "Executing main()", frank
    # load up the jinja template
    # env = Environment(loader=FileSystemLoader(""))
    env = Environment(loader=FileSystemLoader(__path__))

    client = env.get_template("client.jinja")

    rendered_client = client.render(frank=frank)

    loc = "{}/client.py".format(output_dir)
    fp = open(loc, 'w')
    fp.write(rendered_client)
    fp.write("\n")
    fp.close()



    # setup.py
    setup = env.get_template("setup.jinja")


