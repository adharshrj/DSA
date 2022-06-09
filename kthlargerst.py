#  TC = 2n*(k-1)+n = 2kn-n = O(kn)  SC = O(1)
def kthlargestkn(nums, k):
    for i in range(k-1):
        nums.remove(max(nums))
    return max(nums)

arr = [2, 6, 4, 5, 7, 9]
print(kthlargestkn(arr, 3))

# Sorting the list TC = O(nlogn) + O(1) = O(nlogn)
def kthlargestnlogn(nums, k):
    nums.sort()
    l = len(nums)
    return nums[l - k]

# Priority Queue using heaps TC = O(n + klogn) SC = O(n)
import heapq
def kthlargesthheap(nums, k):
    nums = [-e for e in nums]
    heapq.heapify(nums)
    for i in range(k-1):
        heapq.heappop(nums)
    return -heapq.heappop(nums)