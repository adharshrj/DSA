def stockbuysell(A, N):
    l, h = 0,1
    maxProfit = 0
    N = len(A)
    while h<N-1:
        if A[h]>A[l]:
            profit = A[h]-A[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = h
        h+=1
    return maxProfit