#!/usr/bin/python3


"""
Square Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init data"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return Square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Return size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square id, size, x, and y"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of square"""
        my_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_dict
