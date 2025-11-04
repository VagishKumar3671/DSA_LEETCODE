class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if len(nums)==1 and nums[0]==1:
            return 1
        if len(nums)==1 and nums[0]==0:
            return 0
        count=0
        temp=0
        for i in nums:
            if i==1:
                temp+=1
                count=max(temp,count)
            else:
                temp=0
        return count