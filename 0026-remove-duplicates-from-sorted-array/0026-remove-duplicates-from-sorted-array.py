class Solution(object):
    def removeDuplicates(self, nums):
        # handle empty list
        if not nums:
            return 0

        # remove duplicates (extra space used here)
        unique = sorted(set(nums))

        # write unique values back into nums in-place
        for i in range(len(unique)):
            nums[i] = unique[i]

        # return number of unique elements
        return len(unique)
