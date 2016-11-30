class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):                                          # __str__ function returns the representation of the object
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, self_1):                                  # __add__ function will add two x point with '+'
        return Point(self.x + self_1.x, self.y + self_1.y)

points = Point(2, 12)                                          # giving values to the function for x point and y point
points_1 = Point(16, 6)                                        # giving another value to add in the first x point and y point
points_2 = points + points_1                                   # using + sign to add both values
print points_2                                                 # print the sum of both points

