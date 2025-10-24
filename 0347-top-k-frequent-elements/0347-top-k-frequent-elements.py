class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums)==1:
            return nums
        if len(set(nums))==k:
            return list(set(nums))
        dic = {i: nums.count(i) for i in set(nums)}
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]

