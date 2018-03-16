# CSCI 2061
# Abiola Adimi

#Class person
class Person(object):
    def __init__(self, name, age, address, typePerson):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson

    def restaurant(self):
        pass

    def order(self):
        pass
        
    def pay_bill(self, bill):
        self.bill = bill

#Class of type Millionaire
class Millionaire(Person):
    def __init__(self, name, age, address, typePerson, vacationHomes):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson
        self.vacationHomes = vacationHomes

    #Overrides restaurant from class person     
    def restaurant(self):
        print(' Restaurant: Driver, take me to Mannys Steakhouse')

    #Overrides order from class person
    def order(self):
        print(' Order: Caviar, filet mignon, lobster and several bottles of your best wine!')

    ##Overrides pay_bill from class person
    def pay_bill(self, bill):
        bill_new = bill + (bill*0.5)
        print(' Bill: Here you go ${} And keep the change!'.format(bill_new))
#Class of type Teacher
class Teacher(Person):
    def __init__(self, name, age, address, typePerson, mortgage):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson
        self.mortgage = mortgage

    #Overrides restaurant from class person
    def restaurant(self):
        print(' Restaurant: Honey, how about Chilis tonight?')

    #Overrides order from class person
    def order(self):
        print(' Order: Can I have the special?  And how much is a tall beer?')

    #Overrides pay_bill from class person
    def pay_bill(self, bill):
        self.bill = bill
        bill_new = bill + (bill*0.15)
        print(' Bill: Are you sure {} is correct?  OK, here is {}'.format(bill, bill_new))

class Student(Person):
    def __init__(self, name, age, address, typePerson, rent):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson
        self.rent = rent

    #Overrides restaurant from class person
    def restaurant(self):
        print(' Restaurant: MacDonalds or Culvers?')

    #Overrides order from class person
    def order(self):
        print(' Order: Burger and fries please!')

    #Overrides pay_bill from class person
    def pay_bill(self, bill):
        self.bill = bill
        print(' Bill: Can I owe you ten bucks or do the dishes?')



def main():
    persons = []
    again = 'Y'

    ## Input data for different people and add appropriate object to list
    while(again == 'Y' or again == 'y'):

        name = input('Please enter the name: ')
        
        age = input('Please enter the age: ')
        
        address = input('Please enter the address: ')
        
        typeOfPerson = input('Please enter the type of person: ')

        #Identifies the type of person
        if(typeOfPerson == 'Millionaire'):
            vacation = input('How many vacation homes does he/she have? ')
            persons.append(Millionaire(name, age, address, typeOfPerson, vacation))

        if(typeOfPerson == 'Teacher'):
            mortgage = input('How much mortgage is remaining? ')
            persons.append(Teacher(name, age, address, typeOfPerson, mortgage))

        if(typeOfPerson == 'Student'):
            rent = input('How much is rent this month? ')
            persons.append(Student(name, age, address, typeOfPerson, rent))
        

        again = input('Go again?')
        print()

    ## Display information for people in list
    for person in persons:
        print(person.typePerson, "", person.name)
        person.restaurant()
        person.order()
        bill = float(input(' What is the bill?'))
        person.pay_bill(bill)
        print()
      

if __name__ == '__main__': main()
