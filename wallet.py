# CSCI 2061, Assignment 09, Problem 01
# Abiola Adimi
# Dictionary wallet program.

#Function Main
def main():
    
    #Nested 'wallet' Dictionary contains 'money', 'creditCards', 'IDs'. 
    wallet = {'money': {'two': 20, 'one': 10, 'zero': 5, 'four': 1},
            'creditCards': (['Visa', 'Discovery', 'MasterCard']),
            'IDs': (['Drivers License', 'Student ID'])
            }
    #Dictionary for converting strings numbers into integers
    number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    print("Wallet Contents:")
    print()

    #Displays the credit cards from the dictionary wallet.
    print("Credit Cards:")
    for c in wallet['creditCards']:
        print (c)
   
    print()

    #Displays the IDs from the the dictionary wallet.
    print("IDs:")
    for i in wallet['IDs']:
        print (i)

    print()

    #Calculates the total cash in the dictionary wallet.
    total = 0
    for key, val in wallet['money'].items():
        total += (val * number[key])
        
    print("Total cash is: ${}".format(total))

    print()
    print("After changes, wallet contents are:")
    print()

    #Adds coupons to the dictionary wallet.
    wallet['coupons'] = {'Cub': 'meat', 'Kohls': 'shirt', 'Target': 'toothpaste'}

    #Removes credit cards from the dictionary wallet.
    wallet['creditCards'].remove('Discovery')

    #Adds 3 $20 bills to the dictionary wallet.
    wallet['money'].update({'three': 20})

    #Displays the credit cards from the dictionary wallet.
    print("Credit Cards:")
    for c in wallet['creditCards']:
        print (c)
   
    print()

    #Displaying the IDs from the the dictionary wallet.
    print("IDs:")
    for i in wallet['IDs']:
        print (i)

    print()

    #Displaying the coupons from the dictionary wallet.
    print("Coupons:")
    for key, value in wallet['coupons'].items():
        print(key, " ",value)

    print()

    #Calculating the total cash in the dictionary wallet.
    total = 0
    for key, val in wallet['money'].items():
        total += (val * number[key])
    print("Total cash is: ${}".format(total))
   
if __name__ == "__main__": main()

