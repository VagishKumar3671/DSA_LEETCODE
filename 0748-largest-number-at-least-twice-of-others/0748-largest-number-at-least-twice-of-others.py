class Solution(object):
    def dominantIndex(self, nums):
        maxi = max(nums)
        ind = nums.index(maxi)
        for num in nums:
            if num != maxi and maxi < 2 * num:
                return -1
        return ind
