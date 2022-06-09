class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        omap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in omap:
                return [omap[diff], i]
            omap[n]=i
        return