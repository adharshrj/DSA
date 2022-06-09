# Floyd's cycle finding algorithm approach

def find_duplicates(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break
    
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast: break
    return slow
