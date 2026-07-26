class Solution(object):

    def binary(self, nums, target, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary(nums, target, mid + 1, high)
        else:
            return self.binary(nums, target, low, mid - 1)

    def search(self, nums, target):
        return self.binary(nums, target, 0, len(nums) - 1)