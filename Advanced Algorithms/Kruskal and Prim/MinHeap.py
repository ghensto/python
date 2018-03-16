def Parent(i):
    return(i//2)

def Left(i):
    return 2 * i 

def Right(i):
    return 2 * i + 1

def maximum(A):
    return A[0]

def extract_minimum(A):
    if len(A) < 0:
        return ("Heap underflow")
    min = A[0]
    A[0] = A[len(A) -1]
    del A[len(A) -1]
    min_heapify(A,0)
    return min

def increase_key(A,i,key):
    if key > A[i]:
        return("New key is smaller than current key")
    A[i] = key
    while i > 0 and A[Parent(i)] > A[i]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)

def min_insert(A,key):
    A.append(key)
    increase_key(A,len(A)-1,key)
    return A

def min_heapify(B,i):
    l = Left(i)
    r = Right(i)
    smallest = i

    if l < len(B) and B[l] < B[smallest]:
        smallest = l

    if r < len(B) and B[r] < B[smallest]:
        smallest = r

    if smallest != i:
        B[i], B[smallest] = B[smallest], B[i]
        min_heapify(B,smallest)
        
def build_min_heap(B):    ### Build Max-Heap or Min-heap
    for i in range((len(B)//2),-1,-1):
        min_heapify(B,i)
