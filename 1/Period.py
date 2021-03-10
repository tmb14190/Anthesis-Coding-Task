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
    
def validateList(start_end_list, points_list):
    
    if (not isinstance(start_end_list, list)): raise Exception("start_end_list must be a list")
    if (not isinstance(points_list, list)): raise Exception("points_list must be a list")
    if (not all(isinstance(x, int) for x in start_end_list)): raise Exception("start_end_list can only contain integers")
    if (not all(isinstance(x, int) for x in points_list)): raise Exception("points_list can only contain integers")
    if (len(start_end_list) % 2 != 0): raise Exception("Unequal number of start and end points")

def generatePeriods(start_end_list, points_list):
    
    validateList(start_end_list, points_list)

    points = []
    
    it = iter(start_end_list)
    for a in it:
        b = next(it)
        if (a > b): raise Exception("Point {a} is > to {b}".format(a=a, b=b))
        points.append( PeriodBuilder().withStart(a)
                                      .withEnd(b)
                                      .withPoints( [p for p in points_list if p >= a and p <= b] )
                                      .build() )
    return points
    
if __name__ == "__main__":
    start_end_list = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50]
    points_list = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26, 11, 31, 18, 24, 21, 4, 22, 50, 6, 36]
    periods = generatePeriods(start_end_list, points_list)
    
    for p in periods:
        print ("Start -> " + str(p.start))
        print ("End -> " + str(p.end))
        print ("Points -> " + str(p.points))
        print ("Point Count -> " + str(p.point_count))
        print ("\n")
    


