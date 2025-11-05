class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        if nums[0]==nums[len(nums)-1]:
            return 0
        max_ans = 0
        for i in range(len(nums) - 1):  
            max_ans = max(max_ans, nums[i + 1] - nums[i])
        return max_ans