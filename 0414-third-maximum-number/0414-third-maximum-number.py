class Solution(object):
    def thirdMax(self, nums):
        if len(set(nums)) < 3:
            return sorted(set(nums), reverse=True)[0]
        return sorted(set(nums), reverse=True)[2]
