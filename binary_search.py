def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

def verify(index):
        if index is not None:
            print("Target in list",index)
        else:
            print("Target not in list")

import math
def pefsqrt(index):
    if math.sqrt(index)%2==0:
        return index
    else:
        return None

    
numbers = [1,2,3,4,5,6,7,8,9,10]
unsorted = [5,3,6,3,9,0,2,31,1]

result = binary_search(numbers, 97)
result2 = binary_search(numbers, 9)
result3 = binary_search(unsorted, 31)
result4 = binary_search(unsorted, 122)


verify(result)
verify(result2)
verify(result3)
verify(result4)

