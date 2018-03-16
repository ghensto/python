from Knuth_Morris_Pratt import kmp_matcher, compute_prefix
from read_string_info import fil



text = fil()
w = []
x = []
for i in range(0,len(text),2):
    w.append(text[i])
    
for i in range (1, len(text),2):
    x.append(text[i])
    
for i in range(len(w)):   
    w[i] =  list(w[i])
    x[i] = list(x[i])
    kmp_matcher(w[i],x[i])
    print(compute_prefix(x[i]))
