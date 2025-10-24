class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums) == 1:
            return nums
        if len(set(nums)) == k:
            return list(set(nums))
        
        # Count frequency
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1  # increment count
        
        # Sort by frequency descending
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        
        # Return top k keys
        return [item[0] for item in sorted_items[:k]]
