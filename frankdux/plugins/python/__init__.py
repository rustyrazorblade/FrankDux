from jinja2 import Environment, FileSystemLoader


def main(frank):
    print "Executing main()", frank
    # load up the jinja template
    # env = Environment(loader=FileSystemLoader(""))
    env = Environment(loader=FileSystemLoader("frankdux/plugins/python"))
    client = env.get_template("client.jinja")

    client.render(frank=frank)

    # setup.py
