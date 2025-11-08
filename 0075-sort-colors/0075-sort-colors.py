class Solution(object):
    def sortColors(self, nums):
        c0=c1=0
        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1:
                c1 += 1
            else:continue
        nums[:] = [0]*c0 + [1]*c1 + [2]*(len(nums)-(c0+c1))
        return nums
