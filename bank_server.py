from MaxHeap import *
from MinHeap import *
from ReadFile import file_name



heap = []

# Gets informations from a .txt file
name, priority = file_name("customer_info.txt")

#Converts string of numbers to integers
priority = map(int,priority)         
customers = dict(zip(name,priority))

priorities = priority

#Inserts priority numbers inside heap
for i in range(len(priority)):
    insert(heap,priority[i])

#Displays the name of the next customer in line
print("Customers name by highest priority:\n")
for i in range(len(heap)):
    maxim = extract_maximum(heap)
    for name, priority in customers.items():
        if maxim == priority:
            print("{}\n".format(name))

## Uncomment this to display names using Min_Priority_Queue
##print '\n'
##print '\n'
##
###Inserts priority numbers inside heap
##for i in range(len(priorities)):
##    min_insert(heap,priorities[i])
##
###Displays the name of the next customer in line
##print("Customers name by lowest priority:\n")
##for i in range(len(heap)):
##    minim = extract_minimum(heap)
##    for name, priority in customers.items():
##        if minim == priority:
##            print("{}\n".format(name))
##
##
