'''
Created on 8 Mar 2021

@author: jackm
'''

class Period:
    
    def __init__(self, start, end, points, point_count) -> None:
        self.start = start
        self.end = end
        self.points = points
        self.point_count = point_count

class PeriodBuilder:
    
    def __init__(self): pass
    
    def withStart(self, start):
        self.start = start
        return self
    
    def withEnd(self, end):
        self.end = end
        return self
    
    def withPoints(self, points):
        self.points = points
        return self
    
    def build(self):
        return Period(self.start, self.end, self.points, len(self.points))
    
def validateLists(start_end_list, points_list):
    
    if (not isinstance(start_end_list, list)): raise TypeError("start_end_list must be a list")
    if (not isinstance(points_list, list)): raise TypeError("points_list must be a list")
    if (len(start_end_list) > 20): raise ValueError("Can only be a maximuim of 10 Period")
    if (not all(isinstance(x, int) for x in start_end_list)): raise TypeError("start_end_list must be whole numbers")
    if (not all(isinstance(x, int) for x in points_list)): raise TypeError("points_list must be whole numbers")
    if (len(start_end_list) % 2 != 0): raise ValueError("Unequal number of start and end points")

def validatePoints(a, b, points):
    
    if (a > b): raise ValueError("Point {a} is > to {b}".format(a=a, b=b))
    if (b - a > 10): raise ValueError("A period may be no longer than 10 seconds")
    if (len(points) > 10 or len(points) <= 0): raise ValueError("Each period must contain between one and 10 data points")
    if (points != sorted(points)): raise ValueError("Points must be stored in time order, with the earliest listed first") # TODO

def generatePeriods(start_end_list, points_list):
    
    validateLists(start_end_list, points_list)

    periods = []
    
    it = iter(start_end_list)
    for a in it:
        b = next(it)
        points = [p for p in points_list if p >= a and p <= b]
        validatePoints(a, b, points)
        periods.append( PeriodBuilder().withStart(a)
                                       .withEnd(b)
                                       .withPoints(points)
                                       .build() )
    return periods