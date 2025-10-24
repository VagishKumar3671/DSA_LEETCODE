class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums) == 1:
            return nums
        if len(set(nums)) == k:
            return list(set(nums))
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]
