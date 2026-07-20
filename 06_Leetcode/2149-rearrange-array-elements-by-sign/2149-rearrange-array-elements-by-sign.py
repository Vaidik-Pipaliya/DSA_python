class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n
        pos, neg = 0, 1

        for i in range(n):
            if nums[i] >= 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2

        return result