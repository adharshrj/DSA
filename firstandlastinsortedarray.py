class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0 or nums[0]>target or nums[-1]<target:
            return [-1,-1]
        
    
        def find_start(nums, target):
            if nums[0]==target:
                return 0
            start = 0
            end = len(nums)-1
            res = -1
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    res = mid
                    end = mid - 1
                elif nums[mid]<target:
                    start = mid+1
                else:
                    end = mid-1
            return res
        
        def find_end(nums, target):
            if nums[-1]==target:
                return len(nums)-1
            start = 0
            end = len(nums)-1
            res = -1
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    res = mid
                    start = mid + 1
                elif nums[mid]<target:
                    start = mid+1
                else:
                    end = mid-1
            return res
        
        start = find_start(nums, target)
        end = find_end(nums, target)
        return [start, end]


def first_and_last(arr, target):
    if len(arr)==0 or arr[0]>target or arr[-1]<target:
        return [-1, -1] 
    
    def first(arr, target):
        if arr[0]==target:
            return 0 
        start = 0
        end = len(arr)-1
        res = -1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target and nums[mid-1]<target:
                res = mid
                end = mid - 1
            elif nums[mid]>target:
                end = mid - 1
            else:
                start = mid+1
        return res

    def last(arr, target):
        if arr[-1]==target:
            return len(arr)-1
        start = 0
        end = len(arr)-1
        res = -1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target and nums[mid+1]>target:
                res = mid
                start = mid + 1
            elif nums[mid]>target:
                end = mid - 1
            else:
                start = mid+1
        return res
    
    start = first(arr, target)
    end = last(arr, target)
    return [start, end]
