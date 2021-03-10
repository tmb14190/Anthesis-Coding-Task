'''
Created on 8 Mar 2021

@author: jackm
'''
import unittest
import PeriodWithDefinedTesting as period

class TestValidationMethods(unittest.TestCase):
    
    def testUsingModifiedExampleData(self):
        start_end_list = [1, 5, 6, 10, 11, 20, 21, 25, 26, 30, 31, 40]
        points_list = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26, 11, 31, 18, 24, 21, 4, 22, 50, 6, 36]
        sorted_points_list = sorted(points_list)
        period.generatePeriods(start_end_list, sorted_points_list)
    
    # Example data fails because there exists a time period longer than 10 seconds with 26 -> 40
    # It would also fail due the list of seconds not being in chronological order
    def testUsingExampleData(self):
        start_end_list = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50]
        points_list = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26, 11, 31, 18, 24, 21, 4, 22, 50, 6, 36]
        self.assertRaises(ValueError, period.generatePeriods, start_end_list, points_list)
    
    def testPointsAreWholeNumbers(self):
        start_end_list = [1, 5.55]
        points_list = [1, 5]
        self.assertRaises(TypeError, period.generatePeriods, start_end_list, points_list)
    
    def testMaximumOfTenPeriods(self):
        start_end_list = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50, 51, 60, 61, 70, 71, 80, 81, 90, 91, 100]
        points_list = [1, 5]
        self.assertRaises(ValueError, period.generatePeriods, start_end_list, points_list)
    
    def testPeriodMustBeNoLongerThanTenSeconds(self):
        start_end_list = [1, 12]
        points_list = [1, 5]
        self.assertRaises(ValueError, period.generatePeriods, start_end_list, points_list)
    
    def testNumberOfDataPointsBetweenOneAndTen(self):
        start_end_list = [1, 11, 12, 20]
        long_points_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # feels odd that this is a reasonable use case, but is also wrong
        short_points_list = [12, 15]
        self.assertRaises(ValueError, period.generatePeriods, start_end_list, long_points_list)
        self.assertRaises(ValueError, period.generatePeriods, start_end_list, short_points_list)
    
    def testPointsStoredInTimeOrder(self):
        start_end_list = [1, 10]
        points_list = [5, 1]
        self.assertRaises(ValueError, period.generatePeriods, start_end_list, points_list)

if __name__ == '__main__':
    unittest.main()
    