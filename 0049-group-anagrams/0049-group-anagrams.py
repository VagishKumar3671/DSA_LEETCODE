class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lis = []           
        keys = []           
        for word in strs:
            sorted_word = ''.join(sorted(word))  
            if sorted_word in keys:
                index = keys.index(sorted_word)
                lis[index].append(word)
            else:
                lis.append([word])
                keys.append(sorted_word)
        return lis
