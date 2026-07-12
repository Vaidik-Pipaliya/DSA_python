class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        hash_ = {}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hash_:
                return [hash_[remaining],i]
            hash_[nums[i]] = i 
        