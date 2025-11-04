class Solution(object):
    def maximumCount(self, nums):
        if nums[0]>0:
            return len(nums)
        nc=0
        np=0
        for i in range(len(nums)):
            if nums[i]<0:
                nc+=1
            elif nums[i]==0:
                continue
            else:
                np=len(nums)-i
                break
        return max(nc,np)


        