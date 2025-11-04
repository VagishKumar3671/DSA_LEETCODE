class Solution(object):
    def search(self, nums, target):
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        if max(nums)==target or min(nums)==target:
            if max(nums)==target:
                return len(nums)-1
            else:
                return 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1      