#
# hw9pr1.py
# Name: Brian Richardson & Courtney Gutherie
#
class Date:
    """ A user-defined data structure that
        stores and manipulates dates
    """
 
    def __init__(self, month, day, year):
        '''
        >>> d = Date(1,11,1111)
        >>> d.month
        1
        >>> d.day
        11
        >>> d.year
        1111
        '''
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year
 
 
    def __repr__(self):
        """ Returns a string REPResentation for the
            object of type Date that calls it (named self).
 
             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        '''
        >>> d1 = Date(11, 3, 2015)
        >>> print(date1)
        11/03/2015
        >>> print('Tuesday is', date1)
        Tuesday is 11/03/2015
        >>> d2 = Date(11, 3, 2015)
        >>> print(date2)
        11/03/2015
        '''
        return "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
 
 
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise.
        """
        '''

        >>> d3 = Date(1, 1, 2016)
        >>> d2 = Date(11, 3, 2015)
        >>> d3.isLeapYear()
        True
        >>> d2.isLeapYear()
        False
        '''
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        '''
        >>> date1 = Date(1, 1, 2016)
        >>> date2 = date1.copy()
        >>> date1 = Date(1, 2, 2018)
        >>> print(date1)
        01/02/2018
        >>> print(date2)
        01/01/2016
        '''
        newDate = Date(self.month, self.day, self.year)
        return newDate
    def isEqual(self, date2):
        """ Decides if self and date2 represent the same calendar date,
            whether or not they are in the same place in memory.
        """
        '''
        >>> date1 = Date(1, 1, 2016)
        >>> date2 = date1.copy()
        >>> date1 == date2
        False
        >>> date1.isEqual(date2)
        True
        >>> date1.isEqual(Date(1, 1, 2016))
        True
        >>> date1 == Date(1, 1, 2016)
        False
        '''
        return self == date2
    def __eq__(self,other):
        return self.year == other.year and self.month == other.month \
               and self.day == other.day
    def tomorrow(self):
        '''
        >>> d1 = Date(12,31,2015)
        >>> d1
        12/31/2015
        >>> d1.tomorrow()
        >>> d1
        01/01/2016
        >>> d1 = Date(2,28,2016)
        >>> d1.tomorrow()
        >>> d1
        02/29/2016
        >>> d1.tomorrow()
        >>> d1
        03/01/2016
        '''
        DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear():
            DAYS_IN_MONTH[2] += 1
        if self.day + 1 > DAYS_IN_MONTH[self.month]:
            if self.month + 1 > 12:
                self.year += 1
                self.month = 0
            self.month += 1
            self.day = 0
        self.day += 1

    def yesterday(self):
        '''
        >>> d = Date(1, 1, 2016)
        >>> d
        01/01/2016
        >>> d.yesterday()
        >>> d
        12/31/2015
        >>> d = Date(3, 1, 2016)
        >>> d.yesterday()
        >>> d
        02/29/2016
        >>> d.yesterday()
        >>> d
        02/28/2016
        '''
        DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear():
            DAYS_IN_MONTH[2] += 1
        if self.day - 1 == 0:
            if self.month - 1 == 0:
                self.year -= 1
                self.month = len(DAYS_IN_MONTH)
            self.month -= 1
            self.day = DAYS_IN_MONTH[self.month] + 1
        self.day -= 1
    def addNDays(self,n,**debug):
        '''
        >>> d = Date(1,1,2000)
        >>> d.addNDays(3)
        01/01/2000
        01/02/2000
        01/03/2000
        01/04/2000
        >>> d
        01/04/2000
        >>> d = Date(11,3,2015)
        >>> d.addNDays(929,debug=True)
        11/03/2015
        05/20/2018
        >>> d
        05/20/2018
        '''
        out = str(self)
        for _ in range(n):
            self.tomorrow()
            out += '\n'+str(self)
        if debug:
            out = out[:len(str(self))] + '\n' + str(self)
        print(out)
    def subNDays(self,n,**debug):
        '''
        >>> d = Date(1,4,2000)
        >>> d.subNDays(3)
        01/04/2000
        01/03/2000
        01/02/2000
        01/01/2000
        >>> d
        01/01/2000
        >>> d = Date(5,20,2018)
        >>> d.subNDays(929,debug=True)
        05/20/2018
        11/03/2015
        >>> d
        11/03/2015
        '''
        out = str(self)
        for _ in range(n):
            self.yesterday()
            out += '\n'+str(self)
        if debug:
            out = out[:len(str(self))] + '\n' + str(self)
        print(out)
    def __gt__(self,other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                return self.day > other.day
            else:
                return False
        else:
            return False
    def isAfter(self,other):
        '''
        >>> date1 = Date(11, 11, 2015)
        >>> date2 = Date(1, 1, 2016)
        >>> date1.isAfter(date2)
        False
        >>> date2.isAfter(date1)
        True
        >>> date1.isAfter(date1)
        False
        '''
        return self > other
    def __lt__(self,other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
            else:
                return False
        else:
            return False
    def isBefore(self,other):
        '''
        >>> d1 = Date(11, 11, 2015)
        >>> d2 = Date(1, 1, 2016)
        >>> d1.isBefore(d2)
        True
        >>> d2.isBefore(d1)
        False
        >>> d1.isBefore(d1)
        False
        '''
        return self < other
    def diff(self,other):
        '''
        >>> date1 = Date(11, 6, 2018)  # Tuesday lab date
        >>> date2 = Date(11, 22, 2018) # Thanksgiving
        >>> date2.diff(date1)
        16
        >>> date1.diff(date2)
        -16
        >>> # Make sure they didn't change.
        >>> print(date1)
        11/06/2018
        >>> print(date2)
        11/22/2018
         
        >>> # How long until graduation for Bucknell Class of 2020?
        >>> date3 = Date( 5, 17, 2020)
        >>> date3.diff(date1)
        558
        '''
        dif = 0
        copy = self.copy()
        while not(copy == other):
            if copy > other:
                dif += 1
                copy.yesterday()
            if copy < other:
                dif -= 1
                copy.tomorrow()
        return dif
    def dayOfWeek(self):
        '''
        >>> date = Date(12, 7, 1941)
        >>> date.dayOfWeek()
        'Sunday'
         
        >>> Date(10, 28, 1929).dayOfWeek()     # dayOfWeek is appropriate: crash day!
        'Monday'
         
        >>> Date(10, 19, 1987).dayOfWeek()     # ditto!
        'Monday'
         
        >>> date = Date(1, 1, 2100)
        >>> date.dayOfWeek()
        'Friday'

        >>> date = Date(4, 3, 2017)
        >>> date.dayOfWeek()
        'Monday'
        '''
        week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        ref = Date(11,5,2018)
        dayIndex = 0
        dif = self.diff(ref)
        if dif > 0:
            while (dif >= 7):
                dif -= 7
        if dif < 0:
            while (dif < 0):
                dif += 7
        return week[dif]
def newYearDayCounter():
    """
    each iteration checks if date.month = 1, and date.day = 1
        if correct date (1,1):
            matches day to dictionary and adds 1
    """
 
    # Set each counter to zero.
 
    dayOfWeekCounter = {}   # initialize a Python dictionary
    dayOfWeekCounter["Sunday"]    = 0
    dayOfWeekCounter["Monday"]    = 0
    dayOfWeekCounter["Tuesday"]   = 0
    dayOfWeekCounter["Wednesday"] = 0
    dayOfWeekCounter["Thursday"]  = 0
    dayOfWeekCounter["Friday"]    = 0
    dayOfWeekCounter["Saturday"]  = 0
 
    # Count the day of the week on January 1 for the next 100 years.
 
    for year in range(2018, 2119):    # We've passed the new year's day for the current year.
        date = Date(1, 1, year)
        print('Current date is', date)
        weekday = date.dayOfWeek()
        dayOfWeekCounter[weekday] += 1
 
    print('totals are', dayOfWeekCounter)
 
    # we could return dayOfWeekCounter here
    # but we don't need to right now
    # return dayOfWeekCounter
def birthdayCounter():
    dayOfWeekCounter = {}   # initialize a Python dictionary
    dayOfWeekCounter["Sunday"]    = 0
    dayOfWeekCounter["Monday"]    = 0
    dayOfWeekCounter["Tuesday"]   = 0
    dayOfWeekCounter["Wednesday"] = 0
    dayOfWeekCounter["Thursday"]  = 0
    dayOfWeekCounter["Friday"]    = 0
    dayOfWeekCounter["Saturday"]  = 0
 
    # Count the day of the week on January 1 for the next 100 years.
 
    for year in range(2018, 2119):    # We've passed the new year's day for the current year.
        date = Date(7, 4, year)
        print('Current date is', date)
        weekday = date.dayOfWeek()
        dayOfWeekCounter[weekday] += 1
 
    print('birthday totals are', dayOfWeekCounter)
import doctest
doctest.testmod()