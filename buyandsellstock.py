# Given an array of nums find the best time to buy and sell so the profit is maximum

def maxProfit(nums):
    l, r = 0, 1
    maxP = 0
    while r <= len(nums)-1:
        if nums[l]<nums[r]:
            profit = nums[r]-nums[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r+=1
    return maxP