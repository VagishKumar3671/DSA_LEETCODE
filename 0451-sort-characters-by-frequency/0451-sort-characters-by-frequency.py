class Solution(object):
    def frequencySort(self, s):
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1 
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        result = ''
        for char, freq in sorted_items:
            result += char * freq
        return result
