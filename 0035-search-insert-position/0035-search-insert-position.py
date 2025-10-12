class Solution(object):
    def searchInsert(self, nums, target):
        # Case 1: Only one element
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            return 1

        # Case 2: Target is greater than or equal to last element
        if target > nums[-1]:
            return len(nums)

        # Case 3: Target is smaller than the first element
        if target <= nums[0]:
            return 0

        # Case 4: Binary Search for correct position
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
