class point:
    def __init__(self, x=0, y=0):                            # __init__ is easier to instantiate object
        self.x = x
        self.y = y

    def __str__(self):                                       # __str__ function returns the representation of the object
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

point = point(5, 6)                               # giving values to the x point and y point
print point                                       # print point



