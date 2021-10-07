#Ex 10
def tri2(t):
    """
    res=[]
    for i in range(len(t)):
        res=res+[0]
    res=[]
    """
    for i in range(len(t)):
        res.append(0)
        res=[0] * len(t)
        res[0] = t[0]
        for i in range(1, len(t)):
            j = i
            v = t[i]
            while j > 0 and t[j - 1] > v:
                t[j] = t[j - 1]
                j = j - 1
            t[j] = v