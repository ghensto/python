

def kmp_matcher(T,P):
    n = len(T)
    m = len(P) 
    s = compute_prefix(P)
    q = 0

    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = s[q-1]
        if P[q] == T[i]:
            q = q + 1
        if q == m:
            print("Start = {}".format(i-m+2))
            if i < n-1:
                q = s[q]
            else:
                return
                
def compute_prefix(P):
    m = len(P)-1
    s = range(m)
    s[0] = 0
    k = 0
    for j in range(1,m):
        while k > 0 and P[k] is not P[j]:
            k = s[k-1]
        if P[k] == P[j]:
            k = k + 1
        s[j] = k
    return s



