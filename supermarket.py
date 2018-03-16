# CSCI 2061, Assignment 09, Problem 02
# Abiola Adimi
# Supermarket program.

#Main function.
def main():
    
    #Shopping dictionary
    shoppingList = {'potato':2, 'lettuce':5, 'onion':1}

    #Inventory dictionary
    inventory = {'potato':6, 'lettuce':0, 'onion':32, 'carrot':15}

    #Prices dictionary
    prices = {'potato':4, 'lettuce':2, 'onion':1.5, 'carrot':3}
    

    #Prints Cub foods Inventory
    print("*********CUB Foods Inventory********")
    print("************************************")
    printInventory(inventory, prices)
    print()

    #Prints bill
    print("Your shopping bill is:")
    computeBill(inventory, shoppingList, prices)

#Function to process inventory
def printInventory(inv, pr):
    print("{:<8}     {:<8}     {:<8}       {:<8}".format("Item", "Price","Quantity","Value"))
    for (i, j), (k, l) in sorted(zip(inv.items(), pr.items())):
        print("{:<8}     ${:<8}     {:<8}       ${:<8}".format(i, l, j, (j*l)))

#Function to display the bill
def computeBill(inv, shp, pr):
    
    for ((i, j),(k, l),(m,n)) in sorted(zip(inv.items(), shp.items(), pr.items())):
        if(j == 0):
            print("{:<28} -out of stock".format(k))
        elif(j > l):
            print("{} {:<8} at ${:<8} each -total ${}".format(l,k,n,l*n))
if __name__ == "__main__": main()

