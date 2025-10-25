class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''for i in range(min_list, max_list + 1]):
            if i in nums:
                lis.append(1)
                count += 1
                temp = max(temp, count)
            else:
                lis.append(0)
                count = 0

        return temp'''

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        if len(nums) == 2 and nums[0] == nums[1]:
            return 1
        nums =set(nums)
        temp = 0
        for i in nums:
            if (i - 1) not in nums:
                count = 1
                while (i + count) in nums:
                    count += 1
                temp = max(temp, count)
        return temp