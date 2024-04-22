#!/usr/bin/python3
"""Rectangle module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize rectangle class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str representation of square"""

        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Getter function"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter function"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""

        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation"""

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
