class Solution(object):
    def findFinalValue(self, nums, original):
        if original not in nums:
            return original
        nums=sorted(nums)
        for num in nums:
            if num==original:
                original=original*2
            elif num < original:
                continue
            else:
                break
        return original

