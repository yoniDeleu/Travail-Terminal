def conv_bin(n):
    if n < 0:
        return None
    nb_bit = 1
    bin= [n % 2]
    n = n // 2
    while n:
        nb_bit += 1
        bin = [n % 2] + bin
        n = n // 2
    return (bin, nb_bit)


def tri_bulles(T):
    n = len(T)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T
