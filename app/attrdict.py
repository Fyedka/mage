### CLASSES ###


class AttrDict(dict):
    def __init__(self, x):
        super().__init__(x)

    def __getattr__(self, item):
        return self[item]

    def __dir__(self):
        return super().__dir__() + [str(k) for k in self.keys()]
