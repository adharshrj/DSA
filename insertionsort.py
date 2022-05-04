def insertionsort(arr):
    for i in range(0, len(arr)-1):
        j = i
        while j>0 and arr[j]<arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr

arr = [5,32,67,3,3,7,35,89]
print(insertionsort(arr))