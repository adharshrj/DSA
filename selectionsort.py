def selectionsort(arr):
    for sorted_arr in range(len(arr)):
        smallest = sorted_arr
        for unsorted_arr in range(sorted_arr+1, len(arr)):
            if arr[smallest] > arr[unsorted_arr]:
                smallest = unsorted_arr
        arr[smallest], arr[sorted_arr] = arr[sorted_arr], arr[smallest]
    return arr
arr = [5,32,67,3,3,7,35,89]
print(selectionsort(arr))