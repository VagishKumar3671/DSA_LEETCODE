class Solution(object):
    def topKFrequent(self, words, k):
        dic = {}
        for i in words:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sort_item = sorted(dic.items(),key=lambda x: (-x[1], x[0]))
        return [item[0] for item in sort_item[:k]]