class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp = ''
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][:i+1] != strs[j+1][:i+1]:
                    return temp
            temp = strs[0][:i+1]
        return temp