class Solution(object):
    def maximumCount(self, nums):
        if nums[0] > 0:
            return len(nums)
        nc = 0 
        for i in range(len(nums)):
            if nums[i] < 0:
                nc += 1
            elif nums[i] == 0:
                continue
            else:
                return max(nc, len(nums) - i)
        return max(nc, 0)
