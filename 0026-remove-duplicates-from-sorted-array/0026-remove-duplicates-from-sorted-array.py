class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        l = sorted(set(nums))
        for i in range(len(l)):
            nums[i] = l[i]
        return len(l)
