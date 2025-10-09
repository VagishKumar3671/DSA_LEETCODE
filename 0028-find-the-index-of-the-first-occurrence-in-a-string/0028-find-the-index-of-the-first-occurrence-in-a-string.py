class Solution(object):
    def strStr(self, haystack, needle):
        if(len(haystack)==0 or len(needle)==0):
            return 0
        for i in range(len(haystack)-len(needle)+1):
            j=0
            while j<len(needle) and haystack[i+j]==needle[j]:
                j+=1
            if j==len(needle):
                return i
        return -1