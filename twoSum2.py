''' Write a function that takes in a non-empty array of distinct integers and
an integer representing a target sum. If any two numbers in the input array 
sum up to the target sum, the function should return them in an array,in any order. 
If no two numbers sum up to the target sum, the function should return an empty array.'''
# time: O(N^2) space:O(1)
def twosumonn(array, sum):
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if (array[i] + array[j] == sum) and (i!=j):
                return [array[i], array[j]]
    return []
print(twosumonn([12,3,1,2,-6,5,-8,6], 0))

# time: O(N) space:O(1)
def twosumon(array, sum):
    for i in range(0, len(array)):
        first = array[i]
        second = sum - first
        if second in array[i+1:]:
            return sorted([first, second])
    return []
print(twosumon([12,3,1,2,-6,5,-8,6], 0))

# time O[logN] space O(1) Binary search:
def twosumbs(array, sum):
    array.sort()
    first = 0
    last = len(array) - 1
    while last>first:
        csum = array[first] + array[last]
        if csum == sum:
            return [array[first], array[last]]
        if csum < sum:
            first+=1
        if csum > sum:
            last-=1
    return []
print(twosumon([12,3,1,2,-6,5,-8,6], 0))