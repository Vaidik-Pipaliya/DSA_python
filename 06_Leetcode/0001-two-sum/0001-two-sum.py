class Solution(object):
    # Optimal: Hash Map - O(N) Time, O(N) Space
    def twoSum(self, nums, target):
        n = len(nums)
        hash_ = {}
        for i in range(0, n):
            remaining = target - nums[i]
            if remaining in hash_:
                return [hash_[remaining], i]
            hash_[nums[i]] = i

    # Alternative: Brute Force - O(N^2) Time, O(1) Space
    def twoSumBruteForce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
