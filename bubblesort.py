def bubblesort(arr):
    issorted = False
    end = len(arr)-1
    while not issorted:
        issorted = True
        for i in range(0, end):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                issorted = False
        end-=1
    return arr

arr = [5,32,67,3,3,7,35,89]
print(bubblesort(arr))