class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            return 1
        if target > nums[-1]:
            return len(nums)
        if target == nums[-1]:
            return len(nums) - 1
        if target <= nums[0]:
            return 0
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
