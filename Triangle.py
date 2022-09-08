def solutoin (A):
    if len (A)<3:
        return 0

    A.sort()
    for i in range(0, len(A)-2):
        #if (A[i]>A[i+2]-A[i+1]):
        if (A[i]+A[i+1]>A[i+2]):
            return 1

    return 0