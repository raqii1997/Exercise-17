class Point(object):

    def __init__(self, x=0, y=0):                    # __init__ is easier to instantiate object
        self.x = x
        self.y = y
        print "The coordinate X = %d" % self.x, "and the coordinate Y = %d" % self.y

points = Point(5, 11)                      # By not assigning anything for x or y they are assumed to be 0

point = Point(16)                          # If you just want an x just write a value
                                           # for a Y you need to write (0,"number you want")
