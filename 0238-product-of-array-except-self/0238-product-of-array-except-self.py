class Solution(object):
    def productExceptSelf(self, nums):
        if len(nums) == 2:
            return nums[::-1]
        pre = [1] * len(nums)
        post = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        return res
