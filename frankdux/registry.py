"""
RPC registry
"""

class Registry(object):
    mapping = None

    def __init__(self):
        self.mapping = {}
