from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        # Count frequency of each number
        count = Counter(nums)
        
        # Sort numbers by frequency (highest first)
        sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # Return top k frequent numbers
        return sorted_nums[:k]
