
# Abiola Adimi
# Employee Payroll Program

import re

def main():
    print("**************** Payroll Program ****************")
    print()
    print("****************   Data Input    ****************")
    numEmployees = int(input("Please enter the number of employees: "))
    print()
    
    employeeNames = []
    employeeRates = []
    employeeHours = []
    employeeWages = []

    for employeeNumber in range(numEmployees):
        
        
        while True:
            
            #Initiates exceptions handling
            try:
                print("Data entry for employee", employeeNumber)
                name = readName()
                rate = readRate()
                hours = readHours()
            
            #Checks error in name entered              
            except EmpNameError as n:
                print(n, "\nPlease start over\n")
                continue
            
            #Checks error in rate entered     
            except RateError as r:
                print(r, "\nPlease start over\n")
                continue
            
            #Checks error in hours entered 
            except HoursError as h:
                print(h, "\nPlease start over\n")
                continue
            
            #Adds informations to list
            else:
                employeeNames.append(name)
                employeeRates.append(rate)
                employeeHours.append(hours)
                employeeWages.append(employeeHours[employeeNumber] * employeeRates[employeeNumber])
                print()
                break
            print()
            print()
            
    
    
    #Displays the informations gathered    
    else:
        print("****************  Payroll Data  ****************")
        for employeeNumber in range(numEmployees):
            print("Employee: {}".format(employeeNames[employeeNumber]))
            print("   Hours: {}".format(employeeHours[employeeNumber]))
            print("   Rate:  ${}/hr".format(employeeRates[employeeNumber]))
            print("   Wage:  ${}".format(employeeWages[employeeNumber]))
            print()



# Thrown if employee name is zero length
class EmpNameError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Thrown if hourly rate <0 or > 20
class RateError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Thrown if weekly hours <0 OR > 60
class HoursError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



#Function readName
def readName():
    
    name = input("Enter the employee name: ")
    
    if (len(name) == 0):
        raise EmpNameError("Name cannot be zero length")
    
    elif(name.isnumeric()):
        raise EmpNameError("Data entered in incorrect format")
    
    else:
        return name

#Function readRate
def readRate():
    
    rateString = input("Enter the employee wage rate (0..20): ")
    
    check = re.compile("[a-z]", re.IGNORECASE);
    if(re.search(check,rateString)):
        k = True
    else:
        k = False
    
    if(k is not True ):
        rate = float(rateString)
        
        if (rate >= 0 and rate <= 20):
            return rate
        
        else:
            raise RateError("Rate must between 0 and 20")
        
    else:
        raise RateError("Data entered in incorrect format")    


#Function readHours
def readHours():
    
    hoursString = input("Enter the employee hours (0..60): ")
    
    check = re.compile("[a-z]", re.IGNORECASE);
    if(re.search(check, hoursString)):
        k = True
    else:
        k = False
    
    if(k is not True ):
        
        hours = float(hoursString)  
        
        if (hours >= 0 and hours <= 60):   
            return hours
        
        else:
            raise HoursError("Hourly rate must between 0 and 60")
        
    else:
        raise HoursError("I'm an integer")
    
if __name__ == "__main__": main()

