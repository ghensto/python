import collections
from read_char_info import read_char
from printTree import*
from MinHeap import *

def getfreq():    
    H = []
    N = []
    ch = dict()
    new = []
    char = read_char()
    for i in range(len(char)):
        char[i] = list(char[i])
        l = len(char[i])
        if l > 120:
            print("Can't process more than 120 characters at the time")
            print("Check line {}".format(i+1))
            del char[i]
            
    new = collections.Counter(char[0])

    for key, value in new.items():
        ch[key] = value
    return  ch

#Creates huffman's tree with nodes.    
def hufftree(ch):
    freq = [(f,l) for (l,f) in ch.items()]
    build_min_heap(freq)
    while len(freq) >= 2:
        fx , zx = extract_minimum(freq)
        fy , zy = extract_minimum(freq)
        z  = fx, fy
        min_insert(freq, (fx + fy, {0: zx, 1:zy}))
                
    return extract_minimum(freq)[1]

#Traverses the tree created above and convert nodes into '0' or '1'
def hufftraverse(tree,prefix,code):
    for node in tree:
        if len(tree[node]) == 1:
            code[prefix+str(node)] = tree[node]

        else:
            hufftraverse(tree[node], prefix+str(node), code)


def huffcode(tree):
    code = {}
    hufftraverse(tree, '', code)
    return code




##############################################################################################################

fqcy = getfreq()
C = huffcode(hufftree(fqcy))
for key,value in sorted(C.items(), key =lambda v: v[1]):
    print value, ':', key


print '\n',"Huffman's Tree"
hc = printfreq()
printtree(hc)





