def sort_it_up(n, arr):
    left = 0
    right = n-1
    i = 0
    while i <= right:
        if arr[i] == 2:
            arr[i] = arr[right]
            arr[right] = 2
            right -= 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i] = arr[left]
            arr[left] = 0
            left += 1
            i += 1
    return arr

n = int(input())
arr = list(map(int, input().split()))

outp = sort_it_up(n, arr)