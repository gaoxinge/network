def Item(name, data):

    """contruct a named dictionary"""

    # check whether data is a list
    if not isinstance(data, list):
        raise TypeError('%s is not a list' % str(data))

    # check whether value in data is unique
    for x in data:
        if data.count(x) != 1:
            raise ValueError('%s is not unique in %s' % (str(x), str(data)))

    # attributes
    attrs = {}

    # _fields, __slots__
    attrs['_fields']   = data
    attrs['__slots__'] = ('_d', )

    # __init__
    def __init__(self, **args):
        self._d = {}
        for x in args:
            if x not in self._fields:
                raise ValueError('%s is not in %s' % (str(x), str(self._fields)))
            self._d[x] = args[x]

    attrs['__init__'] = __init__

    # __getitem__, __setitem__, __delitem__
    def __getitem__(self, x):
        return self._d[x]

    def __setitem__(self, x, y):
        if x not in self._fields:
            raise ValueError('%s is not in %s' % (str(x), str(self._fields)))
        else:
            self._d[x] = y

    def __delitem__(self, x):
        del self._d[x]

    attrs['__getitem__'] = __getitem__
    attrs['__setitem__'] = __setitem__
    attrs['__delitem__'] = __delitem__

    # keys, values, items
    def keys(self):
        return self._d.keys()

    def values(self):
        return self._d.values()

    def items(self):
        return self._d.items()

    attrs['keys']   = keys
    attrs['values'] = values
    attrs['items']  = items

    # __iter__, __len__, __str__, __repr__
    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)

    def __str__(self):
        return str(self._d)

    def __repr__(self):
        return repr(self._d)

    attrs['__iter__'] = __iter__
    attrs['__len__']  = __len__
    attrs['__str__']  = __str__
    attrs['__repr__'] = __repr__

    # return
    return type(name, (object, ), attrs)
