# CSCI 2061, Final Project
# Abiola Adimi
# Portfolio tracker.
''' This program stores a collection of investments
and help the user keep track of the value of a group of stocks. '''

# Imports regular expression module for string processing
import re

# Main function
def main():

    # Empty list used for storing informations
    data = []

    # Dictionary for the menu choices
    menu = {'A': add, 'D': delete, 'L': load, 'U': update, 'R': report, 'Q': Quit}

    # Prints the menu
    choice = ""

    # Calls the menu choosen
    while choice != 'q' or choice != 'Q':
        choice = input(printMenu())

        # Add
        if choice == 'a' or choice == 'A':
            menu['A'](data)
            print()

        # Delete
        elif choice == 'd' or choice == 'D':

            # Checks if data is empty 
            if not data:
                print("There is nothing to be deleted!!")
            else:
                data = menu['D'](data)
            print()

        # Load
        elif choice == 'l' or choice == 'L':
            data = menu['L']()
            print()

        # Updates
        elif choice == 'u' or choice == 'U':

            # Checks if data is empty 
            if not data:
                print("There is nothing to be updated!!")
            else:
                data = menu['U'](data)
            print()

        # Report
        elif choice == 'r' or choice == 'R':

            # Checks if data is empty 
            if not data:
                print("There is nothing to report!!")
            else:
                menu['R'](data)
            print()

        # Quit
        elif choice == 'q' or choice == 'Q':
            menu['Q'](data)
            break

        # Redisplays the menu when choice is wrong
        else:
            print()
            print("Choose A, D, L, U, R or Q")
            print()
            printMenu()

# Function for displaying menu
def printMenu():
    
    return "(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? "

# Function for adding data
def add(data):
    
    print("Add a stock to your portfolio...")
    print()

    # Gets the company informations we want to add to the list
    ticket = input("Ticker: ")
    companyName = input("Company name: ")
    numberOfShares = input("Number of shares: ")
    price = input("Purchase price per share: $")
    latest = price

    # Stores the informations collected to a list
    newCompany = [ticket, companyName, numberOfShares, price, latest]

    # Appends the list to main list
    data.append(newCompany)
    return data
    
# Function for deleting data    
def delete(data):

    # Gets the name of the company whose informations should be deleted
    ticker = input("Enter the ticker symbol of the stock to remove: ")
    t = ticker.upper()

    # Index of data that is going to be deleted
    x = -1
    
    for i in range(len(data)):
        if(t == data[i][0] or t == data[i][1]):
            x = i
            break
        
    # Deletes the list of data matching the index    
    if(x >= 0):
        del data[x]
        
    return data

# Function for loading data from a file
def load():
    
    print("Load file: portfolio.dat")

    # Reads file and converts contents to list  
    f = open('portfolio.dat', 'r')
    newlst = []
    word = []
    for line in f:
        word = re.sub("[^\w.]", " ", line).split()
        newlst.append(word)
    f.close()

    # Puts words into list of list
    for i in range(len(newlst)):
        if(len(newlst[i]) > 5):
            str1 = newlst[i][1]
            str2 = newlst[i][2]
            temp = ' '.join([str1, str2])
            newlst[i][1] = temp
            del newlst[i][2]
            
    # Copy the list
    data = newlst[:]
    return data

# Function for updating data
def update(data):

    print("Update stock prices (<Return> to keep current value)...")
    print()

    #Updates the data inside list
    for i in range(len(data)):
        uInput = input("{}: ".format(data[i][0]))
        data[i][4] = uInput
    
    return data
    
# Function for displaying the data stored
def report(data):

    # Gets user choice for display type wanted
    sChoice = input("Sort output on (N)ame, or (V)alue? ")

    # Displays data in alphabetic order
    if(sChoice == 'n' or sChoice == 'N'):
        
        # Creates dictionary from list
        number = []
        for i in range(len(data)): 
            number.append(data[i][1])

        # Empty dictionary
        dic = {}
        
        for j in range(len(data)):
            dic[number[j]] = data[j]

        # Variables ininitialization    
        sumValue = 0
        sumGainLoss = 0
        latestTotal = 0
        purTotal = 0

        # Displays the title of the table
        print("{:28}    {:}    {:>6}    {:}   {:10} {:>}".format("Company", "Shares", "Pur.", "Latest", "Value", "G/L"))
        print("=============================================================================")

        # Displays informations
        for k, v in sorted(dic.items()):

            # Combines the string that form the name and the acronyme
            str1 = v[1]
            str2 = '(' + v[0] + ')'
            temp = ' '.join([str1, str2])

            # Calculates value and sum them
            value = int(round(float(v[2]) * float(v[4])))
            sumValue += value

            # Calculates gain and loss
            gainLoss = ((float(v[4]) - float(v[3]))/ float(v[3]))*100
            gtotal = (float(v[4])- float(v[3]))/ float(v[3]) * 100
            latestTotal += value
            purTotal += (float(v[3])* float(v[2]))

            # Displays companies with their data on the same line
            print("{:27} {:>8}    {:>8} {:>8} {:>8} {:8.1f}".format(temp, v[2], v[3], v[4], value, gainLoss))

        # Displays the total
        sumGainLoss = ((latestTotal - purTotal)/purTotal)*100
        sumGainLoss = round(sumGainLoss, 1)  #rounds
        print("                                                         -------------------")
        print("                                                             {}    {:4.1f}%".format(sumValue, sumGainLoss))
        print("                                                         ===================")

    # Displaays data in numerical order
    elif(sChoice == 'v' or sChoice == 'V'):
        
        # Creates dictionary from list
        number = []
        for i in range(len(data)): 
            number.append(data[i][1])

        dic = {}
        
        for j in range(len(data)):
            dic[number[j]] = data[j]

        # Variables ininitialization     
        sumValue = 0
        sumGainLoss = 0
        latestTotal = 0
        purTotal = 0

        # Displays the title of the table
        print("{:28}    {:}    {:>6}    {:}   {:10} {:>}".format("Company", "Shares", "Pur.", "Latest", "Value", "G/L"))
        print("=============================================================================")

        # Displays informations
        for k, v in sorted(dic.items(), reverse=True):

            # Combines the string that form the name and the acronyme
            str1 = v[1]
            str2 = '(' + v[0] + ')'
            temp = ' '.join([str1, str2])

            # Calculates value and sum them
            value = int(round(float(v[2]) * float(v[4])))
            sumValue += round(value,2)

            # Calculates gain and loss
            gainLoss = ((float(v[4]) - float(v[3]))/ float(v[3]))*100
            gtotal = (float(v[4])- float(v[3]))/ float(v[3]) * 100
            latestTotal += value
            purTotal += (float(v[3])*float(v[2]))

            # Displays companies with their data on the same line
            print("{:27} {:>8}    {:>8} {:>8} {:>8} {:8.1f}".format(temp, v[2], v[3], v[4], value, gainLoss))

        # Displays the total
        sumGainLoss = ((latestTotal - purTotal)/purTotal)*100
        sumGainLoss = round(sumGainLoss, 1)  #rounds
        
        print("                                                         -------------------")
        print("                                                             {}    {:4.1f}%".format(sumValue, sumGainLoss))
        print("                                                         ===================")

    # Redisplays the choice when a bad choice is made
    else:
        report(data)
        
# Function for quitting
def Quit(data):
    
    qchoice = input("Save portfolio.dat (y/n)?")

    # Saves information to .dat file on the disk
    if(qchoice == 'y' or qchoice == 'Y'):
        
        # Clears the file
        open('portfolio.dat', 'w').close()

        # Writes new data to the file
        f = open('portfolio.dat', 'w')
        for item in data:
          f.write("{}\n".format(item))
        f.close()

        print()
        print("File saved")

    # Does not save informations to the disk    
    elif(qchoice == 'n' or qchoice == 'N'):
        print("File not saved")
    print()    
    print("Bye.")
    
main()






