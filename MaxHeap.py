def Parent(i):
    return(i//2)

def Left(i):
    return 2 * i 

def Right(i):
    return 2 * i + 1

def maximum(A):
    return A[0]

def extract_maximum(A):
    if len(A) < 0:
        return ("Heap underflow")
    max = A[0]
    A[0] = A[len(A) -1]
    del A[len(A) -1]
    heapify(A,0)
    return max

def increase_key(A,i,key):
    if key < A[i]:
        return("New key is smaller than current key")
    A[i] = key
    while i > 0 and A[Parent(i)] < A[i]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)

def insert(A,key):
    A.append(key)
    increase_key(A,len(A)-1,key)
    return A

def heapify(A,i):
    l = Left(i)
    r = Right(i)
    largest = i
    
    if l < len(A) and A[l] > A[i]:
        largest = l
        
    if r < len(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A,largest)

def buildHeap(A):    ### Build Max-Heap
    for i in range((len(A)//2),-1,-1):
        heapify(A,i)

