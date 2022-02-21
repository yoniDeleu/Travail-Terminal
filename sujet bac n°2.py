def moyenne (a):
    s=0
    n=0
    for e in a:
        note = e[0]
        coef = e[1]
        s = s + note * coef
        n = n + coef
    return s/n

def pascal (n):
    C=[[1]]
    for k in range(1, n+1):
        Ck = [1]
        for i in range (1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C
