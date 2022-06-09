def fourSum(nums, target):
    temp, res = [], []
    def ksum(k, start, target):
        if k>2:
            for i in range(start, len(nums)-1):
                if i > start and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                ksum(k-1, i+1, target - nums[i])
                temp.pop()
            return
        
        l, r = start, len(nums)-1
        while l<r:
            cs = nums[l] + nums[r]
            if cs > target:
                r-=1
            elif cs < target:
                l+=1
            else: 
                res.append(temp + [nums[l], nums[r]])
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
        
    ksum(4, 0, target)   
    return res
