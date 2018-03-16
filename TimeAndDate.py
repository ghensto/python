#!/usr/bin/python3
# Abiola ADIMI
# Program that displays times and dates

def main():
    #Prints the standard 
    print("Standard time:")
    time1 = Time(8,36,0,'PM')
    print( time1.getTime() )
    time1.showTime();
    print()

    #Prints the standard date
    print("Standard date:")
    date1 = Date(13,10,2015)
    print( date1.getDate())
    date1.showDate()
    print()

    #Prints the date and time
    print("Date time: ")
    dt1 = DateTime(8,36,0,'PM',13,10,2015)
    print(dt1.getDateTime())
    dt1.showDateTime()
    print()

    #Prints the military time and the conversion to standard time
    print("Military time:")
    mt1 = MilitaryTime(2236,22)
    print(mt1.getMilitaryTime())
    mt1.showMilitaryTime()
    mt1.showStandardTime()
    
#Base class for displaying time     
class Time:

    #Constructor
    def __init__(self, hour=0, minute=0, second=0, period = 'AM'):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.period = period

    #Returns the time
    def getTime(self):
        return (self.hour, self.minute, self.second, self.period)

    #Sets the time
    def setTime(self, hour, minute, second, period):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.period = period

    #Displays the time
    def showTime(self):
        print("{}:{}:{} {}".format(self.hour, self.minute, self.second, self.period))

#Class that inherits Time() attributes and displays the military time
class MilitaryTime(Time): 

    #Constructors
    def __init__(self, militaryHours=0, militarySeconds=0):
        self.militaryHours = militaryHours
        self.militarySeconds = militarySeconds

    #Returns getMilitary time
    def getMilitaryTime(self):
        return(self.militaryHours, self.militarySeconds)

    #Set the military Time
    def setMilitaryTime(self, militaryHours=0, militarySeconds=0):
        self.militaryHours = militaryHours
        self.militarySeconds = militarySeconds

    #Displays the military time
    def showMilitaryTime(self):
        print("{}:{}, hours".format(self.militaryHours, self.militarySeconds))

    #Convert the military time to standard
    def convertToStandard(self):
        hrs = round(int(self.militaryHours / 100))
        mn = round(((self.militaryHours / 100) - hrs)*100)
        
        if(hrs <= 12):
            self.hour = hrs
            self.minute = mn
            self.second = self.militarySeconds
            self.period = "AM"
            
        if(hrs > 12):
            d = {24:12, 23:11, 22:10, 21:9, 20:8, 19: 7, 18:6, 17:5, 16:4, 15:3, 14:2, 13:1}
            self.hour = d[hrs]
            self.minute = mn
            self.second = self.militarySeconds
            self.period = "PM"
            
        
    #Displays the standard time
    def showStandardTime(self):
        self.convertToStandard()
        self.showTime()

#Base class for displaying the date
class Date:

    #Constructor
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    #Return the date
    def getDate(self):
        return(self.day, self.month, self.year)

    #Set the date
    def setDate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    #Displays the the date    
    def showDate(self):
        
        dicty = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August",
                 9:"September", 10:"October", 11:"November", 12:"December"}
        self.month = dicty[self.month]
        print(self.month,self.day,",", self.year)


#Class that inherites Time() and Date attributes to display the date and the time 
class DateTime(Time, Date):

    #Constructor
    def __init__(self, hour, minute, second, period, day, month, year):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.period = period
        self.day = day
        self.month = month
        self.year = year 

    #Returns the time
    def getDateTime(self):
        return(self.hour, self.minute, self.second, self.period, self.day, self.month, self.year)

    #Sets the time
    def setDateTime(self, hour, minute, second, period, day, month, year ):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.period = period
        self.day = day
        self.month = month
        self.year = year 

    #Displays the time
    def showDateTime(self):

        dicty = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August",
                 9:"September", 10:"October", 11:"November", 12:"December"}
        self.month = dicty[self.month]    
        print("{}:{}:{} {}".format(self.hour, self.minute, self.second, self.period))
        print(self.month, self.day,",", self.year)
    
main()
