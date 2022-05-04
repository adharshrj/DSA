''' Write a function that takes in a non-empty array of distinct integers and
an integer representing a target sum. If any three numbers in the input array 
sum up to the target sum, the function should return them in an array,in any order. 
If no three numbers sum up to the target sum, the function should return an empty array.'''

# time: O(N^3) space:O(1)
def threesumonnn(array, tsum):
    array.sort()
    output = []
    for i in range(0, len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                if (array[i] + array[j] + array[k] == tsum):
                    output.append([array[i], array[j], array[k]])
    return output
print(threesumonnn([12,3,1,2,-6,5,-8,6], 0))

def threesumnlogn(arr, sum):
    arr.sort()
    out = []
    for current in range(len(arr)):
        left = current + 1
        right = len(arr)-1 
        while left<right:
            res = arr[current] + arr[left] + arr[right]
            if res == sum:
                out.append([arr[current], arr[left], arr[right]])
                left+=1
                right-=1
            elif res < sum:
                left+=1
            else:
                right-=1
    return out
print(threesumnlogn([12,3,1,2,-6,5,-8,6], 0))

# Negatives 
def threesumnnegatives(arr, sum):
    arr.sort()
    out = []
    for current in range(len(arr)-2):
        if current > 0 or arr[current] == arr[current-1]:
            continue
        if arr[current]>0:
            break
        left = current + 1
        right = len(arr)-1 
        while left<right:
            res = arr[current] + arr[left] + arr[right]
            if res == sum:
                if len(out) ==0 or out[-1] != [arr[current], arr[left], arr[right]]:
                    out.append([arr[current], arr[left], arr[right]])
                left+=1
                right-=1
            elif res < sum:
                left+=1
            else:
                right-=1
    return out
